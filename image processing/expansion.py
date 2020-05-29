import cv2,matplotlib
import numpy as np
import matplotlib.pyplot as plt
inimage=cv2.imread('lena.jpeg')
changeimage=cv2.imread('lena.jpeg')

tate=inimage.shape[0]
yoko=inimage.shape[1]


x=yoko//5
y=tate//4

for i in range(tate//2):
    for j in range(yoko//2):
        changeimage[2*i][2*j]=inimage[i+x][j+y]
        changeimage[2*i][2*j+1]=inimage[i+x][j+y]
        changeimage[2*i+1][2*j]=inimage[i+x][j+y]
        changeimage[2*i+1][2*j+1]=inimage[i+x][j+y]

cv2.imwrite('out_expansion.jpeg',changeimage)
