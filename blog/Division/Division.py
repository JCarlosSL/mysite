import numpy as np

class divisionOperator:
    def __init__(self,_img):
        self.img=_img
        self.rows = _img.shape[0]
        self.cols = _img.shape[1]
        self.c=0
        self.d=255

    def div(self,p,q):
        return np.divide(p,q).astype(np.uint8)

    def divisionImg(self,imgs):
    	newimg = [ [] for i in range(self.rows)]
    	minimo=99999
    	maximo=0
    	for i in range(self.rows):
    		for j in range(self.cols):
    			if(minimo > self.img[i,j] / imgs[i,j]):
    				minimo = self.img[i,j] / imgs[i,j]
    			if(maximo < self.img[i,j] / imgs[i,j]):
    				maximo = self.img[i,j] / imgs[i,j]
    			newimg[i].append((self.img[i,j]/imgs[i,j]).astype(np.uint8))
    	newimg=self.rescaling(minimo,maximo,np.array(newimg))
    	return newimg

    def divisionC(self,c=1):
    
    
    	newimg = [ [] for i in range(self.rows)]
    	for i in range(self.rows):
    		for j in range(self.cols):
    			newimg[i].append(self.div(self.img[i,j],c))
    	return np.array(newimg)
    def funcrescaling(self,mini,maxi,fxy):
    	return ((fxy-mini)*(255/(maxi-mini)))
    
    def rescaling(self,mini,maxi,img1):
        newimg=[[] for i in range(self.rows)]
        for i in range(self.rows):
        	for j in range(self.cols):
        		newimg[i].append(self.funcrescaling(mini,maxi,img1[i,j]).astype(np.uint8))
        return np.array(newimg)
