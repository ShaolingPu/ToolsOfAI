from PIL import Image, ImageEnhance
import numpy as np

img_dir = '../datasets/AliTampered/train/tampered/'
mask_dir = '../dataset/masks/'

files = os.listdir(img_dir)
files.sort()
l = []
for f in files:
    if f.endswith('.jpg'):
        img = Image.open(os.path.join(img_dir, f)).convert('RGBA')
        # print(np.array(img).shape)
        msk = Image.open(os.path.join(mask_dir, f.replace('jpg', 'png'))).convert('L')
        # print(np.array(msk).shape)
        shadow = Image.new('RGBA', img.size, (255,255,102))
        opacity = 0.7
        # print(np.array(shadow.split()[3]))
        alpha = ImageEnhance.Brightness(shadow.split()[3]).enhance(opacity)
        shadow.putalpha(alpha)
        # print(np.array(shadow.split()[3]))
        # shadow = shadow.convert('RGB')
        # shadow.save('sha.jpg')
        # break
        # print(shadow.size)
        msk = np.array(msk) // 3
        msk = Image.fromarray(msk.astype('uint8')).convert('L')
        # print(msk)
        # img_blender = Image.new('RGB', shadow.size, (0, 0, 0, 0))
        # shadow = Image.blend(shadow, img_blender, 0.0)
        # img.paste(shadow, (0, 0), mask=shadow.split()[3])
        img.paste(shadow, (0, 0), mask=msk)
        # print(np.array(msk.split()[3]))
        img = img.convert('RGB')
        img.save('./data_vis/'+f)
    # break
