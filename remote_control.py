from move import CarMove
import RPi.GPIO as GPIO
import sys
import termios
import time
import select

car = CarMove()

def clear_input_buffer():
    while select.select([sys.stdin], [], [], 0.0)[0]:
        sys.stdin.read(1)

# 将终端设备设置为非阻塞模式
def set_non_blocking(fd):
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 0
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    return old

# 恢复终端设备的阻塞模式
def set_blocking(fd, old):
    termios.tcsetattr(fd, termios.TCSAFLUSH, old)

try:

    fd = sys.stdin.fileno()
    # 将终端设备设置为非阻塞模式
    old = set_non_blocking(fd)
    # 循环读取键盘输入并控制电机
    crt_dir = 'w'
    while True:
        # 等待用户输入
        r, w, e = select.select([fd], [], [], 0.1)
        clear_input_buffer()
        # 如果有输入，则读取并处理用户的操作
        if r:
            key = sys.stdin.read(1)
            print(key)
            if key == 'w':
                # pass
                crt_dir = 'w'
                car.forward(20)
            elif key == 's':
                # pass
                crt_dir = 's'
                car.backward(20)
            elif key == 'a':
                # pass
                if crt_dir == 'w':
                    car.turn(direction='left-forward')
                elif crt_dir == 's':
                    car.turn(direction='left-backward')
                else:
                    pass
            elif key == 'd':
                # pass
                if crt_dir == 'w':
                    car.turn(direction='right-forward')
                elif crt_dir == 's':
                    car.turn(direction='right-backward')
                else:
                    pass
            elif key == 'e':
                print("stop")
                car.MotorStop('all')
            if key == 'q':
                break       
        else:
            car.motor_stop()
        
        time.sleep(0.1)
        

finally:
    # 恢复终端设备的阻塞模式
    set_blocking(fd, old)
    # 停止电机
    car.motor_stop()
    time.sleep(0.3)
    GPIO.cleanup()
