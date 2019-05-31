import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import json
import time
import glob

from io import StringIO
from PIL import Image

import matplotlib.pyplot as plt

from utils import visualization_utils as vis_util
from utils import label_map_util

from multiprocessing.dummy import Pool as ThreadPool

MAX_NUMBER_OF_BOXES = 1000
MINIMUM_CONFIDENCE = 0.75

PATH_TO_LABELS = 'annotations/label_map.pbtxt'
PATH_TO_TEST_IMAGES_DIR = 'test_images'

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=sys.maxsize, use_display_name=True)
CATEGORY_INDEX = label_map_util.create_category_index(categories)

# Path to frozen detection graph. This is the actual model that is used for the object detection.
MODEL_NAME = 'output_inference_graph'
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

import xml.etree.ElementTree as ET
#width=1000
#height=700

#==============================================================================
# width=1000
# height=700
# 
# crop_coord_x=1000
# crop_coord_y=700
#==============================================================================
width=500
height=350

crop_coord_x=500
crop_coord_y=350

def obtain_coordinates(str):
    i=0
    #coord= ["" for x in range(numelem)]
    coord=np.zeros(numelem)
    for description in root.iter(str):
        #print(description.text)
        coord[i]=description.text
        i+=1
    return coord

#Creates a new XML to store all detections
fname="object_detection/lala1.xml"
rootn=ET.Element("annotation")

#Parse XML with coordinates
nxml="object_detection/coordinates.xml"
tree = ET.parse(nxml)
root=tree.getroot()

numelem=0
for description in root.iter('coordinates'):
    numelem+=1
    
labels= ["" for x in range(numelem)]

xmins_or = obtain_coordinates('xmin_or')
ymins_or = obtain_coordinates('ymin_or')
print(xmins_or)
print(ymins_or)

###################TO BE CHANGED###############################
recomposition = Image.new('RGBA', (2066,2924), (255, 255, 255))
#recomposition = Image.new('RGBA', (2125,2750), (255, 255, 255))
##################TO BE CHANGED#################################

def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)

def detect_objects(image_path):
    
    count=0
    image = Image.open(image_path)
    image_np = load_image_into_numpy_array(image)
    
    image_np_expanded = np.expand_dims(image_np, axis=0)

    (boxes, scores, classes, num) = sess.run([detection_boxes, detection_scores, detection_classes, num_detections], feed_dict={image_tensor: image_np_expanded})

    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        CATEGORY_INDEX,
        min_score_thresh=MINIMUM_CONFIDENCE,
        use_normalized_coordinates=True,
        line_thickness=2)
        
    bboxes=np.squeeze(boxes)
    scores_array=np.squeeze(scores)

    for i in range(0,len(bboxes)):
        #Store only bounding boxes with at least MINIMUM_CONFIDENCE
        if scores_array[i]>MINIMUM_CONFIDENCE:
            print(scores_array[i])
            count=count+1
            #ymin
            y_min=bboxes[i][0]
            #xmin
            x_min=bboxes[i][1]
            #ymax
            y_max=bboxes[i][2]
            #xmax
            x_max=bboxes[i][3]
            
            class_f=classes[0][i]
            
            objelement=ET.Element("object")
            rootn.append(objelement)
                            
            name=ET.SubElement(objelement, "name")
            bndbox=ET.SubElement(objelement,"bndbox")
                    
            xmn=ET.SubElement(bndbox, "xmin")
            xmx=ET.SubElement(bndbox, "xmax")
            ymn=ET.SubElement(bndbox, "ymin")
            ymx=ET.SubElement(bndbox, "ymax")
            
            xmin_d=np.float64((x_min*crop_coord_x))+xmins_or[j]
            xmax_d=np.float64((x_max*crop_coord_x))+xmins_or[j]
            ymin_d=np.float64((y_min*crop_coord_y))+ymins_or[j]
            ymax_d=np.float64((y_max*crop_coord_y))+ymins_or[j]
                        
            xmn.text=str(xmin_d)  #/widthc
            xmx.text=str(xmax_d) #/widthc
            ymn.text=str(ymin_d)#/heightc
            ymx.text=str(ymax_d) #/heightc
            
            name.text=str(class_f)
            tree=ET.ElementTree(rootn)
            with open(fname,"wb") as fh:
                tree.write(fh)

    fig = plt.figure()
    #fig.set_size_inches(10, 7)
    fig.set_size_inches(5, 3.5)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.imshow(image_np, aspect = 'auto')

    plt.savefig('output/{}'.format(image_path), dpi = 100)
    plt.close(fig)
    
    image_wm = Image.open('output/{}'.format(image_path)).convert("RGBA")
    image_wm = image_wm.resize((crop_coord_x, crop_coord_y), Image.BILINEAR)
    recomposition.paste(image_wm,(np.int(xmins_or[j]),np.int(ymins_or[j])),image_wm)
    

# TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image-{}.jpg'.format(i)) for i in range(1, 4) ]
TEST_IMAGE_PATHS = glob.glob(os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.png'))
#TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'randscore1crop{}.png'.format(i+1)) for i in range(0, 60) ]

j=0
# Load model into memory
print('Loading model...')
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

print('detecting...')
with detection_graph.as_default():
    with tf.Session(graph=detection_graph) as sess:
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        for image_path in TEST_IMAGE_PATHS:
            detect_objects(image_path)
            j+=1
        recomposition.save("final.png")