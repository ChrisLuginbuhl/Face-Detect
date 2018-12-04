"""
Modification by Chris Luginbuhl
Based on Jeevsh Narang's code
https://github.com/JeeveshN/Face-Detect
Modified to output to files rather than screen
Modify Line 17 for your path
"""


import cv2
import sys
import os
from PIL import Image
from matplotlib import pyplot as plt

#You gotta choose your own path...
path = "/Users/chrisluginbuhl/machine_learning_local/wikiart/Early_Renaissance/"
subfolder = "detected/"
dirs = os.listdir( path )
final_size = 64;
os.makedirs(path + subfolder, exist_ok=True)

CASCADE="Face_cascade.xml"
FACE_CASCADE=cv2.CascadeClassifier(CASCADE)

def detect_faces(image_path):
    im = cv2.imread(path + item)
    f, e = os.path.splitext(path + subfolder + item)
    image_grey=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#if faces are not detected, reduce scaleFactor
    faces = FACE_CASCADE.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)

    i = 0
    for x,y,w,h in faces:
        sub_img=im[y-10:y+h+10,x-10:x+w+10]
        cv2.imwrite(f + '_detected_' + str(i) + '.jpg', sub_img)
        i += 1

for item in dirs:
        if item == '.DS_Store':
            continue
        if os.path.isfile(path + item):
            detect_faces(path + item)
