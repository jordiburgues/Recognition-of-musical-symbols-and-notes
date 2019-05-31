# -*- coding: utf-8 -*-
"""
CREATES NON-OVERLAPPING CROPS FOR TESTING
@author: burguej1
"""

from PIL import Image
import numpy as np
import cv2

import xml.etree.ElementTree as ET

#Create XML to store original coordinates
fname="coordinates.xml"
rootn=ET.Element("annotation")


im =  cv2.imread("lordoftherings.png")

im = cv2.resize(im,(2066,2924))

imgheight=im.shape[0]
imgwidth=im.shape[1]

y1 = 0

#Non-verlapping crops dimensions
M = 700 #350
N = 1000 #500

for x in range(0, imgwidth, N):
    for y in range(0,imgheight,M):
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
        
        if height_t==M and width_t==N:
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
        
            #####DIRECTORY MUST BE CHANGED IF USED IN ANOTHER COMPUTER##############
            cv2.imwrite("nonoverlappingcrops/" + str(x) + '_' + str(y)+".png",image2)
        #cv2.rectangle(im, (x, y), (x1, y1), (0, 255, 0))

#cv2.imwrite("asas.png",im)
