#-*- coding=utf-8 -*-
#Hangyao THU
#12-08-2013

"""
选择文本的特征值
"""
import util
import segment
import json

CONSTDICT=['的','了','啊','呀','嘛','。','，',' ','、','我们','他们','一个','可以','这个','主要','但是','如果','对于','那么','而且','都是','以及','不过','还有','一些','个人','正在','没有','因此','更多','目前','已经','非常','其中','同时','由于','这些','这一','因为','就是']


def featureDict(labelNum,num):
    str=('../data/trainData/Data/class%d/'+'%d.txt') % (labelNum,num)
    Dict={}
    counter=util.Counter()
    Dict=segment.fileToDict(str)
    for item in Dict.keys():
        if item in CONSTDICT or len(item)<6:
            del(Dict[item])
        else:
            counter[item]=Dict[item]
    #print
    
    sort=sorted(Dict.items(),key=lambda e:e[1],reverse=True)
    #print json.dumps(sort,encoding='UTF-8',ensure_ascii=False)
    #print "length of sort",len(sort)
    return counter
def featureSelect(filenum):
    Dict={}
    counter=util.Counter()
    Dict=segment.fileToDict(filenum)
    for item in Dict.keys():
        if item in CONSTDICT or len(item)<6:
            del(Dict[item])
        else:
            counter[item]=Dict[item]
    return counter
def featureDictWord(labelNum,num):
    str=('../data/trainData/Data/class%d/'+'%d.txt') % (labelNum,num)
    print ("%d.txt") % num
    Dict={}
    counter=util.Counter()
    Dict=segment.fileToDict(str)
    for item in Dict.keys():
        if item in CONSTDICT or len(item)<6:
            del(Dict[item])
        else:
            counter[item]=1
    #print "featureSelected featureDictWord has finished!"
    return counter

def labelDict(fileNum,featureNum):
    t=util.Counter()
    for i in range(fileNum):
        t+=featureDict(i)
    result=sorted(t.items(),key=lambda e:e[1],reverse=True)
    featureDict={}
    for i in range(featureNum):
        featureDict[result[i][0]]=result[i][1]
    print "features are as follows: "
    print json.dumps(featureDict,encoding='UTF-8',ensure_ascii=False)

if __name__=='__main__':
    #labelDict(600,200)

    
    t=util.Counter()
    for i in range(500):
        print "features dict",i
        t+=featureDict(i)
    print "length of dict",len(t)
    result=sorted(t.items(),key=lambda e:e[1],reverse=True)
    #print json.dumps(result,encoding='UTF-8',ensure_ascii=False)
    featureDict={}
    for i in range(100):
        featureDict[result[i][0]]=result[i][1]
    print "features are as follows"
    print json.dumps(featureDict,encoding='UTF-8',ensure_ascii=False)

