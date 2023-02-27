#Distance measurement using HC-SR04 using software triggered pulses.

import RPi.GPIO as GPIO
import time
import numpy as np

#Preparing the RPi------------------------------------------- 
#GPIO Mode (BOARD / BCM)

#------------------------------------------------------------



l=[]
c=0
while c<1000:
    
    GPIO.setmode(GPIO.BCM)
 
    #set GPIO Pins
    TRIG = 23
    ECHO = 24
     
    #set GPIO direction (IN / OUT)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)


    #Create single trigger pulse with 10 ms on the TRIG pin
    #Send trigger signal
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(10E-6)
    GPIO.output(TRIG, GPIO.LOW)
    # save StartTime
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = (StopTime - StartTime)*1E6
    distance = TimeElapsed * 17150 * 1e-5
    c+=1
    l.append(distance)
    print(c, l)
    GPIO.cleanup()
    
lst = np.array(l)
print(f",avg {np.mean(lst)}")
print(f",std {np.std(lst)}")



GPIO.cleanup()



