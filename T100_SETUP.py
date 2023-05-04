'''-----------------------------------------------------------------------------------------------------#
#                                                                                                       #
# Program : Main activation code for a 6DOF robot arm                                                   #
# Author  : Udofia, Silas Silas                                                                         #
# Project : ROBOT ARM                                                                                   #
# Model   : RB346A                                                                                      #
# Ser_Nom : RB346A6DOFUSSOCT92022                                                                       #
# Date    : October 9, 2022                                                                             #
#                                                                                                       #   
# (inverse kinematics) Given the desired end effector position vector and orientation, solves           #
# for the joint variables th1, th2, th3, th4, th5, th6                                                  #
#                                                                                                       #
-----------------------------------------------------------------------------------------------------'''
from machine import Pin, SoftI2C
from KeyPad4x4 import KeyPad4x4
from T100_INIT import T100_INIT
from FKT100 import FKT100
from time import sleep
import sh1106
import math

class T100_SETUP:

    RB = T100_INIT()
    
    Forward_Kinematics = FKT100()
    
    keyPad = KeyPad4x4(21,16,15,23,2,4,5,22)
    keyPad.init()
    
    i2c = SoftI2C(scl=Pin(18), sda=Pin(19))
    
    display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
    display.sleep(False)
    display.fill(0)
    display.invert(True)
    
    
    T1 = 90
    T2 = 70 #120 deg max
    T3 = -100 #60 deg min : 120 deg max

    T4 = 0 #constant here
    T5 = 0 #constant here
    T6 = 90 #constant here

    Forward_Kinematics.SetT1(T1)
    Forward_Kinematics.SetT2(T2)
    Forward_Kinematics.SetT3(T3)
    Forward_Kinematics.SetT4(T4)
    Forward_Kinematics.SetT5(T5)
    Forward_Kinematics.SetT6(T6)

    px = Forward_Kinematics.getPX()
    py = Forward_Kinematics.getPY()
    pz = Forward_Kinematics.getPZ()
    
    def oled_print(self, text="", dint=False, x=0,y=0,color=1):
        if(dint is True):
            self.display.text(str(text), x, y, color)
            self.display.show()
        else:
            self.display.text(text, x, y, color)
            self.display.show()
            
    def oled_cls(self):
        self.display.fill(0)
    #==========================================================================================================
    def Run(self, arr=0):
        for i in range(len(arr)):
            self.RB.setPosition(arr[i][0][0],arr[i][0][1],arr[i][0][2])
            self.RB.setOrientation(arr[i][1][0],arr[i][1][1],arr[i][1][2])
            self.RB.Start()
            self.oled_print("Theta1 =",False,0,1,2)
            self.oled_print(round(self.RB.getT1_Output()),True,65,1,1)
            
            self.oled_print("Theta2 =",False,0,10,1)
            self.oled_print(round(self.RB.getT2_Output()),True,65,10,1)
            
            self.oled_print("Theta3 =",False,0,20,1)
            self.oled_print(round(self.RB.getT3_Output()),True,65,20,1)
            
            self.oled_print("Theta4 =",False,0,30,1)
            self.oled_print(round(self.RB.getT4()),True,65,30,1)
            
            self.oled_print("Theta5 =",False,0,40,1)
            self.oled_print(round(self.RB.getT5()),True,65,40,1)
            
            self.oled_print("Theta6 =",False,0,50,1)
            self.oled_print(round(self.RB.getT6()),True,65,50,1)
            self.oled_cls()
#             print('\n') 
#             print(self.RB.getT2Servo())
#             print(self.RB.getT3Servo())        
    #==========================================================================================================        
    def Move(self, arr=0):
        self.RB.setPosition(arr[0][0],arr[0][1],arr[0][2])
        self.RB.setOrientation(arr[1][0],arr[1][1],arr[1][2])
        self.RB.Start()
        
        self.oled_print("Theta1 =",False,0,1,1)
        self.oled_print(round(self.RB.getT1_Output()),True,65,1,1)
        
        self.oled_print("Theta2 =",False,0,10,1)
        self.oled_print(round(self.RB.getT2_Output()),True,65,10,1)
        
        self.oled_print("Theta3 =",False,0,20,1)
        self.oled_print(round(self.RB.getT3_Output()),True,65,20,1)
        
        self.oled_print("Theta4 =",False,0,30,1)
        self.oled_print(round(self.RB.getT4()),True,65,30,1)
        
        self.oled_print("Theta5 =",False,0,40,1)
        self.oled_print(round(self.RB.getT5()),True,65,40,1)
        
        self.oled_print("Theta6 =",False,0,50,1)
        self.oled_print(round(self.RB.getT6()),True,65,50,1)

#         print(self.RB.getT2Servo())
#         print(self.RB.getT3Servo())
#         print('\n')
#         print("#NEW HOMOGENOUS TRANSFORMATION MATRIX")
#         print(self.RB.getH0_6())
#         print('\n')
                                    # User Interface Code Here
#==================================================================================================================
    home_screen_options = {
            1: 'Menu',
        }
   
    menu_options1 = {
        1: '1:Joint Motion',
        2: '2:IK Motion',
        3: '3:P2P Move',
        4: '4:Back',
        5: '5:Next',
        }
    menu_options2 = {
        1: '1:Joint Control',
        2: '2:XYZ Control',
        3: '3:Restart',
        4: '4:Help',
        5: '5:Back',
        }
    
    def joint_motion(self):
        self.oled_cls()
        #self.Move(([self.px,  self.py,  self.pz],[0,0,90]))
        pos = (([self.px,self.py, self.pz],[0,0,90]), 
              ([self.px,self.py,self.pz],[0,30,90]),
              ([self.px,self.py,self.pz],[0,0,60]))
        self.Run(pos)
        #option = str(input('Enter your choice: '))
        option = self.keyPad.onPress()
        sleep(0.3)
        if option == "4":
            self.HomeScreen()
        elif option =="5":
             self.joint_motion() #Repeat the process
    
    #Display Menu Screen 1
    def MenuScreen1(self):
        self.oled_cls()
        self.oled_print("Menu1",False,45,1,1)
        self.display.hline(0,10,128,1)
        shift_down = 3
        self.oled_print(self.menu_options1[1],False,0,10+shift_down,1)
        self.oled_print(self.menu_options1[2],False,0,20+shift_down,1)
        self.oled_print(self.menu_options1[3],False,0,30+shift_down,1)
        self.oled_print(self.menu_options1[4],False,0,40+shift_down,1)
        self.oled_print(self.menu_options1[5],False,0,50+shift_down,1)
        #Link back to home screen
        #option = str(input('Enter your choice: '))
        option = self.keyPad.onPress()
        sleep(0.3)
        if option == "4":
            self.HomeScreen()
        elif option == "5":
            self.MenuScreen2()
        elif option == "1":
            self.joint_motion()
            
    #Display Menu Screen 2
    def MenuScreen2(self):
        self.oled_cls()
        self.oled_print("Menu2",False,45,1,1)
        self.display.hline(0,10,128,1)
        shift_down = 3
        self.oled_print(self.menu_options2[1],False,0,10+shift_down,1)
        self.oled_print(self.menu_options2[2],False,0,20+shift_down,1)
        self.oled_print(self.menu_options2[3],False,0,30+shift_down,1)
        self.oled_print(self.menu_options2[4],False,0,40+shift_down,1)
        self.oled_print(self.menu_options2[5],False,0,50+shift_down,1)
        #Link back to home screen
        #option = str(input('Enter your choice: '))
        option = self.keyPad.onPress()
        sleep(0.3)
        if option == "5":
            self.MenuScreen1()
       
   #Display Home screen
    def HomeScreen(self):
        self.oled_cls()
        self.oled_print("Home: IROBOTICS",False,0,1,1)
        self.display.hline(0,10,128,1)
        for i in range(400):
            self.display.pixel(i%4+i,(12+i%40),1)
        self.display.hline(0,52,128,1)    
        self.oled_print(self.home_screen_options[1] + ": Press A",False,0,55,1)
        #Link back to menu screen
        #option = str(input('Enter your choice: '))
        option = self.keyPad.onPress()
        sleep(0.3)
        if option == "A":
            self.MenuScreen1()
        else:{
            self.HomeScreen()
            }  
        
    #Start Sequence
    def Begine(self): 
        self.HomeScreen() 
        

