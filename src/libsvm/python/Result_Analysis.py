# -*- coding=utf-8 -*-
#THU
#12-27-2013

import os
import textClassifier
import BayesClassify

def evaluateSVM(filename,classlabel,num=800):
    #return true false
    trueLabel=0
    falseLabel=0
    neuLabel=0
    count=0
    fileList=os.listdir(filename)
    if len(fileList)>0:
        for item in fileList:
            if count<num:
                str=filename+item
                tmp=textClassifier.classify2(str)
                count+=1
                print 'count',count
                if tmp==classlabel:
                    trueLabel+=1
                else:
                    if tmp==0:
                        neuLabel+=1
                    else:
                        falseLabel+=1
            else:
                break
    return trueLabel,falseLabel,neuLabel
def evaluateBayes(filename,classlabel,num=800):
    trueLabel=0
    falseLabel=0
    count=0
    fileList=os.listdir(filename)
    if len(fileList)>0:
        for item in fileList:
            if count<num:
                str=filename+item
                tmp=BayesClassify.classify2(str)
                count+=1
                print 'count',count
                if tmp==classlabel:
                    trueLabel+=1
                else:
                    falseLabel+=1
            else:
                break
    return trueLabel,falseLabel

if __name__=='__main__':
    filename='/Thu_Life/CS/SVM/data/trainData/Data/class4/'
    #t,f,n=evaluateSVM(filename,4)
    #print t
    #print f
    #print n
    t,f=evaluateBayes(filename,4)
    print t
    print f
                


    
