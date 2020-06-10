# Athlete-Abdomen-CT-Check
Ahead of the Rio de Janeiro Olympics, an athlete (preferred to remain anonymous) is suspected of using prohibited supplements.
One of their side effects is increased liver. The Disciplinary Committee has decided to examine the athlete's liver using 
an abdomen CT scan.
One section of the received scan is attached (Liver_CT.bmp)
Write an algorithm that separates the liver from the other organs, finds its area and its boundaries using connected components and morphological operators.

Display the following:
* CT sacn with the liver boundaries you found.
* A black and white image of the liver (without the other organs) with its area in the title of the image.
  The committee has set a threshold of 24000 pixels as grounds for disqualification of athletes. Was the athlete disqualified?

**NOTE:**
This question was part of Medical Image Processing Course HW (0555452001) (Tel Aviv University).

## Input Abdomen CT
![Liver CT](/Liver_CT.bmp)
