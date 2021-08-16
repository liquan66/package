# coding=utf-8
import os
import io


def alter():
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = "<name>1</name>"
    new_str = "<name>small-vehicle</name>"
    file = r'F:/code/DOTA_devkit-master/rain_xml/'
    old_str= ""
    with io.open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with io.open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


# 获取目录下的文件
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return (files)


# 获取后缀名
def file_extension(file):
    return os.path.splitext(file)[1]


file_dir = './'
file_list = file_name(file_dir)

for i in file_list:
    if file_extension(i) == ".ctl":
        alter(i, 'ZHS16GBK', 'AL32UTF8')
