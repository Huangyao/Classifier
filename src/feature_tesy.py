#-*- coding = utf-8 -*-
#HuangYao THU
#12-9-2013

import featureSelected
import json


labelNum=2
num=450
result=featureSelected.featureDict(labelNum,num)
sort=sorted(result.items(),key=lambda e:e[1],reverse=True)
res=[]
length=200
if len(sort)<200:
    length=len(sort)
for i in range(length):
    res.append((sort[i][0],sort[i][1]))
print 'txt features are as follows:'
print json.dumps(res,encoding='UTF-8',ensure_ascii=False)
    


