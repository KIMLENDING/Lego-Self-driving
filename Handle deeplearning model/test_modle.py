import tensorflow as tf
# 학습 데이터 정규화
def normalize_data(data):
    max_val = max(max(row) for row in data)
    normalized_data = []
    for values in data:
        normalized_values = [value / 2550 for value in values]
        normalized_data.append(normalized_values)
    
    return normalized_data
# 핸들 조향 각도를 최대 ±70도로 제한하는 함수
def limit_steering_angle(angle):
    if angle < -70:
        return -70
    elif angle > 70:
        return 70
    else:
        return int(angle)
    
# 예측 결과를 핸들 조향 각도로 변환하는 함수
def predict_steering_angle(model, sensor_values):
    normalized_values = normalize_data([sensor_values])[0]
    steering_angle = model.predict([normalized_values])[0][0]
    steering_angle = limit_steering_angle(steering_angle)
    return steering_angle
# 모델 사용

# 모델 불러오기
my_model = tf.keras.models.load_model('my_model')

# 핸들 조향 각도 예측
sensor_data = [[0, 0], [2400, 2000], [2400, 2500]]
for sensor_values in sensor_data:
    steering_angle = predict_steering_angle(my_model, sensor_values)
    print('Sensor Values: {}, Steering Angle: {}'.format(sensor_values, steering_angle))
