# _*_ coding:utf-8 _*_
import os
import sys
import cv2
import shutil

src_train = 'filelists/main/'



# 生成train.txt、val.txt
train_class_names = os.listdir(src_train)
#print(train_class_names)
train_class_names_len = len(train_class_names)

# train.txt
with open('filelists/' + 'train.txt', 'w') as w:
    for train_class_name in train_class_names[:int(train_class_names_len * 0.88)]:
        files = os.listdir(src_train + train_class_name)
        #print(files)
        names = []
        for file in files:
            #if file.endswith('.txt'):
            if file.endswith('.mp4'):
                w.write(train_class_name + '/' + file[:-4] + "\n")

# val.txt
with open('filelists/' + 'val.txt', 'w') as w:
    for train_class_name in train_class_names[int(train_class_names_len * 0.88): int(train_class_names_len * 0.9)]:
        files = os.listdir(src_train + train_class_name)
        names = []
        for file in files:
            #if file.endswith('.txt'):
            if file.endswith('.mp4'):
                w.write(train_class_name + '/' + file[:-4] + "\n")









