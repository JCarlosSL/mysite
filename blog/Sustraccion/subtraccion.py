import numpy as np
import cv2 as cv

class subtraccion:
    def __init__(self,_img):
        self.img=_img


    def subtraccionImg(self,imgs):
        size1 = self.img.shape[0] + self.img.shape[1]
        size2 = imgs.shape[0] + imgs.shape[1]
        if(size1 > size2):
        	self.img = cv.resize(self.img,imgs.shape[1::-1])
        else:
        	imgs = cv.resize(imgs,self.img.shape[1::-1])
        rows = self.img.shape[0]
        cols = self.img.shape[1]

        newmatrix=[ [] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                newmatrix[i].append((self.img[i,j]-imgs[i,j]).astype(np.uint8))

        return np.array(newmatrix)

    def subtraccionC(self,c=0):
    	rows = self.img.shape[0]
    	cols = self.img.shape[1]
    	
    	newmatrix = [ [] for i in range(rows)]
    	for i in range(rows):
    		for j in range(cols):
    			newmatrix[i].append((self.img[i,j]-c).astype(np.uint8))
    	return np.array(newmatrix)
