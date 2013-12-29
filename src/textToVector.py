#-*- coding=utf-8 -*-
#Huangyao THU
#12-11-2013

import featureSelected
import util
import json
import pickle


CONSTDICT=['的','了','啊','呀','嘛','。','，',' ','、']
def fileToDict(labelNum=2,num=765):
    result=featureSelected.featureDict(labelNum,num)
    sort=sorted(result.items(),key=lambda e:e[1],reverse=True)
    print "文本单词提取"
    print json.dumps(sort,encoding='UTF-8',ensure_ascii=False)
    
    str=('../data/trainData/Dict/%d.txt')   % labelNum
    f=open(str,'rb')
    DICT=pickle.load(f)
    f.close()
    print "字典："
    print json.dumps(DICT,encoding='UTF-8',ensure_ascii=False)

    return sort
def fileToVector(labelNum=2,num=765):
    result=featureSelected.featureDict(labelNum,num)
    vector=[]
    str=('../data/trainData/Dict/%d.txt') % labelNum
    f=open(str,'rb')
    loadDict=pickle.load(f)
    f.close()
    
    loadDict=sorted(loadDict.items(),key=lambda e:e[1],reverse=True)
    for item in loadDict:
        if item[0] in result:
            vector.append(result[item[0]])
        else:
            vector.append(0)
    print "文本向量化已经完成"
    print vector
    #print json.dumps(vector,encoding='UTF-8',ensure_ascii=False)

if __name__=='__main__':
    #fileToDict(4,888)
    for i in range(10):
        fileToVector(1,i)

