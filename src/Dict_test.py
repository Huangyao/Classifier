#coding=utf-8
#THU
#12-12-2013

import json
import pickle

label=2

str=('../data/trainData/Dict/%d.txt') % label
f=open(str,'rb')
load=pickle.load(f)
f.close()

load=sorted(load.items(),key=lambda e:e[1],reverse=True)
print "DICT: ", label
print json.dumps(load,encoding='UTF-8',ensure_ascii=False)
