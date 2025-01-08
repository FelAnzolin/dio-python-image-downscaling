# executado no python 3.10
# pip install opencv-python

import cv2
import numpy as np

baseImage = cv2.imread('images/test01.jpg')
img = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (5, 5), 0)
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)
result = np.vstack([np.hstack([suave, bin]),
                    np.hstack([binI, cv2.bitwise_and(img, img, mask=binI)])])

cv2.imshow("Imagem original:", baseImage)
cv2.imshow("Downscaling da imagem:", result)
cv2.waitKey(0)
