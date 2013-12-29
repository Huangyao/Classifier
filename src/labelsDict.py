#-*- coding = utf-8 -*-
#Huangyao THU
#12-08-2013

"""

"""
import util
import featureSelected
import json

def LabelDicts(labelNum,fileNum,featureNum):
    t=util.Counter()
    for i in range(fileNum):
        t+=featureSelected.featureDict(labelNum,i)
        print "%d.txt" %i
    print "legth of dict label",len(t)
    result=sorted(t.items(),key=lambda e:e[1],reverse=True)
    featureDict={}
    for i in range(featureNum):
        featureDict[result[i][0]]=result[i][1]
    print "features are as follows:"
    print json.dumps(featureDict,encoding='UTF-8',ensure_ascii=False)
    return featureDict
def LabelDictsWord(labelNum,fileNum,featureNum):
    t=util.Counter()
    for i in range(fileNum):
        t+=featureSelected.featureDictWord(labelNum,i)
    print 'legth of dictword label',len(t)
    result=sorted(t.items(),key=lambda e:e[1],reverse=True)
    featureDictWord={}
    for i in range(featureNum):
        featureDictWord[result[i][0]]=result[i][1]
    print json.dumps(featureDictWord,encoding='UTF-8',ensure_ascii=False)
    #return featureDictWord
    return t
if __name__=='__main__':
    label=2
    #label=2
    #label=3
    #label=4
    featureDictWord=LabelDictsWord(2,500,50)
    #featureDict=LabelDicts(label,100,20)
    #featureDict=LabelDicts(2,100,20)
    #featureDict=LabelDicts(3,100,20)
    #featureDict=LabelDicts(4,100,20)
    #import pickle
    #f=open('../data/trainData/Dict/'+'%d.txt','wb') % label
    #pickle.dump(featureDict,f)
    #f.close()







