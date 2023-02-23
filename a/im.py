#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks import ev3brick as brick
# EV3 브릭 생성
ev3 = EV3Brick()
# 포트 1에 연결된 초음파 센서 생성
ultrasonic_sensor = UltrasonicSensor(Port.S1)
# 주 동력
motor_A = Motor(Port.A) 
# 핸들
motor_B = Motor(Port.B) 