import os
import cv2

base_dir = '../datasets/imagenet/train'

files = os.listdir(base_dir)
files.sort()
l = []
for f in files:
    if f.endswith('.jpg'):
        img = cv2.imread(os.path.join(base_dir, f), cv2.IMREAD_UNCHANGED)
