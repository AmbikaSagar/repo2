# import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classifier = Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation="relu "))
classifier.add(MaxPooling2D(2, 2))
classifier.add(Flatten())
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=1, activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_cross_entropy', metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('C:/Users/Ambika/Downloads/download',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')
test_set = test_datagen.flow_from_directory('C:/Users/Ambika/Downloads/OIP',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')
model = classifier.fit_generator(training_set,
                                 steps_per_epoch=8000,
                                 epochs=1,
                                 validation_data=test_set,
                                 validation_steps=2000)
classifier.save('model.h5')
print("saved model to disk")

import numpy as np
from keras.preprocessing import image


