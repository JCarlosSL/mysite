import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class PointOperator:
    def __init__(self,_img):
        self.img=_img
        self.row,self.col=_img.shape

    def FCS(self,Fxy,c,d):
        return ((Fxy - c)*(255/(d-c)))

    def contrastStretching(self,l=0):
        hist,bins = np.histogram(self.img.flatten(),256,[0,256])
        c=np.min(self.img)
        d=np.max(self.img)

        l=((self.row*self.col)/100)*l

        i=c
        count=0
        while True:
            count=count+hist[i]
            if(count>=float(l)):
                c=i
                break
            i=i+1
        i=d
        count=0
        while True:
            count=count+hist[i]
            if(count>=float(l)):
                self.d=i
                break
            i=i-1
        newhist=[]
        for i in range(len(hist)):
            newhist.append(self.FCS(i,c,d))

        newimg=[[] for i in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):
                newimg[i].append(newhist[self.img[i,j]])
        return np.array(newimg)

"""
img = cv.imread('imgoutlier.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])

data=PointOperator(img)

newimg=data.contrastStretching()
cv.imwrite('outimg.jpg',newimg)
hist,bins = np.histogram(newimg.flatten(),256,[0,256])

plt.subplot(2,2,1),plt.imshow(img,'gray',vmin=0,vmax=255)
plt.subplot(2,2,2),plt.hist(img.flatten(),256,[0,256],color='b')
plt.subplot(2,2,3),plt.imshow(newimg,'gray',vmin=0,vmax=255)
plt.subplot(2,2,4),plt.hist(newimg.flatten(),256,[0,256],color='b')
plt.show()
"""
