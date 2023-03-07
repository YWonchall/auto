# Car's movement control (forward, back, left, right, brake)
# motor control
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class CarMove(object):
    def __init__(self):
        self.GPIO_motors_forward = [13,26,12,20]
        self.GPIO_motors_backward = [6,19,16,21]
        self.GPIO_servo = 23 #GPIO口
        
        for gpio in self.GPIO_motors_forward + self.GPIO_motors_backward:
            GPIO.setup(gpio, GPIO.OUT)
        GPIO.setup(self.GPIO_servo, GPIO.OUT)

        self.PWM_motors_forward = [GPIO.PWM(gpio, 500) for gpio in self.GPIO_motors_forward]
        self.PWM_motors_backward = [GPIO.PWM(gpio, 500) for gpio in self.GPIO_motors_backward]
        self.PWM_motors = self.PWM_motors_forward  + self.PWM_motors_backward
        self.PWM_servo = GPIO.PWM(self.GPIO_servo, 50)

        for motor in self.PWM_motors:
            motor.start(0)
        self.PWM_servo.start(7)
        time.sleep(0.1)
        self.PWM_servo.ChangeDutyCycle(0)

    def motor_rota(self, direction, speed=20):
        self.motor_stop()
        if direction == 'forward':
            for motor in self.PWM_motors_forward:
                motor.ChangeDutyCycle(speed)  # set the duty circle (range: 0~100)
        else:
            for motor in self.PWM_motors_backward:
                motor.ChangeDutyCycle(speed)  # set the duty circle (range: 0~100)
    
    def motor_stop(self):
        for motor in self.PWM_motors:
            motor.ChangeDutyCycle(0)
  
  
    def servo_rota(self, ratio=7):
        self.PWM_servo.ChangeDutyCycle(ratio)
        time.sleep(0.1)
        self.PWM_servo.ChangeDutyCycle(0)
        
        
    def forward(self,speed):
        self.servo_rota(7)
        self.motor_rota('forward',speed=speed)
    
    def backward(self,speed):
        self.servo_rota(7)
        self.motor_rota('backward',speed=speed)
    
    def turn(self, direction, speed=20):
        if direction == 'left-forward':
            self.servo_rota(5.5)
            self.motor_rota('forward',speed=speed)
        
        elif direction == 'right-forward':
            self.servo_rota(8.5)
            self.motor_rota('forward',speed=speed)
        
        elif direction == 'left-backward':
            self.servo_rota(5.5)
            self.motor_rota('backward',speed=speed)
        
        elif direction == 'right-backward':
            self.servo_rota(8.5)
            self.motor_rota('backward',speed=speed)
        


if __name__ == '__main__':
    try:
        car = CarMove()
        while (True):
            car.forward(20)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        car.motor_rota()
        GPIO.cleanup()

