import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

class Threshold:
    def __init__(self, imgInput):
        self.img = imgInput
        self.l = 0
        self.r = 255

    def thFunction(self, fxy):
        if( self.l <= fxy and fxy <= self.r):
            return 255
        else:
            return 0

    def thresholding(self,left=0,right=255):
        self.l = left
        self.r = right
        rows,cols = self.img.shape
        newMatrix = [[] for i in range(rows)]
        for i in range (rows):
            for j in range(cols):
                newMatrix[i].append(self.thFunction(self.img[i,j]))
        return np.array(newMatrix)

