#!/usr/bin/env python
import cv2
import numpy as np
import imutils

path_1 = '/home/krzysztof/catkin_ws/src/hello_world/src/perception/color_filtering/tennis_ball_1.jpg'
#path_2 = '/home/krzysztof/catkin_ws/src/hello_world/src/perception/color_filtering/tennis_ball_3.jpg'
#path_3 = '/home/krzysztof/catkin_ws/src/hello_world/src/perception/color_filtering/tennis_ball_3.jpg'

image_1 = cv2.imread(path_1)
#image_2 = cv2.imread(path_2)
#image_3 = cv2.imread(path_3)
image_1 = cv2.resize(image_1, (0,0), fx = 0.5, fy = 0.5)
cv2.imshow('Tennis_Ball_Display', image_1)

#convert from RGB to HSV
image_1_hsv = cv2.cvtColor(image_1, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV_Image_Dispaly', image_1_hsv)

#definicja zakresu kolowru lpilki tenisowek
yellow_lower = (30, 100, 50)
yellow_upper = (60, 255, 255)

#tworzenie maski
mask = cv2.inRange(image_1_hsv, yellow_lower, yellow_upper)

cv2.imshow('Mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()


