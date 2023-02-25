#锐化
import os
import cv2

base_dir = '../datasets/AliTampered/train/tampered/'

kernel_4 = np.array([[0, -1, 0], [-1, 4, -1],[0,-1, 0]], dtype = int)
kernel_8 = np.array([[-1, -1, -1], [-1, 8, -1],[-1,-1, -1]], dtype = int)

files = os.listdir(base_dir)
files.sort()
l = []
for f in files[3:]:
    if f.endswith('.jpg'):
        img = cv2.imread(os.path.join(base_dir, f), cv2.IMREAD_UNCHANGED)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img1 = cv2.filter2D(img_gray, -1, kernel_4)
        img2 = cv2.filter2D(img_gray, -1, kernel_8)
        # print(img_gray.shape)
        # img1 = cv2.resize(img_gray, (224, 224)) #.resize(img.size)
        # img2 = cv2.resize(img1, img_gray.shape[::-1])
        print(img2.shape)
        cv2.imwrite('./img0.png', img_gray)
        cv2.imwrite('./img1.png', img1)
        cv2.imwrite('./img2.png', img2)
        cv2.imwrite('./img3.png', img2 - img1)
        break
