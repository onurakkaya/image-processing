import cv2
import numpy as np

def ConvertToGrayscale(baseImage):
    width, height, channels = baseImage.shape
    gray = np.zeros([width,height,channels],np.uint8)

    # We're looking all pixels of x-axis.
    for i  in range(0,width):
        # We're looking all pixels of y-axis
        for j in range(0,height):
            # We're merging 3 layers into the 1 layer. 0.114, 0.587 and 0.299 values are the coefficients used to set brightness chosen by according human vision skills.
            # For more information about the coefficients, please see Rec.ITU-R BT.601-7
            gray[i,j] =  baseImage[i,j, ] * 0.114 + baseImage[i,j,1] *  0.587 + baseImage[i,j,2] * 0.299
    return gray