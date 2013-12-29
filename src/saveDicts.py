# coding=utf-8
#Huangyao THU
#12-9-2013

import pickle
import labelsDict
import json

def saveDict(label,fileNum,featureNum):
    featureDict=labelsDict.LabelDicts(label,fileNum,featureNum)
    str=('../data/trainData/Dict/%d.txt') % label
    f=open(str,'wb')
    pickle.dump(featureDict,f)
    f.close()
def saveDictWord(label,fileNum):
    featureDictWord=labelsDict.LabelDictsWord(label,fileNum,50)
    str=('../data/trainData/Dict/words%d.txt') %label
    f=open(str,'wb')
    pickle.dump(featureDictWord,f)
    f.close()

if __name__=='__main__':
   # saveDict(1,500,1000)
   # saveDictWord(1,500)
   # saveDict(2,500,1000)
    #saveDictWord(2,500)
 #    saveDict(3,500,1000)
   # saveDictWord(3,500)
    #saveDict(4,500,1000)
  #  saveDictWord(4,500)
"""    
label=4
featureDict=labelsDict.LabelDicts(label,600,200)
#print featurieDict
str=('../data/trainData/Dict/%d.txt') % label
f=open(str,'wb') 
pickle.dump(featureDict,f)
f.close()

#test
f2=open(str,'rb')
load=pickle.load(f2)
f2.close()
#print load
print json.dumps(load,encoding='UTF-8',ensure_ascii=False)
"""
