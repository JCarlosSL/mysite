import cv2 as cv
import matplotlib.pyplot as plt
from pointOperator import pointOperator as pop


def plotshow(img,function):

    l = [60,90,120]
    plt.subplot(2,2,1),plt.imshow(img,'gray',vmin=0,vmax=256)
    for i in range(1,4):
        newimg = function(l[i-1])
        plt.subplot(2,2,i+1),plt.imshow(newimg,'gray',vmin=0,vmax=256)

    plt.show()

#Ejercicio 1
img = cv.imread('log_1.jpg',0)
logOp1 = pop(img)
plotshow(img,logOp1.logarithmOperator)

img1 = cv.imread('log_6.jpg',0)
logOp2 = pop(img1)
plotshow(img1,logOp2.logarithmOperator)


#ejercicio 2
img2 = cv.imread('exp_5.jpg',0)
logOp3 = pop(img2)
plotshow(img2,logOp3.logarithmOperator)

#ejercicio 3
img3 = cv.imread('log_12.jpg',0)
logOp4 = pop(img3)
plotshow(img3,logOp4.raizOperator)
