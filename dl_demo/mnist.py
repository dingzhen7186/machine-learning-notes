from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D
from keras.layers import Dense, Flatten, Dropout
from keras.utils import to_categorical
from keras.datasets import mnist
import matplotlib.pyplot as plt

# 加载数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)

# 数据预处理
img_x, img_y = 28, 28
X_train = X_train.reshape(X_train.shape[0], img_x, img_y, 1)
X_test = X_test.reshape(X_test.shape[0], img_x, img_y, 1)

# 数据标准化
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# 将标记值(y_train, y_test)转换为One-Hot Encode的形式
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
print(y_train.shape)

# 定义模型结构
model = Sequential()
model.add(Conv2D(32, kernel_size=(5,5), activation='relu', input_shape=(img_x, img_y, 1)))
model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
model.add(Dropout(0.5))

model.add(Conv2D(64, kernel_size=(5,5), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
model.add(Dropout(0.5))

model.add(Flatten())

model.add(Dense(1000, activation='relu'))
model.add(Dense(10, activation='softmax'))

# 编译模型
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型
model.fit(X_train, y_train, batch_size=128, epochs=10)

# 评估模型
score1 = model.evaluate(X_train, y_train)
score2 = model.evaluate(X_test, y_test)
print('训练集准确度acc = ', score1[1])
print('测试集准确度acc = ', score2[1])