#-*- coding=utf-8 -*-
#THU
#12-20-2013

import featureSelected
import pickle
import json
import util
import math

#class Bayes_Classifier(self):

def Bayes_load_Features():
    str=('/Thu_Life/CS/SVM/data/trainData/Dict/Chi_Feature.txt')
    f=open(str,'rb')
    feature=pickle.load(f)
        #print json.dumps(feature,encoding='UTF-8',ensure_ascii=False)
    Dict=[]
    for item in feature:
        Dict.append(item[0])
    #print json.dumps(Dict,encoding='UTF-8',ensure_ascii=False)
    #print "len of dict",len(Dict)
    return Dict
def Bayes_FeatureP():
    Dict_P=[]
    for i in range(4):
        label=i+1
        tmp=util.Counter()
        str=('/Thu_Life/CS/SVM/data/trainData/Dict/Chi_%d.txt') % label
        f=open(str,'rb')
        dict_tmp=pickle.load(f)
        f.close()
        DICT=Bayes_load_Features()
        for item in DICT:
            if item in dict_tmp:
                tmp[item]=dict_tmp[item]
            else:
                tmp[item]=0
        #print tmp
        tmp.incrementAll(1)
        tmp.normalize()
        #print json.dumps(tmp,encoding='UTF-8',ensure_ascii=False)
        Dict_P.append(tmp)
    return Dict_P
def calculateLogJointProbabilities(data):
    logJoint=[]
    PDict=Bayes_FeatureP()
    for i in range(4):
        label=i+1
        value=0
        for item in data:
            t=PDict[i][item]
            if t!=0:
                value+=data[item]*math.log(t)
        logJoint.append(value)

    return logJoint
def getLabel(data):
    logJoint=calculateLogJointProbabilities(data)
    count=0
    tmp=logJoint[0]
    for i in range(len(logJoint)):
        if logJoint[i]>tmp:
            tmp=logJoint[i]
            count=i
    label=count+1
    #print 'label',label
    #print 'logJoint',logJoint
    return label
def classify(filename):
    textData=featureSelected.featureSelect(filename)
    label=getLabel(textData)
    #print 'classify',label
    if label==1:
        print "类别：财经"
        return '财经'
    elif label==2:
        print "类别:IT"
        return 'IT'
    elif label==3:
        print "类别：旅游"
        return '旅游'
    elif label==4:
        print "类别：体育"
        return '体育'
def classify2(filename):
    textData=featureSelected.featureSelect(filename)
    label=getLabel(textData)
    return label
    
    
if __name__=='__main__':
    #Bayes_FeatureP()
    filename=('/Thu_Life/CS/SVM/data/trainData/Data/class2/1246.txt')
    classify(filename)
    text=featureSelected.featureSelect(filename)
    #print json.dumps(text,encoding='UTF-8',ensure_ascii=False)
