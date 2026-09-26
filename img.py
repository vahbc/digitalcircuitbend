# import cv2 module
import random
import numpy as np
import cv2
import matplotlib.pyplot as plt



def rand(x):
    return int(random.randint(0, x - 1))

# read the image
img = cv2.imread('input3.png')

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th, dst = cv2.threshold(gray_image,127,255, cv2.THRESH_TOZERO)

h, w, c = img.shape

pixels = img.reshape(-1, c)
np.random.shuffle(pixels)
shuffled = pixels.reshape(h, w, c)
#print(img)
arr = []
arr2 = []
for i, row in enumerate(img):

  # get the pixel values by iterating
    for j, pixel in enumerate(img):
                # update the pixel value to black
        
        temp = dst[i][j]
        t2 = img[i][j]
        #temp = img[i][j]
        arr.append(temp)
        arr2.append(t2)

        if dst[i][j] > 150:
           img[i][j] = int(random.randint(220, 255))
        else:
          img[i][j] = arr2[rand(len(arr2))]
        #print(arr2)
        #print(dst[i][j])
        #print(cv2.threshold(gray_image,127,255, cv2.THRESH_TOZERO))

#print(arr)


# display image
#cv2.imshow("output", img)
cv2.imwrite("output.png", img)
#cv2.imwrite('shuffled.png', shuffled)


cv2.imwrite("opencv-[thresh-tozero.png", dst)