import RPi.GPIO as GPIO
import time



def open_(port):
    print "Open door in port ",port
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(port, GPIO.LOW)
    
def warning_(port):
    print "Warning bell or led in port ",port
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(port, GPIO.LOW)

    