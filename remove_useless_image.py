# -*- coding:UTF-8 -*-
"""
# @file name  : remove_useless_image.py
# @author     : zz0320
# @brief      : 删除没有标签的照片
"""

import os

path1 = r"/Users/kenton/Downloads/集群重点研发/蝠鲼数据集/jpg/处理结果集合/数据对齐与分割程序/VOCdevkit/VOC2007/Annotations"
#对比的文件夹（标签文件夹）
path2 = r"/Users/kenton/Downloads/集群重点研发/蝠鲼数据集/jpg/处理结果集合/数据对齐与分割程序/VOCdevkit/VOC2007/JPEGImages"
#删除文件的文件夹（图片文件夹）
filelist1 = os.listdir(path1) #该文件夹下所有的文件（包括文件夹）
filelist2 = os.listdir(path2)
tp = ".xml"      #要匹配标签文件的后缀


for file2 in filelist2:
    filename = os.path.splitext(file2)[0] + tp  # 匹配文件名
    if filename not in filelist1:           #如果没有对应匹配文件，就删除
        os.remove(os.path.join(path2, file2))