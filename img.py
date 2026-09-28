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
th2, dst2 = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)
th3, dst3 = cv2.threshold(gray_image, 120, 255, cv2.THRESH_TRUNC)
th4, dst4 = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY_INV)

h, w, c = img.shape

pixels = img.reshape(-1, c)
np.random.shuffle(pixels)
shuffled = pixels.reshape(h, w, c)
#print(img)
arr = []
arr2 = []
rarr = []

for i in range(12):
   rarr.append(rand(img.shape[0]))
for i, row in enumerate(img):

  # get the pixel values by iterating
    for j, pixel in enumerate(img):
      temp = dst[i][j]
      t2 = img[i][j]
      #temp = img[i][j]
      arr.append(temp)
      arr2.append(t2)
  
#print(arr2)

for i, row in enumerate(img):

  # get the pixel values by iterating
    for j, pixel in enumerate(img):
                # update the pixel value to black
        
        

        if dst[i][j] > 150:
           #img[i][j] = arr2[rand(len(arr2))]
           img[i][j] = arr2[rand(len(arr2)-200)]
        elif dst2[i][j] > 150:
          #img[i][j] = int(random.randint(0, 255))
          img[i][j] = 23, 56, 34
          
          if j in rarr:
                      
            for k in range(img.shape[0]):
              img[i-k][j] = arr2[rand(len(arr2))]
              img[i-k][j-1] = arr2[rand(len(arr2))]
        elif dst3[i][j] > 50:
          img[i][j] = int(random.randint(0, 12))
        elif dst4[i][j] > 50:
                  #img[i][j] = int(random.randint(0, 255))
                  img[i][j] = arr2[rand(len(arr2))]
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