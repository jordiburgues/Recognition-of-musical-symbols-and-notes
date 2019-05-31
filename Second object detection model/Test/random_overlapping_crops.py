# -*- coding: utf-8 -*-
"""
CREATES RANDOM OVERLAPPING CROPS FOR TESTING
@author: burguej1
"""

from PIL import Image
import numpy as np
import cv2
import random
import os, fnmatch

numcrops=50


def randCrop(img,nw,nh):
    width, height = img.size
    x=random.randint(0,width-nw-1)
    y=random.randint(0,height-nh-1)
    im=img.crop((x,y,x+nw,y+nh))
    return im,x,y,x+nw,y+nh
    
#Width and height of random crops
widthc=1000
heightc=700

i=0
listFiles=os.listdir('.')
pattern="*.png"
print(listFiles)
for entry in listFiles:
    if fnmatch.fnmatch(entry,pattern):
        #Resize image before performing random crops
        im=Image.open(entry.format(i+1))
        im = im.resize((2707, 3828), Image.BILINEAR)
        
        for j in range(0,numcrops):
            image,xminc,yminc,xmaxc,ymaxc = randCrop(im,widthc,heightc)
            imcv2=np.array(image)
            togray=cv2.cvtColor(imcv2, cv2.COLOR_RGB2GRAY)
            image2=np.zeros_like(image)
            image2[:,:,0]=togray
            image2[:,:,1]=togray
            image2[:,:,2]=togray
            cv2.imwrite('newcrops/randscore{0}'.format(i+1)+'crop{0}.jpg'.format(j+1),image2)
        i+=1

