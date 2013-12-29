# -*- coding=utf-8 -*-
#THU
#12-16-2013

import wordDict
import pickle

def ChiFeatures():
    """
    str1=('../data/trainData/Dict/1.txt')
    f1=open(str1,'rb')
    Dict1=pickle.load(f1)
    #
    f1.close()
    Chi_Dict1={}
    count=0
    for word in Dict1:
        A=wordDict.wordNums(1,word)
        B1=wordDict.wordNums(2,word)
        B2=wordDict.wordNums(3,word)
        B3=wordDict.wordNums(4,word)
        B=B1+B2+B3
        D=1500-B
        tmp=Chi(A,B,C,D,2000)
        print "tmp",tmp
        print "count",count
        count+=1
        Chi_Dict1[word]=tmp
    str11=('../data/trainData/Dict/Chi_1.txt')
    f11=open(str11,'wb')
    pickle.dump(Chi_Dict1,f11)
    f11.close()
    """
    """
    str2=('../data/trainData/Dict/2.txt')
    f2=open(str2,'rb')
    Dict2=pickle.load(f2)
    f2.close()
    Chi_Dict2={}
    count=0
    for word in Dict2:
        A=wordDict.wordNums(2,word)
        B1=wordDict.wordNums(1,word)
        B2=wordDict.wordNums(3,word)
        B3=wordDict.wordNums(4,word)
        B=B1+B2+B3
        C=500-A
        D=1500-B
        tmp=Chi(A,B,C,D,2000)
        print "tmp",tmp
        print "count",count
        count+=1
        Chi_Dict2[word]=tmp
    str22=('../data/trainData/Dict/Chi_2.txt')
    f22=open(str22,'wb')
    pickle.dump(Chi_Dict2,f22)
    f22.close()
    """
    """
    str3=('../data/trainData/Dict/3.txt')
    f3=open(str3,'rb')
    Dict3=pickle.load(f3)
    f3.close()
    Chi_Dict3={}
    count=0
    for word in Dict3:
        A=wordDict.wordNums(3,word)
        B1=wordDict.wordNums(1,word)
        B2=wordDict.wordNums(2,word)
        B3=wordDict.wordNums(4,word)
        B=B1+B2+B3
        C=500-A
        D=1500-B
        tmp=Chi(A,B,C,D,2000)
        print "tmp",tmp
        print "count",count
        count+=1
        Chi_Dict3[word]=tmp
    str33=('../data/trainData/Dict/Chi_3.txt')
    f33=open(str33,'wb')
    pickle.dump(Chi_Dict3,f33)
    f33.close()
    """
    str4=('../data/trainData/Dict/4.txt')
    f4=open(str4,'rb')
    Dict4=pickle.load(f4)
    f4.close()
    Chi_Dict4={}
    count=0
    for word in Dict4:
        A=wordDict.wordNums(4,word)
        B1=wordDict.wordNums(1,word)
        B2=wordDict.wordNums(2,word)
        B3=wordDict.wordNums(3,word)
        B=B1+B2+B3
        C=500-A
        D=1500-B
        tmp=Chi(A,B,C,D,2000)
        print "tmp",tmp
        print "count",count
        count+=1
        Chi_Dict4[word]=tmp
    str44=('../data/trainData/Dict/Chi_4.txt')
    f44=open(str44,'wb')
    pickle.dump(Chi_Dict4,f44)
    f44.close()

def Chi(A,B,C,D,N):
    result=(N*(A*D-B*C)*(A*D-B*C))/((A+C)*(A+B)*(B+D)*(C+D)+1)
    return result

    
if __name__=='__main__':
    #ChiFeatures()
