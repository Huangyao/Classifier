# -*- coding=utf-8 -*-
#THU
#12-16-2013

import json
import pickle
import featureSelected

def TextToVector(filename):
    text=featureSelected.featureSelect(filename)
    #print json.dumps(text,encoding='UTF-8',ensure_ascii=False)
    f=open('../data/trainData/Dict/Chi_Feature.txt','rb')
    Dict=pickle.load(f)
    f.close()
    #print json.dumps(Dict,encoding='UTF-8',ensure_ascii=False)
    DICT=[]
    for i in range(len(Dict)):
        DICT.append(Dict[i][0])
    tmp=[]
    print "lenth of DICT ",len(DICT)
    for i in range(len(DICT)):
        if DICT[i] in text:
            tmp.append((i+1,text[DICT[i]]))
    if len(tmp)==0:
        print "len of tmp in VSM = 0"
    return tmp
if __name__=='__main__':
    str=('../data/trainData/Data/class4/938.txt')
    t=TextToVector(str)
    print json.dumps(t,encoding='UTF-8',ensure_ascii=False)
