import cv2 
import numpy as np

image = cv2.imread('bear.jpg')

def MirrorImage(baseImage):
    width, height, channels = baseImage.shape
    mirror = np.zeros([width,height,3],np.uint8)
    for i  in range(0,width):
        for j in range(0,height):
            mirror[i,j] = image[i,height-1-j]
    return mirror

mirrorImage = MirrorImage(image)

cv2.imshow('Original image',image)
cv2.imshow('Mirror image',mirrorImage)
cv2.waitKey(0)
cv2.destroyAllWindows()