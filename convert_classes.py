# -*- coding: utf-8 -*-
# 将 json格式的 class进行统一标签
#可以直接批量读取json文件，并修改内容
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import h5py
import json
import os
import scipy.misc
import sys



def parse_args():
    parser = argparse.ArgumentParser(description='Convert dataset')
    parser.add_argument(
        '--dataset', help="cocostuff, cityscapes", default='cityscapes_instance_only', type=str)
    parser.add_argument(
        '--outdir', help="output dir for json files", default='/home/shining/Projects/datasets/Xray', type=str)
    parser.add_argument(
        '--datadir', help="data dir for annotations to be converted",
        default='/home/shining/Projects/datasets/Xray', type=str)
    # if len(sys.argv) == 1:
    #     parser.print_help()
    #     sys.exit(1)
    return parser.parse_args()


# for Cityscapes
def getLabelID(self, instID):
    if (instID < 1000):
        return instID
    else:
        return int(instID / 1000)



def convert_cityscapes_instance_only(
        data_dir, out_dir):
    """Convert from cityscapes format to COCO instance seg format - polygons"""

    ann_dirs = [
         #'gtFine/val',
         'gtFine/train',
         #'gtFine/test',

        # 'gtCoarse/train',
        # 'gtCoarse/train_extra',
        # 'gtCoarse/val'
    ]

    ends_in = '%s_polygons.json'
    img_id = 0
    ann_id = 0
    cat_id = 0
    #这里说明：  category 映射表
    category_dict = {
        #'name':id
        'pz' : 'bottle',
        'xj': 'camera',
        'dc': 'battery',
        'gj': 'tools',
        'pa': 'pad',
        'sb': 'watch',
        'sj': 'cellphone',
        'Knife':'knife'
        }

    for ann_dir in  ann_dirs:
        ann_dict = {}
        images = []
        annotations = []
        ann_dir = os.path.join(data_dir, ann_dir)
        for root, dirnames, files in os.walk(ann_dir):
            for filename in files:                
                if filename.endswith('.json'):
                    if len(images) % 50 == 0:
                        print("Processed %s images, %s annotations" % (
                            len(images), len(annotations)))
                    json_ann = json.load(open(os.path.join(root, filename)))
                    
                    objects = json_ann['objects']
                    for item in objects:
                         #替换 label
                         if item['label'] in category_dict.keys():
                             item['label'] = category_dict[item['label']]
                             print(filename)
                    djson = {"imgHeight": json_ann['imgHeight'],
                    "imgWidth": json_ann['imgWidth'],
                    "objects": objects
                    }        
                    # save Json 

                    jsPath = os.path.join(root, filename)
                    # jsPath = os.path.join(root, filename)

                    with open(jsPath,"w") as f:
                        json.dump(djson,f, sort_keys=True, indent=4)
                    print("%s saved."%jsPath)                    



if __name__ == '__main__':
    args = parse_args()
    convert_cityscapes_instance_only(args.datadir, args.outdir)
    
