#i*- coding=utf-8 -*-
#THU
#12-16-2013

import VSM
import pickle

def saveSVMTrainFile(label,FileNum):
    #class 1 label=1
    f=open('../data/trainData/SVMFile/SVMTrainFile.txt','a')
    slabel=('%d ') %label
    #f.write(slabel) 
    #f.write(' ')
    for i in range(FileNum):
        s=('../data/trainData/Data/class%d/%d.txt') % (label,i)
        print "text i",i
        #f.write(slabel)
        t=VSM.TextToVector(s)
        if len(t)>0:
            f.write(slabel)
            for k in range(len(t)):
                str=('%d:%d ') % (t[k][0],t[k][1])
                f.write(str)
            f.write('\r\n')
    #f.write('end')
    f.close()
def saveSVMTestFile():
    
def saveSVM(FileNum):
    for i in range(4):
        label=i+1
        saveSVMTrainFile(label,FileNum)
    print "saveSVMTrainFile has finished!"
if __name__=='__main__':
    #saveSVM(250)
