import cv2,matplotlib
import numpy as np
import matplotlib.pyplot as plt
inimage=cv2.imread('lena.jpeg')
changeimage=cv2.imread('lena.jpeg')

tate=inimage.shape[0]
yoko=inimage.shape[1]

for i in range(tate):
    for j in range(yoko//2):
        changeimage[i][yoko-j-1]=changeimage[i][j]

cv2.imwrite('out_mirror.jpeg',changeimage)

