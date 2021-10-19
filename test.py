import numpy as np            
import cv2                     

img=cv2.imread('lenna.png')   #lenna.png 색조모드로 읽기
cv2.imshow('Lenna', img)
print(img.shape)

#(너비, 높이) 지정 방식 
width = int(img.shape[1]*0.5)
height = int(img.shape[0]*0.5)
img1=cv2.resize(img, dsize=(width, height))#1/2 축소 영상 
cv2.imshow('Lenna1', img1)

#(너비, 높이) 비율 지정 방식 
img2=cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.5)#1/2 축소 영상 
cv2.imshow('Lenna2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()         #열려있는 모든 창 닫기