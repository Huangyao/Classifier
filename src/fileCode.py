#-*- coding=utf-8 -*-
# Huangyao THU
#12-8-2013

"""
将GBK编码转换为UTF
"""

import os
import segment

def fileTransfer(file1,file2):
    fileList=os.listdir(file1)
    count=0
    if(len(fileList)>1):
        for item in fileList:
            str1=file1+'/'+item
            str2=(file2+'/'+'%d.txt') % count
            print "str1 item",item
            segment.codeTransfer(str1,str2)
            count+=1
        print "fileTransfer has finished!"
        print "count=",count
    else:
        print "Eror:trainFile too little"

        
if __name__=='__main__':
    #fileTransfer('../data/trainData/origin_Data/class1','../data/trainData/Data/class1')
    #fileTransfer('../data/trainData/origin_Data/class2','../data/trainData/Data/class2')
    #fileTransfer('../data/trainData/origin_Data/class3','../data/trainData/Data/class3')
    fileTransfer('../data/trainData/origin_Data/class4','../data/trainData/Data/class4')
    
