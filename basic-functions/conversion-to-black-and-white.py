import cv2 
import numpy as np

# In most popular image processing method, we're describe each image layer as one byte (8 bits).
# In this case each layer can take a value between 0...255 brightness values.
# -> Black is expressed with 0 (min brightness) and white is expressed with 255 (max brightness).

# We're set choose to coefficient to maximum brightness
byteCoefficient = 255

#We're set threshold value as half of image brightness.
threshold = 0.5

def ConvertToBlackAndWhite(baseImage):
    width, height  = baseImage.shape
    bw = np.zeros([width,height],np.uint8)
    # We're looking all pixels of x-axis.
    for i  in range(0,width):
        # We're looking all pixels of y-axis
        for j in range(0,height):
            # We're convert the image to grayscale and merging the layers to operate before black and white conversion.
            bw[i,j] = baseImage[i,j,0] * 0.114 + baseImage[i,j,1] * 0.587 + baseImage[i,j,2] * 0.299
            # if brightness of the selected pixel is greater then threshold, we'll convert the pixel as white otherwise we'll convert that as black.
            if bw[i,j] > threshold * byteCoefficient:
                bw[i,j] = 1 * byteCoefficient 
            else:
                bw[i,j] = 0 * byteCoefficient
    return bw