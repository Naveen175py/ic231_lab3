import RPi.GPIO as GPIO
import time



def distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

ENTER_THRESHOLD = 0.8 # meters
EXIT_THRESHOLD = 1.2 # meters

people_inside = 0

while True:
    
    GPIO.setmode(GPIO.BOARD)

    TRIG = 23
    ECHO = 24

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    dist = distance()
    if dist < ENTER_THRESHOLD:
        people_inside += 1
        print("Person entered. People inside:", people_inside)
        time.sleep(1)
    elif dist > EXIT_THRESHOLD:
        people_inside -= 1
        if people_inside < 0:
            people_inside = 0
        print("Person exited. People inside:", people_inside)
        
    GPIO.cleanup()

              
   