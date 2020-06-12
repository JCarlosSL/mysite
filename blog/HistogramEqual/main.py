import cv2  as cv
import matplotlib.pyplot as plt
import numpy as np
from HistogramEqual import HistogramEqual as HisEqual

def plotShow(img,newimg):
    plt.subplot(2,2,1),plt.imshow(img,'gray',vmin=0,vmax=255)
    plt.subplot(2,2,2),plt.hist(img.flatten(),256,[0,256],color='b')
    plt.subplot(2,2,3),plt.imshow(newimg,'gray',vmin=0,vmax=255)
    plt.subplot(2,2,4),plt.hist(newimg.flatten(),256,[0,256],color='b')
    plt.show()

#procesamiento hist5
img = cv.imread('hist5.jpg',0)
HE = HisEqual(img)
newimg = HE.Equalization()
plotShow(img,newimg)

#procesamiento hist6
img1 = cv.imread('hist6.jpg',0)
HE1 = HisEqual(img1)
newimg1 = HE1.Equalization()
plotShow(img1,newimg1)

#procesamiento hist10
img3 = cv.imread('hist10_1.jpg',0)
HE3 = HisEqual(img3)

newimg3 = HE3.Equalization()
plotShow(img3,newimg3)

newimgmask,imgmask = HE3.EqualizationMask([210,160],80,60)

plotShow(imgmask,newimgmask)
