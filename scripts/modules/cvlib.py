import numpy as np
import cv2

T11 = 147
T12 = 26
T13 = 120
T21 = 213
T22 = 186
T23 = 255

class TrackingSystem:
    def __init__(self, gui=True):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640/100) # Turn down resolution
        self.cap.set(4, 480/100)

        self._gui = gui
        if gui:
            self._win_name = "Visual"
            cv2.namedWindow(self._win_name, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(self._win_name,600,600)
            cv2.createTrackbar('t1-1', self._win_name, T11, 255, nothing)
            cv2.createTrackbar('t1-2', self._win_name, T12, 255, nothing)
            cv2.createTrackbar('t1-3', self._win_name, T13, 255, nothing)
            cv2.createTrackbar('t2-1', self._win_name, T21, 255, nothing)
            cv2.createTrackbar('t2-2', self._win_name, T22, 255, nothing)
            cv2.createTrackbar('t2-3', self._win_name, T23, 255, nothing)

        # TODO: Set Defaults
        # TODO: Have saveable files

    def update(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        ## convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if self._gui:
            t11 = cv2.getTrackbarPos('t1-1', self._win_name)
            t12 = cv2.getTrackbarPos('t1-2', self._win_name)
            t13 = cv2.getTrackbarPos('t1-3', self._win_name)
            t21 = cv2.getTrackbarPos('t2-1', self._win_name)
            t22 = cv2.getTrackbarPos('t2-2', self._win_name)
            t23 = cv2.getTrackbarPos('t2-3', self._win_name)
        else:
            t11 = T11
            t12 = T12
            t13 = T13
            t21 = T21
            t22 = T22
            t23 = T23

        mask = cv2.inRange(hsv, (t11, t12, t13), (t21, t22, t23))
        ## slice the green
        imask = mask>0
        color = np.zeros_like(frame, np.uint8)
        color[imask] = frame[imask]

        h, s, imgray = cv2.split(color)
        ret, thresh = cv2.threshold(imgray, 30, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        max_area=100
        ci=0
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i

    	#Largest area contour
        if ci>=len(contours): #Passes if color cannot be found
            print("No Contours Found")
            if self._gui:
                cv2.imshow(self._win_name,frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    pass
            return None
        else:
            cnts = contours[ci]

        #Find convex hull
        hull = cv2.convexHull(cnts)

    	#Find moments of the largest contour
        moments = cv2.moments(cnts)

        #Central mass of first order moments
        if moments['m00']!=0:
            cx = int(moments['m10']/moments['m00']) # cx = M10/M00
            cy = int(moments['m01']/moments['m00']) # cy = M01/M00
        else:
            print("No Moments Found")
            return None
        centerMass=(cx,cy)

        #Draw center mass
        cv2.circle(frame,centerMass,7,[100,0,255],2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'Center',tuple(centerMass),font,2,(255,255,255),2)

        #Print x and y coordinates
        cv2.putText(frame,str(cx),(100,200),font,2,(255,255,255),2)
        cv2.putText(frame,str(cy),(100,300),font,2,(255,255,255),2)

        #Print bounding rectangle
        #x,y,w,h = cv2.boundingRect(cnts)
        #img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.drawContours(frame,[hull],-1,(255,255,255),2)

        img2 = cv2.drawContours(frame, contours, -1, (0,255,0), 5)

        # Display the resulting frame
        if self._gui:
            cv2.imshow(self._win_name,frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                pass

        # Remap cx to -1000 to 1000 range
        cx = int(reMap(cx - np.shape(frame)[1]/2,
                   np.shape(frame)[1]/2, -np.shape(frame)[1]/2,
                   100, -100))

        return cx,cy # In frame, pixels off center - origin is center of image

def nothing(x):
    pass

def reMap(value, maxInput, minInput, maxOutput, minOutput):

	value = maxInput if value > maxInput else value
	value = minInput if value < minInput else value

	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput

	scaled_value = float(value - minInput) / float(inputSpan)

	return minOutput + (scaled_value * outputSpan)


if __name__ == "__main__":
    t = TrackingSystem()
    while True:
        t.update()
