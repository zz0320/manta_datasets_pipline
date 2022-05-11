# -*- coding:UTF-8 -*-
"""
# @file name  : chang_xml_label.py
# @author     : zz0320
# @brief      : 批量修改xml文件中的类别名称 当有多个物体时，多个物体的名称均能被修改
"""

from lxml.etree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom
import xml.etree.ElementTree as ET
from xml.etree import ElementTree as etree
import os
import re
from lxml import etree
# 修改自己的路径
# parser = ET.XMLParser(encoding="utf-8")
template_file = r'/Users/kenton/Downloads/集群重点研发/蝠鲼数据集/jpg/处理结果集合/VOCdevkit/VOC2007/Annotations/'  #这里是存放xml文件的文件夹
xmllist = os.listdir(template_file)
# text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", text)
for xml in xmllist:
    if xml == '.DS_Store':
        continue
    # print(xml)
    file = open(os.path.join(template_file, xml)).read()
    # print(type(file))
    file = file.replace("&amp;", "_")
    file = file.replace("&", "_")
    # print(file)
    tree = ET.ElementTree(ET.fromstring(file))
    root = tree.getroot() # 获取根节点
    for child in root:

        print(child.tag,child.attrib)
        if child.tag == 'object':
            name=child.find('name').text
            # print(name)
            if name == '左前':
                child.find('name').text='left_front'
                tree=ET.ElementTree(root)
            elif name == '左后':
                child.find('name').text = 'left_rear'
                tree = ET.ElementTree(root)
            elif name == '右前':
                child.find('name').text = 'right_front'
                tree = ET.ElementTree(root)
            elif name == '右后':
                child.find('name').text = 'right_rear'
                tree = ET.ElementTree(root)
            elif name == '前侧':
                child.find('name').text = 'front'
                tree = ET.ElementTree(root)
            elif name == '后侧':
                child.find('name').text = 'rear'
                tree = ET.ElementTree(root)
            elif name == '左侧':
                child.find('name').text = 'left'
                tree = ET.ElementTree(root)
            elif name == '右侧':
                child.find('name').text = 'right'
                tree = ET.ElementTree(root)
    # print(tree)
    tree.write(os.path.join(template_file, xml))
