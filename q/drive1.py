from ex import*
from A_if_distance1 import*
from B_if_distance1 import*
def drive(motor_A, motor_B,center_distance,right_distance,left_distance):
    """초기속도,가속도,가속도 배율"""
    current_position = motor_B.angle()
    # 현재 위치를 0으로 설정한니다.
    motor_B.reset_angle(0)
    #current_speed = initial_speed + i * acceleration
    motor_A.run(100)
    wait(500)
    while True:
        #속도가 구간별로 줄어드는지 확인하기
        motor_A.run(A_if_distance())
        if(A_if_distance()==0):
            m_stop(center_distance)
        center_distance, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
        print("1",left_distance,center_distance,right_distance)
        m_stop(center_distance)# 전방 센서가 10cm 이하 라면 멈춤
        C_if_distance(motor_A, motor_B)
        B_if_distance(motor_A, motor_B)
        wait(10)


       

        