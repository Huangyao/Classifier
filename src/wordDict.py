# -*- coding=utf-8 -*-
#Huangyao THU
#12-15-2013

import json
import pickle

def wordNums(label,word):
    str=('../data/trainData/Dict/words%d.txt') % label
    f=open(str,'rb')
    Dict=pickle.load(f)
    f.close()
    #print "wordsDict has loaded!"
    #print json.dumps(Dict,encoding='UTF-8',ensure_ascii=False)
    if word in Dict:
        #print "word in Dict"
        return Dict[word]
    else:
        #print "word not in Dict"
        return 0

if __name__=='__main__':
    label=3
    str1=('../data/trainData/Dict/%d.txt') % label
    f1=open(str1,'rb')
    Dict2=pickle.load(f1)
    f1.close()
  #  print json.dumps(Dict2,encoding='UTF-8',ensure_ascii=False)
    
    for word in Dict2.items():
        print "word: ",word[0]
        tmp=wordNums(label,word[0])
        t=(word,tmp)
        print json.dumps(t,encoding='UTF-8',ensure_ascii=False)
    
    #tmp=wordNums(label,'谈判')
    #print 'numsof tmp',tmp
