#IMPORTANT - Before running this program, execute the following command in the terminal - sudo pigpiod

import pigpio
import time

pi = pigpio.pi()

#set GPIO Pins
TRIG = 23 
ECHO = 24
pi.set_mode(TRIG, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)


#Define user defined callback function to measure the timing of the rising edge and falling edge of the ECHO
# functionname(User GPIO, Edge type, )--------
#This function is called when a callback is triggered
#It receives three inputs the specified Pin, the event type (0 = change to low, 1change to high),
# and the timing in micro-second. 
def ownrise(gpio, level, tick):
    global low
    low = tick
def ownfall(gpio, level, tick):
    global high
    high = tick

#-----------------------------------------------------------------------------------


#Start the acquisition process by sending trigger pulse and measure the timings of ECHO-----
#Use this pin to generate a 10 mu-s trigger signal
pi.gpio_trigger(TRIG,10,1)   #(channel number, trigger pulse width in mu-s, channel NOT level after trigger)

#Measure the rising and falling edge of the ECHO 
#See https://abyz.me.uk/rpi/pigpio/python.html#callback
#Arguments (pi.callback(PIN number, Edge type, user defined function))
#Execution: If the event is detectged on the spcified pin then the user defined function is called.
pi.callback(ECHO, pigpio.FALLING_EDGE, ownrise)
pi.callback(ECHO, pigpio.RISING_EDGE, ownfall)    


#Wait with the code progression until the falling edge of the ECHO is detected (5.0 is the timeout time) 
if pi.wait_for_edge(ECHO,pigpio.FALLING_EDGE,5.0):
    tof = low - high
    distance = tof * 17150 * 1e-5
    print(f"Time of flight {tof}")
    print(f"There is an object at a distance of {distance} mm")
else:
    print('Timeout')


#Stop pigpio
pi.stop()
