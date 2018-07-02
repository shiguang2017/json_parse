# -*- coding: utf-8 -*-
# 将 json格式的 class进行统一标签
# 可以直接批量读取json文件，并修改内容
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os
import scipy.misc
import sys



path = "/home/xionglin/345G/PycharmProject/Mask_data_manage/images"


files = os.listdir(path)
# fs2 = os.listdir(path2)
#
# for  in fs1:
#     print
#     imagefolder
#     new_folder = os.path.join(dst_path, imagefolder)
#     print
#     new_folder
#     if not os.path.exists(new_folder):
#         os.mkdir(new_folder)
#
#     path2 = os.path.join(path1, imagefolder)


for json_file in files:
    if json_file.endswith('.json'):
        json_path= os.path.join(path, json_file)
        json_ann = json.load(open(json_path))

        objects = json_ann['objects']
        for item in objects:
            # 打印 label
             print (item['label'])
