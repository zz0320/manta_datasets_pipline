# -*- coding:UTF-8 -*-
"""
# @file name  : video2image.py
# @author     : zz0320
# @brief      : 将视频切分为图片
"""

import cv2

# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image, addr, num):
    address = addr + str(num) + '.jpg'
    cv2.imwrite(address, image)


# 读取视频文件

j = 0
video_name = "IMG_8777.mp4"  # 视频名称
video_dir = "/Users/kenton/Downloads/集群重点研发/蝠鲼数据集/video/"  # 视频根目录
videoCapture = cv2.VideoCapture(video_dir + video_name)

# videoCapture=cv2.VideoCapture(1) # 这里就是直接调用摄像头

# 读帧
success, frame = videoCapture.read()

timeF = 10  # 按需更改
i = 0
while success:
    i = i + 1
    if (i % timeF == 0):
        s = 10000
        j = j + 1
        s += j
        save_image(frame, '/Users/kenton/Downloads/集群重点研发/蝠鲼数据集/video/test/{}'.format(video_name[:-4]), s)
        # {}前的部分为保存视频的地址
        print('save image:', i)
    success, frame = videoCapture.read()
