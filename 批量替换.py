# import sys
# import os
# from sys import argv
#
# file_name = argv[1]
#
# path = 'F:/code/DATA\planeCar/labelTxt-v1.5/'
# for file in os.listdir(file_name):
#     dir_entry_path = os.path.join(path, file);
#     print(dir_entry_path)
#     f = open(dir_entry_path, 'r')
#     rc = f.read().replace('car', 'small-vehicle')
#     f.close()
#     t = open(dir_entry_path, 'w')
#     t.write(rc)
#     t.close()
"""
xmls = glob.glob('F:/code/yolov3_spp/yolov3_spp/my_yolo_dataset/trainsplit/labels/*.txt')

# xmls = glob.glob('F:/code/DATA\planeCar/labelTxt-v1.5/*.xml')
可以实现txt或者xml两种文件，进行字符的批量替换
"""

__author__ = 'ShawDa'


import glob
xmls = glob.glob('F:/code/yolov3_spp/yolov3_spp_DOTA版本/my_yolo_dataset/trainsplit\labels/*.txt')

# xmls = glob.glob('F:/code/DATA\planeCar/labelTxt-v1.5/*.xml')
for one_xml in xmls:
    print(one_xml)
    f = open(one_xml, 'r+', encoding='utf-8')
    all_the_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_the_lines:
        # line = line.replace('car', 'small-vehicle')
        line = line.replace('large-vehicle', 'car ')
        f.write(line)
    f.close()
