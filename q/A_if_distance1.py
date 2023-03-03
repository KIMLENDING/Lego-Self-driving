from ex import*
def A_if_distance():
    """거리에 따른 속도 변화"""
   print('A함수 실행')

    center_distance = center_ultrasonic_sensor.distance()
    if 2551 > center_distance >= 1000 :
        current_speed = 800
        return current_speed
    elif 1000 > center_distance >= 700 : 
        current_speed = 700
        return current_speed
    elif 700 > center_distance >= 400 : 
        current_speed = 500
        return current_speed
    elif 400 > center_distance >= 100 : 
        current_speed = 300
        return current_speed
    elif 100 > center_distance >= 0 : 
        current_speed = 0
        return current_speed
    elif current_speed == 0: 
        current_speed = 0
        return current_speed
    else:
        current_speed = 0
        print("err",center_distance)
        return current_speed
