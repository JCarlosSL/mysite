import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math as math

class pointOperator:
    def __init__(self, _img):
        self.img = _img
        self.c = 0
        self.b = 0
        self.r = 0
    
    def functionExp(self,b,c,fxy):
        return c*(pow(b,fxy)-1)

    def functionRaise(self,r,c,fxy):
        return c*(pow(fxy,r))

    def expoOperator(self,b,c):
        rows, cols = self.img.shape
        imgOut = [[] for i in range(rows)]
        for i in range(rows):
        	for j in range(cols):
        		imgOut[i].append(self.functionExp(b,c,self.img[i,j]))
        return np.array(imgOut)

    def raiseOperator(self,r,c):
        rows, cols = self.img.shape
        imgOut = [[] for i in range(rows)]
        for i in range(rows):
        	for j in range(cols):
        		imgOut[i].append(self.functionRaise(r,c,self.img[i,j]))
        return np.array(imgOut)

