#coding=utf-8
import segment
import json

"""
test def file to dict

"""
d={}
d=segment.fileToDict('../data/test.txt')
#for item in d:
 #   print type(item)
  #  print item,d[item]
print json.dumps(d,encoding='UTF-8',ensure_ascii=False)
