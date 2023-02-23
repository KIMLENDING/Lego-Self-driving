from a.im import*
"""
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

#모터의 포트, 최대 속도, 가속도
def gradual_start(motor_port, max_speed, acceleration):
    ev3 = EV3Brick()
    motor = Motor(motor_port)
    motor.reset_angle(0)

    start_speed = max_speed // 10

    for speed in range(start_speed, max_speed, acceleration):
        motor.run(speed)
        ev3.wait(10)

    motor.run(max_speed)
"""


def move_forward_until_obstacle(target_speed, acceleration, max_distance):
    """목표 속도, 가속도, 장애물 감지 거리"""
    # 초기속도 = 최고 속도 / 10   아님 따로 초기 속도 줘 도 됨
    initial_speed = target_speed // 10

    # 최고 속도 까지 몇 단계로 올라 갈지 단계 결정 wait이 1초니까 몇초 움직일지 묻는거야 
    num_steps = (target_speed - initial_speed) // acceleration

    # 점진적으로 속도 올리면서 장애물 있으면 멈춤
    for i in range(num_steps):
        current_speed = initial_speed + i * acceleration
        motor_A.run(current_speed)
        # 초음파 센서로 거리 측정
        distance = ultrasonic_sensor.distance()
        if distance < max_distance:
            motor_B.stop()
            break
        wait(1000) # 이거 바꾸지 마세요
    """
    현재 속도는 초기 속도 + 초당 속도 증가랑
    모터A에 현재 속도 반영
    초음파 센서로 측정한 거리가 설정한 거리보다 작다면 
    주 동력 모터B를 정지시킨다. 
    """
    # 장애물 없이 for문 끝나면 멈추기
    motor_A.stop()
    ev3 = EV3Brick()
    ev3.sound.beep()


def gradual_start(max_speed, acceleration, start_speed=None):
    """최고속도, 가속도, 초기속도"""
    motor_A.reset_angle(0)

    if start_speed is None:
        start_speed = max_speed // 10

    for speed in range(start_speed, max_speed, acceleration):
        motor_A.run(speed)
        ev3.wait(10) # 다른 작업 수행 가능

    motor_A.run(max_speed)