import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math as math



def MakeMatrix(br,c,img,ope):
	rows,cols = img.shape
	matrixOutput = [[] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			if(ope == 'expo'):
				matrixOutput[i].append(ExpOp(br,c,img[i,j]))
			elif(ope == 'raise'):
				matrixOutput[i].append(RaiseOp(br,c,img[i,j]))
			elif(ope == 'log'):
				matrixOutput[i].append(LogOp(c,img[i,j]))
	return matrixOutput
	
def ExpOp(b,c,pixelVal):
	return c*(pow(b,pixelVal)-1)

def RaiseOp(r,c,pixelVal):
	return c*(pow(pixelVal,r))
	
def LogOp(c,pixelVal):
	return c*(math.log(1 + pixelVal))


img1 = cv.imread('exp_5.jpg',0)

br = 0.05
c = 5

n = 5

output = [[] for i in range(n)]

for i in range(n):
	for j in range(n):
		output[i].append(MakeMatrix(br+(i*0.4),c+(j*5),img1,'raise'))
		

plt.figure()
pos = 1
for i in range(n):
	for j in range(n):
		plt.subplot(n,n,pos)
		plt.imshow(output[i][j],'gray')
		plt.axis('off')
		plt.axis('tight')
		plt.axis('image')
		plt.title('r = '+str(round(br+(i*0.005),3))+' ; c = '+str(round(c+(j*5),3)))
		pos = pos + 1
plt.show()
		

