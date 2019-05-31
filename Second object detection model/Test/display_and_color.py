# -*- coding: utf-8 -*-
"""
DISPLAYS DETECTED OBJECTS IN A SPECIFIC MUSIC SCORE AND CREATES THE COLOR MAP
FOR THE APPLICATION
@author: burguej1
"""
from PIL import Image, ImageDraw
import numpy as np
import xml.etree.ElementTree as ET
import matplotlib.patches as patches
import matplotlib.pyplot as plt

################TO BE CHANGED##########################
imname="real_scores/hobbit.png"
xmlname="real_scores/hobbit.xml"
################TO BE CHANGED##########################

im=Image.open(imname)
width, height = im.size


if width==4250:
    new_width=2125
    new_height=2750
else:
    new_width=2066
    new_height=2924

old_w=2066
old_h=2924

################TO BE CHANGED##########################
fname="newhobbit1.xml"
################TO BE CHANGED##########################

rootn=ET.Element("annotation")

colored = Image.new('RGBA', (new_width,new_height), (255, 255, 255))
draw=ImageDraw.Draw(colored)

im = im.resize((new_width,new_height), Image.ANTIALIAS)
tree = ET.parse(xmlname)
root=tree.getroot()

#Compute the number of objects (bounding boxes) in the xml file
numelem=0
for description in root.iter('object'):
    numelem+=1
    
labels= ["" for x in range(numelem)]

#Creates an array containing the values of xmin,ymin,xmax and ymax tags from
#xml file
def obtain_coordinates(str):
    i=0
    #coord= ["" for x in range(numelem)]
    coord=np.zeros(numelem)
    for description in root.iter(str):
        #print(description.text)
        coord[i]=description.text
        i+=1
    return coord

#Store the corresponding class name of every bounding box
i=0
for description in root.iter('name'):
    labels[i]=description.text
    i+=1    
    
#Store all bounding boxes coordinates in different vectors
xmins = obtain_coordinates('xmin')
ymins = obtain_coordinates('ymin')
xmaxs = obtain_coordinates('xmax')
ymaxs = obtain_coordinates('ymax')

print(xmins)
#Display original image
image = np.array(im, dtype=np.int64)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(image, cmap='gray')

#Loop over all bounding boxes and plot the ones stored in the random crop
for i in range(0,numelem):
#Uncomment width, height if cooridnates are absolute (from original file)
    xmin=(xmins[i]/old_w)*new_width#*width
    ymin=(ymins[i]/old_h)*new_height #height
    xmax=(xmaxs[i]/old_w)*new_width #width
    ymax=(ymaxs[i]/old_h)*new_height #height
    
    currentclass=labels[i]
        
    objelement=ET.Element("object")
    rootn.append(objelement)
                            
    name=ET.SubElement(objelement, "name")
    bndbox=ET.SubElement(objelement,"bndbox")
                    
    xmn=ET.SubElement(bndbox, "xmin")
    xmx=ET.SubElement(bndbox, "xmax")
    ymn=ET.SubElement(bndbox, "ymin")
    ymx=ET.SubElement(bndbox, "ymax")
            
    xmin_d=np.float64(xmin)-10
    xmax_d=np.float64(xmax)
    ymin_d=np.float64(ymin)-10
    ymax_d=np.float64(ymax)+25
    
    if currentclass == "1.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(1,153,153))
    elif currentclass=="2.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(10,204,102))
    elif currentclass=="3.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(20,255,102))
    elif currentclass=="4.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(30,204,51))
    elif currentclass=="5.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(40,102,0))
    elif currentclass=="6.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(50,153,153))
    elif currentclass=="7.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(60,36,45))
    elif currentclass=="8.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(70,51,102))
    elif currentclass=="9.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(80,153,255))
    elif currentclass=="10.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(90,51,153))
    elif currentclass=="11.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(100,51,255))
    elif currentclass=="12.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(110,36,45))
    elif currentclass=="13.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(120,0,204))
    elif currentclass=="14.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(130,153,204))
    elif currentclass=="15.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(140,10,25))
    elif currentclass=="16.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(150,102,102))
    elif currentclass=="17.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(160,153,0))
    elif currentclass=="18.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(170,255,255))
    elif currentclass=="19.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(180,204,204))
    elif currentclass=="20.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(190,0,255))
    elif currentclass=="21.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(200,30,0))
    elif currentclass=="22.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(210,40,25))
    elif currentclass=="23.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(220,100,0))
    elif currentclass=="24.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(230,153,0))
    elif currentclass=="25.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(240,253,0))
    elif currentclass=="26.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(250,60,255))
    elif currentclass=="27.0":
        draw.rectangle(((xmin_d, ymin_d), (xmax_d, ymax_d)), fill=(251,200,200))
                       
                        
    xmn.text=str(xmin_d)  #/widthc
    xmx.text=str(xmax_d) #/widthc
    ymn.text=str(ymin_d)#/heightc
    ymx.text=str(ymax_d) #/heightc
            
    name.text=str(currentclass)
    tree=ET.ElementTree(rootn)
    with open(fname,"wb") as fh:
        tree.write(fh)


    #width=xmax-xmin, height=ymax-ymin, (xmin,ymin) left bottom corner
    rect = patches.Rectangle((xmin,ymin),xmax-xmin,ymax-ymin,linewidth=1,edgecolor='r',facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

################TO BE CHANGED##########################
colored.save("real_scores/hobbitcolored.png")
################TO BE CHANGED##########################
plt.savefig('real_scores/hobbitdetections.png',bbox_inches='tight',pad_inches=0,dpi=1000)
plt.show() 


