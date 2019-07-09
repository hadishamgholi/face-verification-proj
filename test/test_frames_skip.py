import cv2
import os

media = '/home/hadi/Desktop/test/test.mp4'
folder = '/home/hadi/Desktop/test/frames'

cap = cv2.VideoCapture(media)
counter = 0
steps = 5
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if counter % steps == 0:
        name = '{}.jpeg'.format(counter // steps)
        cv2.imwrite(os.path.join(folder, name), frame)
    counter += 1

cap.release()