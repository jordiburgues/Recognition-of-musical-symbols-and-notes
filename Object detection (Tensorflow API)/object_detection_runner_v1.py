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
width=500
height=350


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
    #print(scores_array[0])
    #print(scores_array)
    
    #XML where predicted bboxes coordinates are written
    newname=os.path.basename(image_path)
    namexml=os.path.splitext(newname)[0]
    #print(newname)
    #print(namexml)
    fname="/u/46/burguej1/unix/Desktop/newxmls/"+namexml+"._predicted.xml"
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
    d.text="3"
    segelement.text="0"
    filenamelement.text=newname
    classes= np.squeeze(classes).astype(np.int32)

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
            
            class_f=CATEGORY_INDEX[classes[i]]['name']
            print(class_f)
            
            objelement=ET.Element("object")
            rootn.append(objelement)
                            
            name=ET.SubElement(objelement, "name")
            bndbox=ET.SubElement(objelement,"bndbox")
                    
            xmn=ET.SubElement(bndbox, "xmin")
            xmx=ET.SubElement(bndbox, "xmax")
            ymn=ET.SubElement(bndbox, "ymin")
            ymx=ET.SubElement(bndbox, "ymax")
                            
            xmn.text=str(np.float64((x_min)*width))  #/widthc
            xmx.text=str(np.float64((x_max)*width))  #/widthc
            ymn.text=str(np.float64((y_min)*height)) #/heightc
            ymx.text=str(np.float64((y_max)*height)) #/heightc
            name.text=str(class_f)
            tree=ET.ElementTree(rootn)
            with open(fname,"wb") as fh:
                tree.write(fh)
    #print(count)
    fig = plt.figure()
    fig.set_size_inches(5, 3.5)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    plt.imshow(image_np, aspect = 'auto')
    plt.savefig('output/{}'.format(image_path), dpi = 100)
    plt.close(fig)

# TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image-{}.jpg'.format(i)) for i in range(1, 4) ]
TEST_IMAGE_PATHS = glob.glob(os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.jpg'))

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
