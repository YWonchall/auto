# Car's movement control (forward, back, left, right, brake)
# motor control

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class CarMove(object):
    def __init__(self):
        self.GPIO_motors_forward = [13,26,12,20]
        self.GPIO_motors_backward = [6,19,16,21]

        for gpio in self.GPIO_motors_forward + self.GPIO_motors_backward:
            GPIO.setup(gpio, GPIO.OUT)
        
        self.PWM_motors_forward = [GPIO.PWM(gpio, 500) for gpio in self.GPIO_motors_forward]
        self.PWM_motors_backward = [GPIO.PWM(gpio, 500) for gpio in self.GPIO_motors_backward]
        self.PWM_motors = self.PWM_motors_forward  + self.PWM_motors_backward
        
        for motor in self.PWM_motors:
            motor.start(0)


    def forward(self, speed):
        for motor in self.GPIO_motors_backward:
            GPIO.output(motor, GPIO.LOW)
        for motor in self.PWM_motors_forward:
            motor.ChangeDutyCycle(speed)  # set the duty circle (range: 0~100)
    def backward(self, speed):
        for motor in self.GPIO_motors_forward:
            GPIO.output(motor, GPIO.LOW)
        for motor in self.PWM_motors_backward:
            motor.ChangeDutyCycle(speed)  # set the duty circle (range: 0~100)

    def MotorStop(self, motor_type):
        if motor_type == 'forward':
            for motor in self.PWM_motors_forward:
                motor.ChangeDutyCycle(0)
        elif motor_type == 'backward':
            for motor in self.PWM_motors_backward:
                motor.ChangeDutyCycle(0)
        else:
            for motor in self.PWM_motors:
                motor.ChangeDutyCycle(0)
 
 


if __name__ == '__main__':
    try:
        car = CarMove()
        while (True):
            car.forward(20)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        car.MotorStop()
        GPIO.cleanup()

