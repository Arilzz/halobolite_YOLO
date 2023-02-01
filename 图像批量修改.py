import cv2
import os


path = './data/images/'

for i in os.listdir(path):
    img = cv2.imread(os.path.join(path, i))
    dst = cv2.resize(img, None, fx=0.25, fy=0.25)
    cv2.imwrite(os.path.join(path, i), dst)
