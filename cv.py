import numpy as np
import dlib
import cv2 as cv
import tensorflow as tf
import keras
from tensorflow.keras.models import load_model
import string

cap = cv.VideoCapture(0)

#GPU settings
physical_devices = tf.config.experimental.list_physical_devices('GPU')
print("GPUS: ", len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0], True)

model = load_model('models/model_20.h5')

#Make dictionary to map predictions to letter
chars = dict(enumerate(list(string.ascii_uppercase)))

while True:
    _, frame = cap.read()

    frame = cv.flip(frame, 1)
    cv.rectangle(frame, (50, 50), (300, 300), (0, 255, 0), 3)
    hand = cv.cvtColor(frame[50:300, 50:300], cv.COLOR_BGR2GRAY)
    
    #Process image for model
    img = cv.resize(hand, (28, 28))
    img = np.expand_dims(img, axis=2)
    img = np.expand_dims(img, axis=0)

    #Make prediction and fix numbering issue
    pred = model.predict_classes(img)[0]
    if pred >= 9:
        pred += 1

    print('Prediction: {}'.format(chars[pred]))
    output = cv.putText(hand, chars[pred], (220, 240),
     cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv.imshow('Output', frame)
    cv.imshow('Hand', output)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break