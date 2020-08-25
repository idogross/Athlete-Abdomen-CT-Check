import numpy as np
import cv2


# read image
image = cv2.imread('Binary.bmp', 0)

# Opening to clean image
se_circ = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (26, 26))
opened = cv2.morphologyEx(src=image, kernel=se_circ, op=cv2.MORPH_OPEN)

# show opened image
cv2.imshow('Opening', opened)
cv2.waitKey(0)
cv2.destroyAllWindows()

# connected components
_, labels = cv2.connectedComponents(opened)
area = np.sum(labels[labels == 1])
labels[labels != 1] = 0
labels[labels == 1] = 255
mask_liver = labels.astype(np.uint8)

# show liver
cv2.imshow(f'Area of liver in pixels: {str(int(area))}', mask_liver)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Liver boundaries
SE_circ2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
eroded = cv2.morphologyEx(src=mask_liver, kernel=SE_circ2, op=cv2.MORPH_ERODE)
Liver_boundary = mask_liver - eroded

# Original liver ct + boundary
liver_CT = cv2.imread('Liver_CT.bmp', 0)
liver_CT_combined = cv2.addWeighted(liver_CT, 0.6, Liver_boundary, 0.4, gamma=0)

# Show liver and boundary
cv2.imshow('Liver and Boundary', liver_CT_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
