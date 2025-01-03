import numpy as np
import cv2 as cv
 
# filename = 'Irregular_Pentagon.jpg'
# filename = 'Shapes/DrawnTriangle.jpg'
filename = 'D:\FPV\Results_Sanjana\Vertex_detection\Shapes\Square_vivoT15g.jpg'
# filename = 'Shapes/Irregular_Pentagon.jpg'
# filename = 'Shapes/Pentagon.png'
# filename = 'Shapes/Triangle.png'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
 
#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)
 
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.0002*dst.max()]=[0,0,255]
 
cv.imshow('Corner Detection',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()