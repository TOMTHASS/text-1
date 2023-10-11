import cv2
import numpy as np  
image1 = cv2.imread("C:\\Users\\tom20\\Desktop\\1.bmp")
image12 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
dst1 = cv2.GaussianBlur(image12,(19,19),0,0)
t2,dst2 = cv2.threshold(dst1,181,255,cv2.THRESH_BINARY_INV)
contours,hie =cv2.findContours(dst2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours = list(contours)
contours1 = []
if len(contours) >0:
    for i in range(0,len(contours)):
        contour = contours[i]
        npoints = len(contour)
        depth = contour.dtype
        if npoints>=0 and (depth == np.float32 or depth == np.int32):
            area = cv2.contourArea(contour)
        if area >= 14000 and area <= 15000:
            contours1.append(contours[i])
contours1 = tuple(contours1)
for contour in contours1:
    M = cv2.moments(contour)
    if M['m00']!=0:
        cX = int(M['m10']/M['m00'])
        cY = int(M['m01']/M['m00'])
        cv2.circle(image1,(cX,cY),5,(255,0,0),-1)
    perimeter = cv2.arcLength(contour,True)
    area = cv2.contourArea(contour)
    cv2.putText(image1,'perimeter is:{}'.format(perimeter),(30,90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.putText(image1,'area is:{}'.format(area),(30,130),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.putText(image1,'center is:({},{})'.format(cX,cY),(30,170),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv2.drawContours(image1,contours1,-1,(255,0,0),5)
cv2.imshow('1',image1)
cv2.waitKey(0)
cv2.destroyAllWindows()