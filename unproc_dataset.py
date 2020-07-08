import cv2
import os
import numpy as np
import csv
import glob

label = "Uninfected"
directoryList = glob.glob("cell_images/"+label+"/*.png")
file = open("csv/dataset.csv", "a")

for image_path in directoryList:

    img = cv2.imread("image_path")
    img = cv2.GaussianBlur(img, (5, 5), 2)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, 1, 2)

    file.write(label)
    file.write(",")

    for i in range(5):
        try:
            area = cv2.contourArea(contours[i])
            file.write(str(area))
        except:
            file.write("0")

        file.write(",")

    file.write("\n")
