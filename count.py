# -*- coding:UTF-8 -*-
"""
# @file name  : count.py
# @author     : zz0320
# @brief      : 各类数量统计
"""

import xml.etree.ElementTree as ET
import os
# 修改自己的路径
count0 = count1 = count2 = count3 = count4 = count5 = count6 = count7 = 0
template_file = r'/Users/kenton/Downloads/集群重点研发/蝠鲼数据集/jpg/处理结果集合/VOCdevkit/VOC2007/Annotations'  #这里是存放xml文件的文件夹
xmllist = os.listdir(template_file)
for xml in xmllist:
    if xml == '.DS_Store':
        continue
    # print(xml)

    # tree = ET.parse(os.path.join(template_file,xml))
    # root = tree.getroot() # 获取根节点

    # print(xml)
    file = open(os.path.join(template_file, xml)).read()
    # print(type(file))
    file = file.replace("&amp;", "_")
    file = file.replace("&", "_")
    # print(file)
    tree = ET.ElementTree(ET.fromstring(file))
    root = tree.getroot() # 获取根节点
    for child in root:
        # print(child.tag,child.attrib)
        if child.tag == 'object':
            name=child.find('name').text
            # print(name)
            if name == 'left_front':
                count0 += 1
            elif name == 'left_rear':
                count1 += 1

            elif name == 'right_front':
                count2 += 1

            elif name == 'right_rear':
                count3 += 1

            elif name == 'front':
                count4 += 1

            elif name == 'rear':
                count5 += 1

            elif name == 'left':
                count6 += 1

            elif name == 'right':
                count7 += 1

print(count0, count1, count2, count3, count4, count5, count6, count7)
