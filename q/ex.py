#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
motor_A= Motor(Port.A)
motor_B= Motor(Port.B)

center_ultrasonic_sensor = UltrasonicSensor(Port.S1)
right_ultrasonic_sensor = UltrasonicSensor(Port.S2)
left_ultrasonic_sensor = UltrasonicSensor(Port.S3)

center_distance = center_ultrasonic_sensor.distance()
right_distance = right_ultrasonic_sensor.distance()
left_distance = left_ultrasonic_sensor.distance()

def m_stop(center_distance):
    if center_distance<100:
        motor_A.stop()
        break
    
def crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor):
    center_distance = center_ultrasonic_sensor.distance()
    right_distance = right_ultrasonic_sensor.distance()
    left_distance = left_ultrasonic_sensor.distance()
    return center_distance,right_distance,left_distance