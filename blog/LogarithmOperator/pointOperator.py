import numpy as np

class pointOperator:
    def __init__(self,_img):
        self.img=_img
        self.c=0

    def functionlog(self,Fxy,c):
        return c*np.log10(1+Fxy)

    def logarithmOperator(self,c):        
        rows,columns = self.img.shape
        newimg=[[] for i in range(rows)]

        for i in range(rows):
            for j in range(columns):
                newimg[i].append(self.functionlog(self.img[i,j],c))

        return np.array(newimg)

    def functionraiz(self,Fxy,c):
        return c*np.sqrt(Fxy)

    def raizOperator(self,c):
        rows,columns = self.img.shape
        newimg=[[] for i in range(rows)]

        for i in range(rows):
            for j in range(columns):
                newimg[i].append(self.functionraiz(self.img[i,j],c))

        return np.array(newimg)
