from PIL import Image
import matplotlib.pyplot as plt
import random as rd
img=[[0]*255 for i in range(255)]
for i in range(len(img)):
    for j in range(len(img[i])):
        img[i][j]=rd.randint(0,1)
plt.imshow(img)
plt.show()

