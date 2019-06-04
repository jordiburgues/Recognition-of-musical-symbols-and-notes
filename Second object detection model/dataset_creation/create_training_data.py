# -*- coding: utf-8 -*-
import os, fnmatch
from PIL import Image
import numpy as np
import random
import xml.etree.ElementTree as ET

def randCrop(img,nw,nh):
    width, height = img.size
    x=random.randint(0,width-nw-1)
    y=random.randint(0,height-nh-1)
    im=img.crop((x,y,x+nw,y+nh))
    return im,x,y,x+nw,y+nh

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


def createXML(name,widthc,heightc,nameim):
    #Create new XML for the random cropped image
    rootn=ET.Element("annotation")
    #Make the name of new XML file a variable!
    fname=name
    rootn=ET.Element("annotation")
    filenamelement=ET.Element("filename")
    rootn.append(filenamelement)
    sizeelement=ET.Element("size")
    rootn.append(sizeelement)
    segelement=ET.Element("segmented")
    rootn.append(segelement)
    w=ET.SubElement(sizeelement,"width")
    w.text=str(widthc)
    h=ET.SubElement(sizeelement,"height")
    h.text=str(heightc)
    d=ET.SubElement(sizeelement,"depth")
    d.text="1"
    segelement.text="0"
    filenamelement.text=nameim
    
    tree=ET.ElementTree(root)
    with open(fname,"wb") as fh:
        tree.write(fh)

    #Store all bounding boxes coordinates in different vectors
    xmins = obtain_coordinates('xmin')
    ymins = obtain_coordinates('ymin')
    xmaxs = obtain_coordinates('xmax')
    ymaxs = obtain_coordinates('ymax')
    
    return xmins,ymins,xmaxs,ymaxs,rootn,fname
    
listScores=os.listdir('.')
pattern="*.png"

j=0
numcrops=60
widthc=500
heightc=350
#File containing all images name without extension
txtfile = open("trainval.txt","w+")
for entry in listScores:
       if fnmatch.fnmatch(entry,pattern):
          j+=1
          nameim=entry
          namexml=os.path.splitext(entry)[0]+".xml"
          
          im=Image.open(nameim)
          width,height=im.size
          
          tree = ET.parse(namexml)
          root=tree.getroot()
          
          #Compute the number of objects (bounding boxes) in the xml file
          numelem=0
          for description in root.iter('object'):
                  numelem+=1
    
          labels= ["" for x in range(numelem)]
          print(numelem)
          
          #Store the corresponding class name of every bounding box
          k=0
          for description in root.iter('name'):
              labels[k]=description.text
              k+=1    
              
          count=0
          widthc=500
          heightc=350
          
          for i in range(0,numcrops):   
            count=0
            image,xminc,yminc,xmaxc,ymaxc = randCrop(im,widthc,heightc)
            #nameimage="random{0}".format(j)+"crop{0}.jpg".format(i+1)
            nameimage="random{0}".format(j)+"crop{0}.jpg".format(i+1)
            print(nameimage)
            image.save("images/"+nameimage,"JPEG")
            newxml="annotations/random{0}".format(j)+"crop{0}.xml".format(i+1)
            print(newxml)
            xmins,ymins,xmaxs,ymaxs,rootn,fname=createXML(newxml,widthc,heightc,nameimage)
                            
            #Write name into file
            #txtfile.write("random{0}".format(j)+"crop{0}\n".format(i+1))
            txtfile.write("random{0}".format(j)+"crop{0}\n".format(i+1))
            
            #Loop over all bounding boxes and plot the ones stored in the random crop
            for l in range(0,numelem):
                xmin=xmins[l]*width
                ymin=ymins[l]*height
                xmax=xmaxs[l]*width
                ymax=ymaxs[l]*height
                currentclass=labels[l]
                #Plot only bounding boxes inside new image
                #If the if statement is removed, all bboxes are plotted
                if xmin>=xminc and xmax<=xmaxc and  ymin>=yminc and ymax<=ymaxc:
                    objelement=ET.Element("object")
                    rootn.append(objelement)
                    
                    name=ET.SubElement(objelement, "name")
                    bndbox=ET.SubElement(objelement,"bndbox")
            
                    xmn=ET.SubElement(bndbox, "xmin")
                    xmx=ET.SubElement(bndbox, "xmax")
                    ymn=ET.SubElement(bndbox, "ymin")
                    ymx=ET.SubElement(bndbox, "ymax")
                    
                    #Adjust the bounding boxes to the new dynamic range
                    #Coordinates are transformed from original domain to [0,1] in 
                    #newimage
                    xmn.text=str(np.float64((xmin-xminc)/1))  #/widthc
                    xmx.text=str(np.float64((xmax-xminc)/1))  #/widthc
                    ymn.text=str(np.float64((ymin-yminc)/1)) #/heightc
                    ymx.text=str(np.float64((ymax-yminc)/1)) #/heightc
                    name.text=currentclass
                    count+=1
                    tree=ET.ElementTree(rootn)
                    with open("annotations/random{0}".format(j)+"crop{0}.xml".format(i+1),"wb") as fh:
                        tree.write(fh)
            if count==0:
                    objelement=ET.Element("object")
                    rootn.append(objelement)
                    
                    name=ET.SubElement(objelement, "name")
                    bndbox=ET.SubElement(objelement,"bndbox")
            
                    xmn=ET.SubElement(bndbox, "xmin")
                    xmx=ET.SubElement(bndbox, "xmax")
                    ymn=ET.SubElement(bndbox, "ymin")
                    ymx=ET.SubElement(bndbox, "ymax")
                    
                    #Adjust the bounding boxes to the new dynamic range
                    #Coordinates are transformed from original domain to [0,1] in 
                    #newimage
                    xmn.text=str(np.float64(0))  #/widthc
                    xmx.text=str(np.float64(0)) #/widthc
                    ymn.text=str(np.float64(0)) #/heightc
                    ymx.text=str(np.float64(0)) #/heightc
                    name.text="nothing"
                    count+=1
                    tree=ET.ElementTree(rootn)
                    with open("annotations/random{0}".format(j)+"crop{0}.xml".format(i+1),"wb") as fh:
                        tree.write(fh)
                
