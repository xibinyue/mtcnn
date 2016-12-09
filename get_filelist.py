#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
author:  xibin.yue   
date:  2016/12/9
descrption: 
"""
import glob
import os


def get_filelist():
    path_dir = '/home/meteo/xibin.yue/mtcnn/data/'
    dir_ = map(lambda x: os.path.join(path_dir, x), os.listdir(path_dir))
    print dir_
    filelist = []
    for _dir in dir_:
        temp = map(lambda x: os.path.join(_dir, x), os.listdir(_dir))
        filelist.append(temp)
    with open('filelist.txt', 'w') as f:
        for sublist in filelist:
            for line in sublist:
                f.write(line + '\n')


if __name__ == '__main__':
    get_filelist()
