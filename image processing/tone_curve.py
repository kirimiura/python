import cv2,matplotlib
import numpy as np
import matplotlib.pyplot as plt
inimage=cv2.imread('lena.jpeg')
changeimage=cv2.imread('lena.jpeg')

tate=inimage.shape[0]
yoko=inimage.shape[1]

for i in range(tate):
    for j in range(yoko):
        gray=0.114*inimage[i][j][0]+0.587*inimage[i][j][1]+0.299*inimage[i][j][2]
        if (gray+1)/64<=1:
            changeimage[i][j][0]=255
            changeimage[i][j][1]=gray*4
            changeimage[i][j][2]=0
        elif (gray+1)/64<=2:
            changeimage[i][j][0]=255-4*(gray-63)
            changeimage[i][j][1]=255
            changeimage[i][j][2]=0
        elif (gray+1)/64<=3:
            changeimage[i][j][0]=0
            changeimage[i][j][1]=255
            changeimage[i][j][2]=4*(gray-127)
        elif (gray+1)/64<=4:
            changeimage[i][j][0]=0
            changeimage[i][j][1]=255-4*(gray-191)
            changeimage[i][j][2]=255

cv2.imwrite('out_tonecurve.jpeg',changeimage)
