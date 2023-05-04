'''-----------------------------------------------------------------------------------------------------#
#                                                                                                       #
# Program : Initialization for a 6DOF robot arm                                                         #
# Author  : Udofia, Silas Silas                                                                         #
# Project : ROBOT ARM                                                                                   #
# Model   : XS100                                                                                      #
# Ser_Nom : RB346A6DOFUSSOCT92022                                                                       #
# Date    : October 9, 2022                                                                             #
#                                                                                                       #   
# (inverse kinematics) Given the desired end effector position vector and orientation, solves           #
# for the joint variables th1, th2, th3, th4, th5, th6                                                  #
#                                                                                                       #
-----------------------------------------------------------------------------------------------------'''

from IKT100 import IKT100 as _6DOF

class T100_INIT:
    
    T100 = _6DOF()
    
#The initial t1,t2 and t3 is 0, 90 and -90 degrees respectively, in order to set
#t1,t2, and t3, we need a way of initializing the system with an empty orientation
#of row pitch and yaw and to be 90,0,0 respectively such that the orientation
#does not affect the values of t1,t2 and t3, hence we can find new t1,t2, and t3
#original values for the given position, hence pass the result of initial t1,t2 and t3
#to the set1,2,3 function and get new results of t1,t2 and t3
#given a new orientation which affects the robot motion.
   
    
    #===========================================================================================================
    def setPosition(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        #=======================================================================================================
    def setOrientation(self, y=0,p=0,r=0):
        self.yaw = y
        self.pitch = p
        self.roll = r
        #=======================================================================================================
    def Start(self):
        for i in range(7):
            #DESIRED END EFFECTOR POSITION VECTOR FOR ALL CONDITIONS OF PX !> A1 + A2 + A3 + D6 && PY !> A1 + A2 + A3 + D6 && PZ !> A1 + A2 + A3 + D6 + D1
            self.T100.setPosition(self.x,self.y,self.z) #Initial position
            self.T100.setRPY(90,0,0)#Initial orientation
            # #=======================================================================================================
            self.T1 = self.T100.GET_TH1_DEG()#Inital value of theta_1
            self.T2 = self.T100.GET_TH2_DEG()#Initial value of theta_2
            self.T3 = self.T100.GET_TH3_DEG()#Initial value of theta_3
            # #=======================================================================================================
            #=======================================================================================================
            #THE POSITION HAS TO CORRESPOND WITH THE VALUES OF T1,T2 AND T3
            #TO GET THE ACTUAL VALUES OF T1,T2 AND T3 FOR THE INPUTED POSITION VECTOR, WE RUN AN INITIAL VALUE TEST WITH EMPTY ORIENTATIONS TO GET THE VALUES OF T1,T2,T3 CORRESPONDING TO THAT POSITON
            self.T100.setT1(self.T1)
            self.T100.setT2(self.T2)
            self.T100.setT3(self.T3)
            #=======================================================================================================
            self.T100.setPosition(self.x,self.y,self.z)
            self.T100.setRPY(self.roll, self.pitch, self.yaw) #Roll,Pitch,(Yaw = 90 deg default)
            #=======================================================================================================
     
    def getT1(self):
        return self.T100.getT1()
    
    def getT2(self):
        return self.T100.getT2()
    
    def getT3(self):
        return self.T100.getT3()
    
    def getT4(self):
        return self.T100.getT4()
    
    def getT5(self):
        return self.T100.getT5()
    
    def getT6(self):
        return self.T100.getT6()

    def getH0_3(self):
        return self.T100.H0_3()    

    def getH3_6(self):
        return self.T100.H3_6stringf()
    
    def getH0_6(self):
        return self.T100.H0_6stringf() 

    def getWristCenter(self):
        return self.T100.getWristCenter()    

   #-----------------------------------------------------------------     

    def getT1_Output(self):
        return self.T100.GET_TH1_DEG()

    def getT2_Output(self):
        return self.T100.GET_TH2_DEG()

    def getT3_Output(self):
        return self.T100.GET_TH3_DEG()

    def getT2Servo(self):
        return (180 - round(self.T100.GET_TH2_DEG())) + 45

    def getT3Servo(self):
        return (180 + (round(self.T100.GET_TH3_DEG()))) - 45

    def getT4_Output(self):
        return self.T100.GET_TH4_DEG()

    def getT5_Output(self):
        return self.T100.GET_TH5_DEG()

    def getT6_Output(self):
        return self.T100.GET_TH6_DEG()


    






