import numpy as np

class blendingOperator:
    def __init__(self,_img):
        self.img=_img
        self.rows = self.img.shape[0]
        self.cols = self.img.shape[1]
        self.newimg = [ [] for i in range(self.rows)]

    def function(self,p1,p2,x):
        return p1 * x + p2 * (1-x)

    def blending(self,img2,x):

        for i in range(self.rows):
            for j in range(self.cols):
            	self.newimg[i].append(self.function(
                    self.img[i,j]/2,img2[i,j]/2,x).astype(np.int8))

        return np.array(self.newimg)
