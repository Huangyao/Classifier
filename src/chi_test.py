# -*- coding=utf-8 -*-
#THU
#12-16-2013

import json
import pickle

def chiFeatureNum(num):
    ChiDict={}
    for i in range(4):
        label=i+1
        str=('../data/trainData/Dict/Chi_%d.txt') % label
        f=open(str,'rb')
        Dict=pickle.load(f)
        f.close()
        sort=sorted(Dict.items(),key=lambda e:e[1],reverse=True)
        for item in range(num):
            ChiDict[sort[item][0]]=sort[item][1]
            #print json.dumps(result,encoding='UTF-8',ensure_ascii=False)
    sort=sorted(ChiDict.items(),key=lambda e:e[1],reverse=True)
    #print json.dumps(sort,encoding='UTF-8',ensure_ascii=False)
    return sort
if __name__=='__main__':
    tmp=chiFeatureNum(50)
    print json.dumps(tmp,encoding='UTF-8',ensure_ascii=False)
    s=('../data/trainData/Dict/Chi_Feature.txt')
    f=open(s,'wb')
    pickle.dump(tmp,f)
    f.close()
