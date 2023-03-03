from ex import*
from drive1 import*
def B_if_distance(motor_A, motor_B):
    """전방 장애물 회피"""
    print('B함수 실행')

    center_distance, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
    diff_distance = left_distance - right_distance
    #정면 50~40cm 앞에 장애물이 있다 판단 
    if 500 > center_distance > 400:
        
        if left_distance > right_distance and left_distance > 600: 
            motor_B.run_target(1000,-55) # 각도 수정 필요
            count=0
            while True:
                center_distance, right_distance, left_distance1 = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor) 
                count = count+1
                wait(100)#0.1초 뒤에 왼쪽 2번 센서 측정 
                left_distance2 = left_ultrasonic_sensor.distance()
                print(left_distance1,left_distance2,center_distance,right_distance)
                if left_distance2 > left_distance1 and center_distance > 400:
                    motor_B.stop()
                    break
                elif center_distance < 100:
                    motor_A.stop()
                
            current_position = motor_B.angle()
            motor_B.run_target(1000,-(current_position*1.5))
            
            wait(100*count*0.4)
            motor_B.run_target(1000,0)

        elif left_distance < right_distance and right_distance > 600: 
            motor_B.run_target(1000,55) 
            count=0
            while True:
                center_distance, right_distance1, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
                
                count = count+1
                wait(100)
                right_distance2 = right_ultrasonic_sensor.distance()
                print(left_distance,center_distance,right_distance1,right_distance2)
                if right_distance2 > right_distance1 and center_distance > 400::
                    motor_B.stop()
                    break
                elif center_distance < 100:
                    motor_A.stop()

            current_position = motor_B.angle()
            motor_B.run_target(1000,-(current_position*1.5)) 
            motor_B.stop()       
            wait(100*count*0.4)
            motor_B.run_target(1000,0)
        
        elif (right_distance == left_distance or (left_distance==2550 and right_distance==2550)) and right_distance > 600:
            motor_B.run_target(1000,55) 
            count=0
            while True:
                center_distance, right_distance1, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
                
                count = count+1
                wait(100)
                right_distance2 = right_ultrasonic_sensor.distance()
                print(left_distance,center_distance,right_distance1,right_distance2)
                if right_distance2 > right_distance1 and center_distance > 400::
                    motor_B.stop()
                    break
                elif center_distance < 100:
                    motor_A.stop()

            current_position = motor_B.angle()
            motor_B.run_target(1000,-(current_position*1.5)) 
            motor_B.stop()       
            wait(100*count*0.4)
            motor_B.run_target(1000,0)
        elif right_distance < 500 and left_distance < 500:
            motor_A.stop()
            while True:
                center_distance1, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
                if center_distance1 > center_distance:
                    motor_A.run(100)
                    break
        elif center_distance < 300:
            motor_A.stop()
    elif center_distance < 200:
            motor_A.stop()





def C_if_distance(motor_A, motor_B, speed):
    """얼라이먼트"""
    print('C함수 실행')
    
    center_distance, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
    # 좌우 거리차
    diff_distance = left_distance - right_distance
    
    if diff_distance == 0:
        motor_B.run_target(1000,0)
    # 왼쪽이 더 가까우면 오른쪽으로 이동
    elif 70 < diff_distance < 170:
        motor_B.run_target(1000,30)
        while True:
            center_distance, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
            diff_distance = left_distance - right_distance
            if(diff_distance<=0):
                break
            wait(10)
        motor_B.run_target(1000,0)
        
    # 오른쪽이 더 가까우면 왼쪽으로 이동
    elif -170 < diff_distance < -70:
        motor_B.run_target(1000,-30)
        while True:
            center_distance, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
            diff_distance = left_distance - right_distance
            if(diff_distance<=0):
                break
            wait(10)
        motor_B.run_target(1000,0)
        
    # 왼쪽이 더 가까우면 오른쪽으로 이동
    elif diff_distance > 0:
        motor_B.run_target(1000,50)
        while True:
            center_distance, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
            diff_distance = left_distance - right_distance
            if(diff_distance<=0):
                break
            wait(10)
        motor_B.run_target(1000,0)
    # 오른쪽이 더 가까우면 왼쪽으로 이동
    elif diff_distance < 0:
        motor_B.run_target(1000,-50)
        while True:
            center_distance, right_distance, left_distance = crl_sensor(center_ultrasonic_sensor, right_ultrasonic_sensor, left_ultrasonic_sensor)
            diff_distance = left_distance - right_distance
            if(diff_distance<=0):
                break
            wait(10)
        motor_B.run_target(1000,0)