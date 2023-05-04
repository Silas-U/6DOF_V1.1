from T100_SETUP import T100_SETUP as _6DOF_Robot
from time import sleep
from machine import Pin

#Initialise the Robot
Robot = _6DOF_Robot()

#Begine loop
while True:
    Robot.Begine()
   
        
