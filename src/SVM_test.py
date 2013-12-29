# -*- coding= utf-8 -*-
#THU
#12-17-2013

import VSM
import pickle

def saveSVMTestFile(label,fileName1,fileName2):
    f=open(fileName2,'wb')
    slabel=('%d ') % label
    t=VSM.TextToVector(fileName1)
    if len(t)>0:
        f.write(slabel)
        for k in range(len(t)):
            str=('%d:%d ') % (t[k][0],t[k][1])
            f.write(str)
        f.write('\r\n')
    f.close()
if __name__=='__main__':
    label=2
    fileName1=('../data/trainData/Data/class%d/1234.txt') % label
    fileName2=('../data/trainData/SVMFile/SVM_test')
    saveSVMTestFile(label,fileName1,fileName2)
