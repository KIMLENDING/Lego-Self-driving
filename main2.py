#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks import ev3brick as brick

# Create EV3 Brick object
ev3 = EV3Brick()

# Create motor connected to Port A for the ultrasonic sensor and set it to stop when the program ends
ultrasonic_motor = Motor(Port.A, Direction.CLOCKWISE)
"""ultrasonic_motor.stop()"""

# Create UltrasonicSensor object connected to Port S1
ultrasonic_sensor = UltrasonicSensor(Port.S1)

# Create motor connected to Port B for the handle
motor_B= Motor(Port.B)

# Create motor connected to Port A for the main drive motor
motor_A = Motor(Port.A)

# Beep the EV3 Brick speaker to indicate the start of the program
ev3.speaker.beep()

# Play a sound.
brick.sound.beep()

# Function to rotate the handle motor by a given angle
def rotate_handle(angle):
    motor_B.run_angle(20, angle)
    motor_B.stop()
    brick.sound.beep()

# Function to move forward until an obstacle is detected by the ultrasonic sensor
def move_forward_until_obstacle():
    # Initial and target speeds for the main drive motor
    initial_speed = 100
    target_speed = 400

    # Number of steps to gradually increase the speed
    num_steps = 10

    # Calculate the speed increase per step
    speed_increase = (target_speed - initial_speed) / num_steps

    # Gradually increase the speed and check for obstacles
    for i in range(num_steps):
        current_speed = initial_speed + i * speed_increase
        motor_A.run(current_speed)
        distance = ultrasonic_sensor.distance()
        if distance < 100:
            ultrasonic_motor.stop()
            break
        wait(1500)

    # Stop the main drive motor and beep the EV3 Brick speaker
    motor_A.stop()
    brick.sound.beep()

# Main loop of the program
while True:
    # Check for button presses
    pressed_buttons = ev3.buttons.pressed()

    # Rotate handle to the right by 20 degrees when UP button is pressed
    if Button.UP in pressed_buttons:
        rotate_handle(20)

    # Rotate handle to the left by 20 degrees when DOWN button is pressed
    elif Button.DOWN in pressed_buttons:
        rotate_handle(-20)

    # Move forward until an obstacle is detected when CENTER button is pressed
    elif Button.CENTER in pressed_buttons:
        move_forward_until_obstacle()

    # Wait for 0.05 seconds before checking for button presses again
    wait(50)
