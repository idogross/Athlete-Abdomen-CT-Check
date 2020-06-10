import numpy as np
from matplotlib import pyplot as plt
import cv2



## read image
image = cv2.imread('Binary.bmp',0)
mask = np.zeros(image.shape)

## Opening to clean image
SE_circ = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(26,26))
opened = cv2.morphologyEx(src=image , dst=mask , kernel=SE_circ , op=cv2.MORPH_OPEN)

## show opened image
# cv2.imshow('Opening',opened)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## connected components
retval, labels = cv2.connectedComponents(opened)
mask_liver = np.array(labels,dtype=np.uint8)
mask_liver[labels == 1] = 255

## show liver
# cv2.imshow(f'Area of liver in pixels: {str(int(np.sum(mask_liver)/255))}',mask_liver)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## Liver bounadries
mask2 = np.zeros(image.shape)
SE_circ2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
eroded = cv2.morphologyEx(src=mask_liver , dst=mask2, kernel=SE_circ2, op=cv2.MORPH_ERODE)
Liver_boundary = mask_liver - eroded

## Originial liver ct + boundary
Liver_CT = cv2.imread('Liver_CT.bmp',0)
Liver_CT_combined = np.zeros(Liver_CT.shape)
Liver_CT_combined = cv2.addWeighted(Liver_CT, 0.8, Liver_boundary, 0.5, gamma=0)

## Show liver and boundary
cv2.imshow('Liver and Boundary', Liver_CT_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
