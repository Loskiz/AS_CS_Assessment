from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('zz.jpeg')  #打开图像
one=img.convert('1')   #转换成灰度
gray=img.convert('L')
p=img.convert('P')
RGB=img.convert('RGB')
RGBA=img.convert('RGBA')

plt.subplot(2,3,1), plt.title('original')
plt.imshow(img),plt.axis('off')
plt.subplot(2,3,2), plt.title('1bit')
plt.imshow(one),plt.axis('off')
plt.subplot(2,3,3), plt.title('8bit')
plt.imshow(gray),plt.axis('off')
plt.subplot(2,3,4), plt.title('24bit')
plt.imshow(RGB),plt.axis('off')
plt.subplot(2,3,5), plt.title('32bit')
plt.imshow(RGBA),plt.axis('off')


plt.show()
