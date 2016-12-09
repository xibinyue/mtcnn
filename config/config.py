#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
author:  xibin.yue   
date:  2016/12/9
descrption: 
"""
import os
import caffe

IMAGE_LIST_FILE = "/home/meteo/xibin.yue/mtcnn/filelist.txt"
CAFFE_PATH = '/usr/local/caffe'
CAFFE_MODEL_PATH = "/home/meteo/xibin.yue/mtcnn/model"

FACE_IMAGE_PATH = '/home/meteo/xibin.yue/mtcnn/result/'
PNet = caffe.Net(CAFFE_MODEL_PATH + "/det1.prototxt", CAFFE_MODEL_PATH + "/det1.caffemodel", caffe.TEST)
RNet = caffe.Net(CAFFE_MODEL_PATH + "/det2.prototxt", CAFFE_MODEL_PATH + "/det2.caffemodel", caffe.TEST)
ONet = caffe.Net(CAFFE_MODEL_PATH + "/det3.prototxt", CAFFE_MODEL_PATH + "/det3.caffemodel", caffe.TEST)


def touch_dir(path):
    result = False
    try:
        path = path.strip().rstrip("\\")
        if not os.path.exists(path):
            os.makedirs(path)
            result = True
        else:
            result = True
    except:
        result = False
    return result
