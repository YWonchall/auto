import RPi.GPIO as GPIO
import time
 
servoPIN = 23 #GPIO口
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
print("servoPIN",servoPIN)
p = GPIO.PWM(servoPIN, 50) # GPIO 4 for PWM with 50Hz
p.start(7) # Initialization
try:
  while True:
    p.ChangeDutyCycle(5.5)
    time.sleep(0.2)
    p.ChangeDutyCycle(0)
    time.sleep(1)
    p.ChangeDutyCycle(7)
    time.sleep(0.2)
    p.ChangeDutyCycle(0)
    time.sleep(1)
    p.ChangeDutyCycle(8.5)
    time.sleep(0.2)
    p.ChangeDutyCycle(0)
    time.sleep(1)
    p.ChangeDutyCycle(7)
    time.sleep(0.2)
    p.ChangeDutyCycle(0)
    time.sleep(1)
except KeyboardInterrupt:
  p.ChangeDutyCycle(7)
  time.sleep(1)
  p.stop()
  GPIO.cleanup()