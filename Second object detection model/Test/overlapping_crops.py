# -*- coding: utf-8 -*-
"""
CREATES OVERLAPPING CROPS FOR TESTING
@author: burguej1
"""

from PIL import Image
import numpy as np
import cv2

import xml.etree.ElementTree as ET

#Create XML to store original coordinates
fname="coordinates.xml"
rootn=ET.Element("annotation")

#Read image and resize it
im=cv2.imread("hobbit1.png")
im = cv2.resize(im,(2066,2924))

imgheight=im.shape[0]
imgwidth=im.shape[1]

y1 = 0

#Overlap pixels in the x and y direction
M = 350
N = 500

limitw=300
limith=250

for x in range(0, imgwidth, limitw):
    for y in range(0,imgheight,limith):
        y1 = y + M 
        x1 = x + N 
        tiles = im[y:y+M,x:x+N]
        
        height_t=tiles.shape[0]
        width_t=tiles.shape[1]
        
        imcv2=np.array(tiles)
        togray=cv2.cvtColor(tiles, cv2.COLOR_RGB2GRAY)
        image2=np.zeros_like(tiles)
        image2[:,:,0]=togray
        image2[:,:,1]=togray
        image2[:,:,2]=togray
        
        print("image")
        print(x)
        print(y)
        print(image2.shape[0])
        print(image2.shape[1])
        if image2.shape[0]==M and image2.shape[1]==N:
            #XML file containing initial cropping coordinates
            coordinates=ET.Element("coordinates")
            rootn.append(coordinates)
                        
            xmn=ET.SubElement(coordinates, "xmin_or")
            ymn=ET.SubElement(coordinates, "ymin_or")
                        
            xmn.text=str(np.float64(x))
            ymn.text=str(np.float64(y))
                        
            tree=ET.ElementTree(rootn)
            with open(fname,"wb") as fh:
                tree.write(fh)
        
                
            cv2.imwrite("nonoverlappingcrops/" + str(x) + '_' + str(y)+".png",image2)
        #cv2.rectangle(im, (x, y), (x1, y1), (0, 255, 0))

#cv2.imwrite("asas.png",im)
