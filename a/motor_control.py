from a.im import*

# 핸들을 angle만큼 회전하는 함수
def rotate_handle(angle):
    """회전 각도"""
    motor_B.run_angle(20, angle)
    motor_B.stop()
    brick.sound.beep()
# 핸들을 power의 속으로 회전
def rotate_handle1(power):
    """힘의 크기"""
    motor_B.run(power)
    wait(500)
    motor_B.stop()
    brick.sound.beep()

# 핸들을 점진적으로 회전하는 함수
def rotate_handle_smoothly(target_speed=100, acceleration=500, max_speed=1000, run_time=2000):
    """초기속도, 가속도, 최고속도, 진행시간"""
    # 가감속 설정
    motor_B.run_target(target_speed, acceleration=acceleration)
    motor_B.run_target(max_speed, wait=False)
    wait(run_time)
    motor_B.run_target(0, acceleration=acceleration)
    motor_B.stop()
    brick.sound.beep()
