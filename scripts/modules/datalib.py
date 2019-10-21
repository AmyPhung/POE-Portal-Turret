class RobotCommand:
    def __init__(self, f_vel=0, a_vel=0, r_turret=0, l_turret=0):
        # Forward Velocity - Ranges from -100 to 100 where 0 is stopped
        self.f_vel = f_vel
        # Angular Velocity - Ranges from -100 to 100 where left is positive
        self.a_vel = a_vel
        # Shooting speed - Ranges from 0 to 100
        self.r_turret = r_turret
        self.l_turret = l_turret

    def __eq__(self, other):
        if other == None:
            return False
        if self.f_vel==other.f_vel and self.a_vel==other.a_vel and \
           self.r_turret==other.r_turret and self.l_turret==other.l_turret:
             return True
        else:
             return False

    def __str__(self):
        return "Command: f_vel: {0} a_vel: {1} r_turret: {2} l_turret {3}". \
               format(self.f_vel,self.a_vel,self.r_turret,self.l_turret)




if __name__ == "__main__":
    a = RobotCommand(f_vel=1, a_vel=12)
    b = RobotCommand(f_vel=1, a_vel=1)
    print a==b
