
#----------------동작함수-----------------#
from motor_control import*
from move_forward_until_obstacle1 import*
#----------------------------------------#
ev3.speaker.beep()
while True:
    # 버튼 누르기 
    pressed_buttons = ev3.buttons.pressed()
    # 1. UP 핸들 오른쪽으로 20도 회전
    if Button.UP in pressed_buttons:
        rotate_handle1(20)
    # 2. DOWN 핸들 왼쪽으로 -20도 회전
    elif Button.DOWN in pressed_buttons:
        rotate_handle1(-20)
    # 3. CENTER 전진
    elif Button.CENTER in pressed_buttons:
        move_forward_until_obstacle(500, 30, 50)  
   