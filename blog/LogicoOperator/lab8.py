import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



class Imagen:
	def __init__(self,_imgA):
		self.imgA = _imgA
	
	def notFunction(self):
		rows = self.imgA.shape[0]
		cols = self.imgA.shape[1]
		matrixOut = [[] for i in range(rows)]
		for i in range(rows):
			for j in range(cols):
				matrixOut[i].append(255-self.imgA[i][j])
		return np.array(matrixOut)

	def andFunction(self,imgB):
		size1 = self.imgA.shape[0] + self.imgA.shape[1]
		size2 = imgB.shape[0] + imgB.shape[1]
		if(size1 > size2):
			self.imgA = cv.resize(self.imgA,imgB.shape[1::-1])
		else:
			imgB = cv.resize(imgB,self.imgA.shape[1::-1])
		self.imgA = self.imgA.astype(int)
		imgB = imgB.astype(int)

		rows = self.imgA.shape[0]
		cols = self.imgA.shape[1]
		matrixOut = [[] for i in range(rows)]
		for i in range(rows):
			for j in range(cols):
				matrixOut[i].append(self.imgA[i][j] & imgB[i][j])
		return np.array(matrixOut)


	def orFunction(self,imgB):
		size1 = self.imgA.shape[0] + self.imgA.shape[1]
		size2 = imgB.shape[0] + imgB.shape[1]
		if(size1 > size2):
			self.imgA = cv.resize(self.imgA,imgB.shape[1::-1])
		else:
			imgB = cv.resize(imgB,self.imgA.shape[1::-1])
		self.imgA = self.imgA.astype(int)
		imgB = imgB.astype(int)

		rows = self.imgA.shape[0]
		cols = self.imgA.shape[1]
		matrixOut = [[] for i in range(rows)]
		for i in range(rows):
			for j in range(cols):
				matrixOut[i].append(self.imgA[i][j] | imgB[i][j])
		return np.array(matrixOut)

	def xorFunction(self,imgB):
		size1 = self.imgA.shape[0] + self.imgA.shape[1]
		size2 = imgB.shape[0] + imgB.shape[1]
		if(size1 > size2):
			self.imgA = cv.resize(self.imgA,imgB.shape[1::-1])
		else:
			imgB = cv.resize(imgB,self.imgA.shape[1::-1])
		self.imgA = self.imgA.astype(int)
		imgB = imgB.astype(int)

		rows = self.imgA.shape[0]
		cols = self.imgA.shape[1]
		matrixOut = [[] for i in range(rows)]
		for i in range(rows):
			for j in range(cols):
				matrixOut[i].append(self.imgA[i][j] ^ imgB[i][j])
		return np.array(matrixOut)


#img_A = cv.imread('log_3.png',0)
#img_B = cv.imread('log_4.png',0)
#img_A = cv.imread('sub_10.jpg',0)
#img_B = cv.imread('sub_11.jpg',0)

#imgOut = img.notFunction()
#img1 = Imagen(img_A)
#imgOut1 = img1.notFunction()
#img2 = Imagen(img_B)
#imgOut2 = img2.notFunction()

#img = Imagen(imgOut1)
#imgOut = img.andFunction(imgOut2)

#plt.imshow(imgOut,'gray',vmin=0,vmax=255)
#plt.show()
