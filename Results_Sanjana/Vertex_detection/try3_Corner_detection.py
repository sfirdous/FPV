import cv2 
import numpy as np 
  
# path to input image specified and  
# image is loaded with imread command 
# image = cv2.imread('Triangle2.png') 
# image = cv2.imread('Pentagon.png') 
# image = cv2.imread('Triangle.jpg') 
# image = cv2.imread('Irregular_Pentagon.jpg') 
image = cv2.imread('Shapes/Pentagon_RandomShape.png') 
  
# convert the input image into 
# grayscale color space 
operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
# modify the data type 
# setting to 32-bit floating point 
operatedImage = np.float32(operatedImage) 
  
# apply the cv2.cornerHarris method 
# to detect the corners with appropriate 
# values as input parameters 
dest = cv2.cornerHarris(operatedImage, 2, 7, 0.01) 
  
# Results are marked through the dilated corners 
dest = cv2.dilate(dest, None) 
  
# Reverting back to the original image, 
# with optimal threshold value 
image[dest > 0.0001 * dest.max()]=[0, 0, 255] 
  
# the window showing output image with corners 
cv2.imshow('Image with Borders', image) 
  
# De-allocate any associated memory usage  
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 