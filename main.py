#!python "c:/Users/gotsl/Desktop/새 폴더 (2)/a/main2.py"
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks import ev3brick as brick


#----------------동작함수-----------------#
#from rotate_handle1 import*
#from move_forward_until_obstacle1 import*


#----------------------------------------#

# EV3 브릭 생성
ev3 = EV3Brick()

# 포트 A에 연결된 모터 생성 초음파 센서에 의한 정지
ultrasonic_motor = Motor(Port.A, Direction.CLOCKWISE)

# 포트 1에 연결된 초음파 센서 생성
ultrasonic_sensor = UltrasonicSensor(Port.S1)

# Write your program here.
ev3.speaker.beep()


# Play a sound.
brick.sound.beep()
# 핸들 모터
motor_B= Motor(Port.B)


while True:
    # 버튼 누르기 
    pressed_buttons = ev3.buttons.pressed()
    # 1. UP 핸들 오른쪽으로 20도 회전
    if Button.UP in pressed_buttons:
        motor_B.run(20)
        wait(500)
        motor_B.stop()
        brick.sound.beep()
    # 2. DOWN 핸들 왼쪽으로 20도 회전
    elif Button.DOWN in pressed_buttons:
        motor_B.run(-20)
        wait(500)
        motor_B.stop()
        brick.sound.beep()
    # 3. CENTER 전진
    elif Button.CENTER in pressed_buttons:
        # 주 동력 모터
        motorA = Motor(Port.A)
        #초기 속도
        initial_speed = 100
        #목표 속도
        target_speed = 400

        # 움직일 시간
        num_steps = 10

        # 초당 증가 속도
        speed_increase = (target_speed - initial_speed) / num_steps

        # Use a loop to gradually increase the speed.
        for i in range(num_steps):
        # 현재 속도 계산
            current_speed = initial_speed + i * speed_increase
        # 현재 속도 출력
            motorA.run(current_speed)
        # 앞에 장애물이 초음파 감지에 100이하 거리에 있다면 정지
            distance = ultrasonic_sensor.distance()  # 초음파 객체
            if distance < 100:
                ultrasonic_motor.stop()
                break
        # 1.5초 뒤에 속도 증가
            wait(1500)

        # Stop the motor.
        motorA.stop()
        brick.sound.beep() 
    # 0.5초뒤에 1,2,3 중 동작 입력 가능 
    wait(50)
    







