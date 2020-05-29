import cv2,matplotlib
import numpy as np
import matplotlib.pyplot as plt
inimage=cv2.imread('03200242三浦乙利_in.jpg')
changeimage=cv2.imread('03200242三浦乙利_in.jpg')

tate=inimage.shape[0]
yoko=inimage.shape[1]

#中心ちょい上を拡大する
x=yoko//5
y=tate//4

for i in range(tate//2):
    for j in range(yoko//2):
        changeimage[2*i][2*j]=inimage[i+x][j+y]
        changeimage[2*i][2*j+1]=inimage[i+x][j+y]
        changeimage[2*i+1][2*j]=inimage[i+x][j+y]
        changeimage[2*i+1][2*j+1]=inimage[i+x][j+y]

cv2.imwrite('03200242三浦乙利_1-2_out.jpg',changeimage)