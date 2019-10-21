class TurretCommand:
    def __init__(self, f_vel=0, a_vel=0):
        # Forward Velocity - Ranges from -100 to 100 where 0 is stopped
        self.f_vel = f_vel
        # Angular Velocity - Ranges from -100 to 100 where left is positive
        self.a_vel = a_vel

    def __eq__(self, other):
        if other == None:
            return False
        if self.f_vel==other.f_vel and self.a_vel==other.a_vel:
             return True
        else:
             return False

    def __str__(self):
        return "Command: f_vel: {0} a_vel: {1} ".format(self.f_vel,self.a_vel)




if __name__ == "__main__":
    a = TurretCommand(f_vel=1, a_vel=0)
    b = TurretCommand(f_vel=1, a_vel=1)
    print(a==b)
