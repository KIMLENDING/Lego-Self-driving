#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from ex import*
from drive1 import*

ev3.speaker.beep()

def ex(motor_A, motor_B, center_distance,right_distance,left_distance):
    while True:
        center_distance = center_ultrasonic_sensor.distance()
        right_distance = right_ultrasonic_sensor.distance()
        left_distance = left_ultrasonic_sensor.distance()   
        print(left_distance,center_distance,right_distance)
        wait(1000)
    
    


while True:
    # 버튼 누르기 
    pressed_buttons = ev3.buttons.pressed()
    current_position = motor_B.angle()
    # 1. UP 핸들 오른쪽으로 -7도 회전
    if Button.UP in pressed_buttons:
        motor_B.run_target(1000,(current_position-7))
    # 2. DOWN 핸들 왼쪽으로 7도 회전
    elif Button.DOWN in pressed_buttons:
        motor_B.run_target(1000,(current_position+7))   
    # 3. CENTER 전진
    elif Button.CENTER in pressed_buttons:
    # 현재 위치를 0으로 설정한니다. 1,2를 활용하여 바퀴를 정렬 시켜 두어야함
        current_position = motor_B.angle()#조정한 각도 저장
        drive(motor_A, motor_B,center_distance,right_distance,left_distance)
        motor_B.run_target(1000,current_position)# 정렬
        # ex(motor_A, motor_B, center_distance, right_distance, left_distance)
