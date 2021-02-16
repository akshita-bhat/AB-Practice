import imutils
import cv2

# load image
image = cv2.imread("jp.png")
# image stats
(h,w,d) = image.shape
print("width={}, height={}, depth={}".format(w,h,d))

#display an image
'''
cv2.imshow("Image", image)
cv2.waitKey(0)
'''
# Information:
'''
> What is a pixel?

> All images consist of pixels which are the raw building blocks of images. 
> Images are made of pixels in a grid. 
> A 640 x 480 image has 640 columns (the width) and 480 rows (the height). 
> There are 640 * 480 = 307200  pixels in an image with those dimensions.

> Each value in the BGR 3-tuple has a range of [0, 255]. 
> How many color possibilities are there for each pixel in an RGB image in OpenCV? 
> That’s easy: 256 * 256 * 256 = 16777216

'''

# Pixel at x=50 and y=100 has the value of Red = 41, Green = 49 and Blue = 37
(B,G,R) = image[100,50]
print("R = {}, G = {}, B = {}".format(R,G,B))

# region of interest : slicing the image!
# starting at x = 320, y = 60 and ending at 
# x = 420, y = 180 
'''
roi = image[60:180, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
'''

# resizing images
'''
resized = cv2.resize(image, (200,200))
cv2.imshow("Resized", resized)
cv2.waitKey(0)
'''






