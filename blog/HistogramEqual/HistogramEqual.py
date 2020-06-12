import numpy as np

class HistogramEqual:
    def __init__(self,_img):
        self.L=256
        self.img=_img

    """retorna el vector de el histograma normalizado"""
    def Pdistribucion(self,hist,totalPixel):
        vP=[]
        for i in range(len(hist)):
            vP.append(hist[i]/totalPixel)
        return vP


    def sumDistribucion(self,vP):
        sumD=[]
        temp=0
        for i in range(len(vP)):
            sumD.append(vP[i]+temp)
            temp+=vP[i]
        return sumD

    def functionS(self,Fxy,sumD):
        return (self.L-1)*sumD[Fxy]

    """Equalizacion de la imagen"""
    def Equalization(self):
        hist,bins = np.histogram(self.img.flatten(),256,[0,256])
        rows,columns = self.img.shape
        vP = self.Pdistribucion(hist,rows*columns)
        sumD = self.sumDistribucion(vP)

        newimg=[[] for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                newimg[i].append(self.functionS(self.img[i,j],sumD))
        return np.array(newimg)
    
    """Ecualizacion con una mascara de la misma imagen"""
    def EqualizationMask(self,point,rows,columns):
        imgMask=self.img[point[0]:point[0]+rows,point[1]:point[1]+columns]
        hist,bins = np.histogram(imgMask.flatten(),256,[0,256])
        x,y = imgMask.shape
        vP=self.Pdistribucion(hist,x*y)
        sumD = self.sumDistribucion(vP)

        rows,columns = self.img.shape

        newimg = [[] for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                newimg[i].append(self.functionS(self.img[i,j],sumD))

        return np.array(newimg),imgMask


