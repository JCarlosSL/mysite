import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import matplotlib.cbook as cbook

class ConstS:
    def __init__(self,_img):
        self.a=0
        self.b=255
        self.img=_img
        self.c=0
        self.d=255
        self.v=False

    def Formula(self,Fxy):
        return (((Fxy-self.c)*((self.b-self.a)/(self.d-self.c)))+self.a)%256

    def Stretch(self):
    
    	if self.v==False:
    		self.c=np.min(self.img)
    		self.d=np.max(self.img)
    	
    	rows,columns=self.img.shape
    	newimg=[[] for i in range(rows)]
    	for i in range(rows):
    		for j in range(columns):
    			pixel=0
    			if(self.c < self.img[i,j] < self.d):
    				pixel=self.img[i,j]
    			else:
    				pixel=((self.d-self.c)/2)+self.c
    			newimg[i].append(self.Formula(pixel))
    	return np.array(newimg)

    def CDlimit(self,l=0):
        self.hist,bins =np.histogram(self.img.flatten(),256,[0,256])
        
        self.v=True
        self.c=np.min(self.img)
        self.d=np.max(self.img)

        rows,columns=self.img.shape
        l=((rows*columns)/100)*l
        
        i=self.c
        count=0
        while True:
            count=count+self.hist[i]
            if(count>int(l)):
                self.c=i
                break
            i=i+1
        i=self.d
        count=0
        while True:
            count=count+self.hist[i]
            if(count>=int(l)):
                self.d=i
                break
            i=i-1

def addOutlier(img,r,c):
    for i in range(r):
        for j in range(c):
            img[i,j]=1
"""
img=cv.imread('contrast.jpg',0)

#ContrastStretching sin outlier
contrast=ConstS(img)
contrast.CDlimit()
newimg=contrast.Stretch()

cv.imwrite('outimg.jpg',newimg)

#Agregando outlier a la imagen
addOutlier(img,30,30)
cv.imwrite('imgoutlier.jpg',img)

#Aplicando ContrastStretch con limites
contrast1=ConstS(img)
contrast1.CDlimit(15)
newimg1=contrast1.Stretch()

cv.imwrite('outimgoutlier.jpg',newimg1)
"""

