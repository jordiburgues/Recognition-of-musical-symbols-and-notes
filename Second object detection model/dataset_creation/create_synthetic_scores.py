#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:33:52 2019
SYNTHETIC SCORES GENERATION
@author: jordi
"""

import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random 
import matplotlib.patches as patches
import xml.etree.ElementTree as ET
from imgaug import augmenters as iaa
import imgaug as ia

#Music symbols
quaver = Image.open('images/crotchet.png').convert("RGBA")
uquaver=Image.open('images/upside.png').convert("RGBA")
quarter=Image.open('images/quarternote.png').convert("RGBA")
uquarter=Image.open('images/rquarternote.png').convert("RGBA")
half=Image.open('images/halfnote1.png').convert("RGBA")
uhalf=Image.open('images/halfnote2.png').convert("RGBA")

whole=Image.open('images/whole.png').convert("RGBA")
dotted=Image.open('images/dotted.png').convert("RGBA")

#Clefs
gclef=Image.open('images/gclef.png').convert("RGBA")
fclef=Image.open('images/fclef.png').convert("RGBA")

#Rests
rest16=Image.open('images/rest16th.png').convert("RGBA")
rest=Image.open('images/rest.png').convert("RGBA")
rest8=Image.open('images/rest8th.png').convert("RGBA")
resth=Image.open('images/rest4.png').convert("RGBA")
restw=Image.open('images/rest5.png').convert("RGBA")

new_width  = 40
new_height = 80

#Resizing of music symbols
quaver = quaver.resize((new_width, 70), Image.ANTIALIAS)
uquaver = uquaver.resize((20, 70), Image.ANTIALIAS)
quarter = quarter.resize((new_width, 77), Image.ANTIALIAS)
uquarter = uquarter.resize((new_width, 83), Image.ANTIALIAS)
half = half.resize((new_width, 77), Image.ANTIALIAS)
uhalf = uhalf.resize((new_width, 83), Image.ANTIALIAS)
whole = whole.resize((33, 33), Image.ANTIALIAS)
dotted = dotted.resize((new_width, 77), Image.ANTIALIAS)

gclef = gclef.resize((80, 140), Image.ANTIALIAS)
fclef = fclef.resize((61, 72), Image.ANTIALIAS)

rest16=rest16.resize((27, 50), Image.ANTIALIAS)
rest=rest.resize((44, 60), Image.ANTIALIAS)
rest8=rest8.resize((35,28),Image.ANTIALIAS)
resth=resth.resize((60, 50), Image.ANTIALIAS)
restw=restw.resize((60, 50), Image.ANTIALIAS)

#Variable for data augmentation
da=0
for i in range(0,1):
    #da_choice=random.choice([1,2,3,4,5,6,7])
    da_choice=0
    #da_choice=random.choice([0,1,2,4])
    x_coord=0
    y_coord=0
    offset=400
    distance=random.choice([440,500,600])
    position=0
    
    width=2707
    height=3828
    
    name_file="twelve{}".format(i+1)
    
    fname="variety/"+name_file+".xml"
    rootn=ET.Element("annotation")
    #Make the name of new XML file a variable!
    rootn=ET.Element("annotation")
    filenamelement=ET.Element("filename")
    rootn.append(filenamelement)
    sizeelement=ET.Element("size")
    rootn.append(sizeelement)
    segelement=ET.Element("segmented")
    rootn.append(segelement)
    w=ET.SubElement(sizeelement,"width")
    w.text=str(width)
    h=ET.SubElement(sizeelement,"height")
    h.text=str(height)
    d=ET.SubElement(sizeelement,"depth")
    d.text="1"
    segelement.text="0"
    filenamelement.text=name_file+".png"
    
    im = Image.new('RGB', (width,height), (255, 255, 255))
    wi,height=im.size
    
    #Create figure and axes
    fig,ax = plt.subplots(1)
    
    if distance==220:
        numgstafflines=14
    elif distance==440:
        numgstafflines=8
    elif distance==500:
        numgstafflines=6
    elif distance==600:
        numgstafflines=4
        
    numsymbols=60
    
    for j in range(0,numgstafflines):
        
        clef=random.choice([gclef,fclef])
        if clef==gclef:
            im.paste(gclef,(100,offset+18),gclef)
        else:
            im.paste(fclef,(120,offset+40),fclef)
        x_coord=200
        draw=ImageDraw.Draw(im)
        draw.line((100,40+offset)+(wi-100,40+offset), fill=0,width=3)
        draw.line((100,60+offset)+(wi-100,60+offset), fill=0,width=3)
        draw.line((100,80+offset)+(wi-100,80+offset), fill=0,width=3)
        draw.line((100,100+offset)+(wi-100,100+offset), fill=0,width=3)
        draw.line((100,120+offset)+(wi-100,120+offset), fill=0,width=3)
        
        #Vertical line at the end of each group of staff lines
        draw.line((wi-100,40+offset)+(wi-100,120+offset),fill=0,width=3)
        
        #Draws vertical line between two groups of staff lines
        if j%2==0:
            draw.line((100,40+offset)+(100,120+offset+distance), fill=0,width=3)
        
        #choice=random.choice([uhalf,uquarter,half,quarter,quaver,uquaver,whole])
        #choice=whole
        for k in range(0,numsymbols):
            
            #Draw bar every 5 symbols         
            if i%5==0 and x_coord>300:
                draw=ImageDraw.Draw(im)
                draw.line((x_coord,40+offset)+(x_coord,120+offset),fill=0,width=3)
            
# =============================================================================
#             if j%2==0:
#                 choice=random.choice([uhalf,uquarter,half,quarter,quaver,uquaver,whole,rest,rest16,rest8,resth,restw])
#             else:
# =============================================================================
            choice=random.choice([uhalf,uquarter,half,quarter,quaver,uquaver,whole])

                
            if x_coord<2500:
                if choice==rest8:
                    im.paste(choice,(x_coord,offset+65),choice)
                elif choice==rest:
                    im.paste(choice,(x_coord,offset+48),choice)
                elif choice==rest16:
                    im.paste(choice,(x_coord,offset+48),choice)
                elif choice==resth:
                    im.paste(choice,(x_coord,57+offset),choice)
                elif choice==restw:
                    im.paste(choice,(x_coord,35+offset),choice)
            #choice=uquaver
            choosekind=random.choice([0,1])
            index=random.choice([2,3,4,5,6,7,10,12,16,18])
            if choice in(uhalf,uquarter,half,quarter,quaver,uquaver,whole) and x_coord<2500:
                for l in range(0,index):
                    if choosekind==0:
                        #y_min=random.choice([-30,-10,10,30,50,70,90,110])
                        if choice in(uhalf,uquarter,whole,uquaver):
                            if choice in(uhalf,uquarter):
                                y_min=random.choice([-70,-50,-30,-10,10,30,50])
                            elif choice==uquaver:
                                y_min=random.choice([-30,-10,10,30,50,70])
                            else:
                                y_min=random.choice([-30,-10,10,30,50,70,90,110,130,150,170,190])
                        elif choice in (half,quarter,quaver):
                            y_min=random.choice([30,50,70,90,110,130])
                            
                    else:
                        #y_min=random.choice([-40,-20,0,20,40,60,80,100])
                        if choice in (uhalf,uquarter,whole,uquaver):
                            if choice in (uhalf,uquarter):
                                y_min=random.choice([-60,-40,-20,0,20,40,60])
                            elif choice==uquaver:
                                y_min=random.choice([-40,-20,0,20,40,60])
                            else:
                                y_min=random.choice([-40,-20,0,20,40,60,80,100,120,140,160,180])
                        elif choice in (half,quarter,quaver):
                            y_min=random.choice([40,60,80,100,120])
    
                    if y_min in (-60,-70):
                        if y_min==-60:
                            position=19
                        else:
                            position=20
                        draw.line((x_coord+7,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                        draw.line((x_coord+7,offset)+(x_coord+36,offset), fill=0,width=3)
                        draw.line((x_coord+7,offset-20)+(x_coord+36,offset-20), fill=0,width=3)
                        draw.line((x_coord+7,offset-40)+(x_coord+36,offset-40), fill=0,width=3)
                    elif y_min==-50:
                        position=18
                        draw.line((x_coord+7,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                        draw.line((x_coord+7,offset)+(x_coord+36,offset), fill=0,width=3)
                        draw.line((x_coord+7,offset-20)+(x_coord+36,offset-20), fill=0,width=3)
                    elif y_min==-40:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=17
                            if choice==whole:
                                draw.line((x_coord-4,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                                draw.line((x_coord-4,offset)+(x_coord+36,offset), fill=0,width=3)
                                draw.line((x_coord-4,offset-20)+(x_coord+36,offset-20), fill=0,width=3)
                            elif choice==uquaver:
                                draw.line((x_coord-5,20+offset)+(x_coord+23,20+offset), fill=0,width=3)
                                draw.line((x_coord-5,offset)+(x_coord+23,offset), fill=0,width=3)
                                draw.line((x_coord-5,offset-20)+(x_coord+23,offset-20), fill=0,width=3)
                            else:
                                draw.line((x_coord+7,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                                draw.line((x_coord+7,offset)+(x_coord+36,offset), fill=0,width=3)
                                draw.line((x_coord+7,offset-20)+(x_coord+36,offset-20), fill=0,width=3)
                    elif y_min==-30:
                        if choice in(uhalf,uquarter,whole,uquaver):
                           position=16
                           if choice==whole:
                                draw.line((x_coord-4,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                                draw.line((x_coord-4,offset)+(x_coord+36,offset), fill=0,width=3)
                           elif choice==uquaver:
                               draw.line((x_coord-5,20+offset)+(x_coord+23,20+offset), fill=0,width=3)
                               draw.line((x_coord-5,offset)+(x_coord+23,offset), fill=0,width=3)
                               draw.line((x_coord-5,offset-20)+(x_coord+23,offset-20), fill=0,width=3)
                           else:
                               draw.line((x_coord+7,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                               draw.line((x_coord+7,offset)+(x_coord+36,offset), fill=0,width=3)
                    elif y_min==-20:
                        if choice in(uhalf,uquarter,whole,uquaver):
                           position=15
                           if choice==whole:
                               draw.line((x_coord-4,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                               draw.line((x_coord-4,offset)+(x_coord+36,offset), fill=0,width=3)
                           elif choice==uquaver:
                               draw.line((x_coord-5,20+offset)+(x_coord+23,20+offset), fill=0,width=3)
                               draw.line((x_coord-5,offset)+(x_coord+23,offset), fill=0,width=3)
                           else:
                               draw.line((x_coord+7,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                               draw.line((x_coord+7,offset)+(x_coord+36,offset), fill=0,width=3)
                    elif y_min==-10:
                        if choice in(uhalf,uquarter,whole,uquaver):
                           position=14
                           if choice==whole:
                               draw.line((x_coord-4,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                           elif choice==uquaver:
                               draw.line((x_coord-5,20+offset)+(x_coord+23,20+offset), fill=0,width=3)
                               draw.line((x_coord-5,offset)+(x_coord+23,offset), fill=0,width=3)
                           else:
                               draw.line((x_coord+7,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                    elif y_min==0:
                        if choice in(uhalf,uquarter,whole,uquaver):
                           position=13
                           if choice==whole:
                               draw.line((x_coord-4,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                           elif choice==uquaver:
                               draw.line((x_coord-5,20+offset)+(x_coord+23,20+offset), fill=0,width=3)
                           else:
                               draw.line((x_coord+7,20+offset)+(x_coord+36,20+offset), fill=0,width=3)
                    elif y_min==10:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=12
                            if choice==uquaver:
                                draw.line((x_coord-5,20+offset)+(x_coord+23,20+offset), fill=0,width=3)
                    elif y_min==20:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=11
                    elif y_min==30:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=10
                        elif choice in (half,quarter,quaver):
                            position=6
                    elif y_min==40:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=9
                        elif choice in (half,quarter,quaver):
                            position=5
                    elif y_min==50:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=8
                        elif choice in (half,quarter,quaver):
                            position=4
                    elif y_min==60:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=7
                        elif choice in (half,quarter,quaver):
                            position=3
                    elif y_min==70:
                        if choice in(uhalf,uquarter,whole,uquaver):
                            position=6
                        elif choice in (half,quarter,quaver):
                            position=2
                    elif y_min==80:
                        if choice in(uhalf,uquarter,whole):
                            position=5
                        elif choice in (half,quarter,quaver):
                            position=1
                            if choice==quaver:
                                draw.line((x_coord-3,140+offset)+(x_coord+26,140+offset), fill=0,width=3)
                            else:
                                draw.line((x_coord+4,140+offset)+(x_coord+32,140+offset), fill=0,width=3)
                    elif y_min==90:
                        if choice in(uhalf,uquarter,whole):
                            position=4
                        elif choice in (half,quarter,quaver):
                            position=21
                            if choice==quaver:
                                draw.line((x_coord-5,140+offset)+(x_coord+26,140+offset), fill=0,width=3)
                            else:
                                draw.line((x_coord+4,140+offset)+(x_coord+32,140+offset), fill=0,width=3)
                    elif y_min==100:
                        if choice in(uhalf,uquarter,whole):
                            position=3
                        elif choice in (half,quarter,quaver):
                            position=22
                            if choice==quaver:
                                draw.line((x_coord-5,140+offset)+(x_coord+26,140+offset), fill=0,width=3)
                                draw.line((x_coord-5,160+offset)+(x_coord+26,160+offset), fill=0,width=3)
                            else:
                                draw.line((x_coord+4,140+offset)+(x_coord+32,140+offset), fill=0,width=3)
                                draw.line((x_coord+4,160+offset)+(x_coord+32,160+offset), fill=0,width=3)
                    elif y_min==110:
                       if choice in(uhalf,uquarter,whole):
                            position=2
                       elif choice in (half,quarter,quaver):
                           position=23
                           if choice==quaver:
                               draw.line((x_coord-5,140+offset)+(x_coord+26,140+offset), fill=0,width=3)
                               draw.line((x_coord-5,160+offset)+(x_coord+26,160+offset), fill=0,width=3)
                           else:
                               draw.line((x_coord+4,140+offset)+(x_coord+32,140+offset), fill=0,width=3)
                               draw.line((x_coord+4,160+offset)+(x_coord+32,160+offset), fill=0,width=3)
                    elif y_min in (120,130):
                        if choice==whole:
                            if y_min==120:
                                position=1
                            else:
                                position=21
                            draw.line((x_coord-4,140+offset)+(x_coord+36,140+offset), fill=0,width=3)
                        elif choice in (quarter,half,quaver):
                            if y_min==120:
                                position=24
                            else:
                                position=25
                            if choice==quaver:
                                draw.line((x_coord-5,140+offset)+(x_coord+26,140+offset), fill=0,width=3)
                                draw.line((x_coord-5,160+offset)+(x_coord+26,160+offset), fill=0,width=3)
                                draw.line((x_coord-5,180+offset)+(x_coord+26,180+offset), fill=0,width=3)
                            else:
                                draw.line((x_coord+4,140+offset)+(x_coord+32,140+offset), fill=0,width=3)
                                draw.line((x_coord+4,160+offset)+(x_coord+32,160+offset), fill=0,width=3)
                                draw.line((x_coord+4,180+offset)+(x_coord+32,180+offset), fill=0,width=3)
                            
                    elif y_min in (140,150):
                        if y_min==140:
                            position=22
                        else:
                            position=23
                        draw.line((x_coord-4,140+offset)+(x_coord+36,140+offset), fill=0,width=3)
                        draw.line((x_coord-4,160+offset)+(x_coord+36,160+offset), fill=0,width=3)
                    elif y_min in (160,170):
                        if y_min==160:
                            position=24
                        else:
                            position=25
                        draw.line((x_coord-4,140+offset)+(x_coord+36,140+offset), fill=0,width=3)
                        draw.line((x_coord-4,160+offset)+(x_coord+36,160+offset), fill=0,width=3)
                        draw.line((x_coord-4,180+offset)+(x_coord+36,180+offset), fill=0,width=3)
                    elif y_min in(180,190):
                        if y_min==180:
                            position=26
                        else:
                            position=27
                        draw.line((x_coord-4,140+offset)+(x_coord+36,140+offset), fill=0,width=3)
                        draw.line((x_coord-4,160+offset)+(x_coord+36,160+offset), fill=0,width=3)
                        draw.line((x_coord-4,180+offset)+(x_coord+36,180+offset), fill=0,width=3)
                        draw.line((x_coord-4,200+offset)+(x_coord+36,200+offset), fill=0,width=3)
                        
                    if choice==uquaver:
                       position+=1
                       
                    if choice in (uhalf,uquarter,uquaver):
                        y_min=y_min+2
                    
                    if choice==whole:
                        im.paste(choice,(x_coord,y_min+offset+4),choice)
                    else:
                        im.paste(choice,(x_coord,y_min+offset),choice)
                    
                    h=choice.size[1]
                    x_min=x_coord
                    x_max=x_min+new_width
                    y_min=y_min+offset
                    y_max=h+y_min
                    
                    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 25)
                    #draw.text((x_min-5, y_min-5), str(position),(0, 0, 0, 0), font = font)
                    
                    if choice in(quarter,half):
                        if y_min-offset in (80,90,100,110,120,130):
                            x_max=x_max+5
                            x_min=x_min-4
                            y_min=y_min-2
                        y_min=y_min+50
                        x_max=x_max-12
                        x_min=x_min+7
                        y_max=y_max-9
                    elif choice==uquarter:
                        if y_min-offset-2 in (0,-10,-20,-30,-40,-50,-60,-70):
                            x_max=x_max+5
                            x_min=x_min-1
                            y_max=y_max+1
                            y_min=y_min-2
                        y_min=y_min+7
                        x_max=x_max-9
                        x_min=x_min+7
                        y_max=y_max-56
                    elif choice==uhalf:
                        if y_min-offset-2 in (0,-10,-20,-30,-40,-50,-60,-70):
                            x_max=x_max+5
                            x_min=x_min-6
                            y_max=y_max+2
                            y_min=y_min-2
                        y_min=y_min+9
                        x_max=x_max-8
                        x_min=x_min+12
                        y_max=y_max-56
                    elif choice==quaver:
                        if y_min-offset in (80,90,100,110,120,130):
                            x_max=x_max+5
                            x_min=x_min-6
                            y_max=y_max-1
                            y_min=y_min-2
                        x_max=x_max-18
                        y_min=y_min+50
                        y_max=y_max-2
                    elif choice==uquaver:
                        if y_min-offset-2 in (-30,-40,-20,-10,0,10):
                            x_max=x_max+5
                            x_min=x_min-6
                            y_max=y_max+3
                            y_min=y_min-2
                        x_max=x_max-21
                        y_max=y_max-52
                    elif choice==whole:
                         if y_min-offset in (0,-10,-20,-30,-40,120,130,140,150,160,170,180,190):
                            x_max=x_max-5
                            x_min=x_min-5
                         else:
                            x_max=x_max-8
                        
                         y_min=y_min+9
                         y_max=y_max-4
                         
                    objelement=ET.Element("object")
                    rootn.append(objelement)
                    
                    name=ET.SubElement(objelement, "name")
                    bndbox=ET.SubElement(objelement,"bndbox")
                    
                    xmn=ET.SubElement(bndbox, "xmin")
                    xmx=ET.SubElement(bndbox, "xmax")
                    ymn=ET.SubElement(bndbox, "ymin")
                    ymx=ET.SubElement(bndbox, "ymax")
                                    
                    if da_choice==1:
                        transf=iaa.Affine(shear=10.0)
                    elif da_choice==2:
                        transf = iaa.GaussianBlur(2.5)
                    elif da_choice==3:
                        transf=iaa.ElasticTransformation(alpha=(0.5, 1.5), sigma=0.25)
                    elif da_choice==4:
                        transf=iaa.ContrastNormalization((0.5, 2.0))
                    elif da_choice==5:
                        transf=iaa.Sharpen(alpha=(0,1.0),lightness=20.0)
                    elif da_choice==6:
                        transf=iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0))
                    elif da_choice==7:
                        transf=iaa.SaltAndPepper(0.08)
                            
                    if da==1:
                        #Data augmentation
                        imcv2=np.array(im)
                        bb=ia.BoundingBoxesOnImage([ia.BoundingBox(x1=x_min, y1=y_min, x2=x_max, y2=y_max)],shape=imcv2.shape)
                        transf_det=transf.to_deterministic()
                        bbs_aug=transf_det.augment_bounding_boxes([bb])[0]
                        bbs_aug=bbs_aug.bounding_boxes[0]
                        
                        x_min=bbs_aug.x1
                        x_max=bbs_aug.x2
                        y_min=bbs_aug.y1
                        y_max=bbs_aug.y2
                        
                        print(x_min)
                        print(x_max)
                        print(y_min)
                        print(y_max)
                        
                    xmn.text=str(np.float64((x_min)/1))  #/widthc
                    xmx.text=str(np.float64((x_max)/1))  #/widthc
                    ymn.text=str(np.float64((y_min)/1)) #/heightc
                    ymx.text=str(np.float64((y_max)/1)) #/heightc
                    name.text=str(position)
                    tree=ET.ElementTree(rootn)
                    with open(fname,"wb") as fh:
                                tree.write(fh)
                    
                    
                    rect = patches.Rectangle((x_min,y_min),x_max-x_min,y_max-y_min,linewidth=1,edgecolor='r',facecolor='none')
                    #rect = patches.Rectangle((bbs_aug.x1,bbs_aug.y1),bbs_aug.x2-bbs_aug.x1,bbs_aug.y2-bbs_aug.y1,linewidth=1,edgecolor='r',facecolor='none')
                    ax.add_patch(rect)
                
            x_coord=x_coord+40
            
        # Display the image
        #ax.imshow(im, cmap='gray')
            
        offset=offset+distance
      
    #im.save("variety/"+name_file+".png")
    #plt.show()
    
    #im_da=Image.open("variety/"+name_file+"da.png")
    imcv2=np.array(im)
    
    if da_choice==1:
        transformation=iaa.Affine(shear=10.0)
    elif da_choice==2:
        transformation = iaa.GaussianBlur(2.5)
    elif da_choice==3:
        transformation=iaa.ElasticTransformation(alpha=(0.5, 1.5), sigma=0.25)
    elif da_choice==4:
        transformation=iaa.ContrastNormalization((0.5, 2.0))
    elif da_choice==5:
        transformation=iaa.Sharpen(alpha=(0,1.0),lightness=20.0)
    elif da_choice==6:
        transformation=iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0))
    elif da_choice==7:
        transformation=iaa.SaltAndPepper(0.08)
        
    if da_choice==0:
        cv2.imwrite("variety/"+name_file+".png",imcv2)
    else:
        imcv2_transf = transformation.augment_image(imcv2)
        cv2.imwrite("variety/"+name_file+".png",imcv2_transf)
    
# =============================================================================
#     sp=iaa.SaltAndPepper(0.03)
#     imcv2_sp=sp.augment_image(imcv2)
#     cv2.imwrite("variety/"+name_file+"da_2.png",imcv2_sp)
# =============================================================================
    
    #second=iaa.ContrastNormalization((0.5, 2.0))
    #second=iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0))
    #second=iaa.Sharpen(alpha=(0,1.0),lightness=20.0)
    #second=iaa.Affine(shear=6.0)
    #second=iaa.ElasticTransformation(alpha=(0.5, 3.5), sigma=0.25)
    #second=iaa.PiecewiseAffine((0.0, 0.1))
    #second=iaa.PerspectiveTransform(scale=(0.01, 0.1))
# =============================================================================
#     imcv2_second=second.augment_image(imcv2)
#     cv2.imwrite("variety/"+name_file+"da_3.png",imcv2_second)
# =============================================================================

# =============================================================================
#     new=iaa.AllChannelsCLAHE
#     imcv2_all=new.augment_image(new)
#     cv2.imwrite("variety/"+name_file+"da_4.png",imcv2_all)
# =============================================================================
    
    if da_choice==0:
        ax.imshow(imcv2, cmap='gray')
        plt.show()
    else:
        ax.imshow(imcv2_transf, cmap='gray')
        plt.show()