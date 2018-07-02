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

label_list = []
total_num=0
for json_file in files:

    if json_file.endswith('.json'):
        total_num += 1
        json_path= os.path.join(path, json_file)
        print(json_path)
        json_ann = json.load(open(json_path))

        objects = json_ann['objects']
        for item in objects:
            # 打印 label
            # print (item['label'])
            label_list.append(item['label'])
print(label_list)
category = set(label_list)  # myset是另外一个列表，里面的内容是mylist里面的无重复 项

# readme_path =
# with open(path+'readme.txt','w') as f:
with open(os.path.join(path, 'readme'), 'w') as f:
    '''
    保存信息
    '''
    f.write('总json文件数量 = %d'% total_num)
    f.write('\n类别数 = %s' % category)
    for label in category:
        print("the %s has found %d" % (label, label_list.count(label)))
        f.write("\nthe %s has found %d" % (label, label_list.count(label)))

