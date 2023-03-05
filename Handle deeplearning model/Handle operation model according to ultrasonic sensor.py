import tensorflow as tf

# 센서 학습 데이터 불러오기
# 조향 학습 데이터 불러오기
def load_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    data = []
    for line in lines:
        values = line.strip().split(' ')
        data.append(list(map(int, values[:2])))  # value1, value3 값만 저장

    return data

def load_angles(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    angles = []
    for line in lines:
        values = line.strip().split(' ')
        angle = int(values[-1])
        angles.append(angle)
        #angle_values = list(map(int, values[:-1]))
        #angle_values.append(angle)
        #angles.append(angle_values)

    return angles

    
# 학습 데이터 정규화
def normalize_data(data):
    max_val = max(max(row) for row in data)
    normalized_data = []
    for values in data:
        normalized_values = [value / 2550 for value in values]
        normalized_data.append(normalized_values)
    
    return normalized_data





# 핸들 조향 각도 예측 모델 구현
def create_steering_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),        
        tf.keras.layers.Dense(256, activation='relu'),        
        tf.keras.layers.Dense(128, activation='relu'),      
        tf.keras.layers.Dense(64, activation='relu'),       
        tf.keras.layers.Dense(32, activation='relu'),       
        tf.keras.layers.Dense(1, activation='linear')
    ])#softmax,linear,sigmoid,tanh
       
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer, loss='mean_squared_error')
    return model

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

# 모델 학습
data = load_data('angle.txt')
normalized_data = normalize_data(data)
angles = load_angles('angle.txt')

model = create_steering_model()
model.fit(normalized_data, angles, epochs=200, batch_size=64)

# 모델 평가
test_data = load_data('test.txt')
normalized_test_data = normalize_data(test_data)
test_angles = load_angles('test.txt')

loss = model.evaluate(normalized_test_data, test_angles)
print('Test Loss: {:.3f}'.format(loss))
# 모델 저장
tf.keras.models.save_model(model, 'my_model')

# 핸들 조향 각도 예측
sensor_data = [[0, 0], [2400, 2000], [2400, 2500]]
for sensor_values in sensor_data:
    steering_angle = predict_steering_angle(model, sensor_values)
    print('Sensor Values: {}, Steering Angle: {}'.format(sensor_values, steering_angle))