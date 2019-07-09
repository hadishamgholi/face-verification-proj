from mtcnn.mtcnn import MTCNN
import cv2

scale_factor = .709
detector = MTCNN(scale_factor=scale_factor)

images = ['/home/hadi/Desktop/4.jpg', '/home/hadi/Desktop/1.jpg',
'/home/hadi/Desktop/2.jpg', '/home/hadi/Desktop/5.jpg']

for i in images:
    img = cv2.imread(i)#[:,:,::-1]
    res = detector.detect_faces(img)
    print(i, '\n', res, '\n\n')
    title = 'not detected' if len(res) == 0 else res[0]['confidence']
    cv2.imshow(str(title), img)


cv2.waitKey(0)
cv2.destroyAllWindows()