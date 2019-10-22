import numpy as np
import cv2

def nothing(x):
    pass

win_name = "Visual"
cap = cv2.VideoCapture(0)
cv2.namedWindow(win_name)
cv2.createTrackbar('t1-1', win_name, 0, 255, nothing)
cv2.createTrackbar('t1-2', win_name, 0, 255, nothing)
cv2.createTrackbar('t1-3', win_name, 0, 255, nothing)
cv2.createTrackbar('t2-1', win_name, 255, 255, nothing)
cv2.createTrackbar('t2-2', win_name, 255, 255, nothing)
cv2.createTrackbar('t2-3', win_name, 255, 255, nothing)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    ## convert to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    t11 = cv2.getTrackbarPos('t1-1', win_name)
    t12 = cv2.getTrackbarPos('t1-2', win_name)
    t13 = cv2.getTrackbarPos('t1-3', win_name)
    t21 = cv2.getTrackbarPos('t2-1', win_name)
    t22 = cv2.getTrackbarPos('t2-2', win_name)
    t23 = cv2.getTrackbarPos('t2-3', win_name)
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
        pass
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
    cv2.imshow(win_name,frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# import numpy as np
# import cv2
# from cv2 import Feature2D as f2d
# from matplotlib import pyplot as plt
#
# img = cv2.imread('greenshirt.jpeg')
# #cv2.imshow('uncontoured', img)
# #cv2.waitKey(0)
# imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# ret, thresh = cv2.threshold(imgray, 80, 255, 0)
# #print(ret)
# #print(thresh[60])
# im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# print(len(contours))
#
# img2 = cv2.drawContours(img, contours, -1, (0,255,0), 5)
#
# cv2.imshow('contoured', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
