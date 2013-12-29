# -*- coding = utf-8 -*-
#Huangyao THU
#12-14 2013

import util
import featureSelected
import json
import pickle

def saveWordTextDict(label,fileNum):
    str1=('../data/trainData/Dict/%d.txt') % label
    str2=('../data/trainData/Dict/words%d.txt') %label
    f1=open(str1,'rb')
    Dict=pickle.load(f1)
    f1.close()
    wordDict=util.Counter()
    for item in Dict.items():
        wordDict[item]=0
    for item in Dict.items():
        print 'item',item
        for i in range(fileNum):
            tmp=featureSelected.featureDict(label,i)
            if item in tmp:
                wordDict[item]+=1
    print "saveWordTextDict has finished!"
    f2=open(str2,'wb')
    pickle.dump(wordDict,f2)
    f2.close()


if __name__=='__main__':
    saveWordTextDict(1,500)
    #saveWordTextDict(2,500)
    #saveWordTextDict(3,500)
    #saveWordTextDict(4,500)




