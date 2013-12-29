# coding=utf-8

from pymmseg import mmseg
import os
import sys

"""
读取一个文件，将其转换为一个字典
"""
def fileToDict(file):
    if(os.path.isfile(file)):
        mmseg.dict_load_defaults()
        Dict={}
        f=open(file,'r')
        for item in f.readlines():
            alg=mmseg.Algorithm(item)
            for tok in alg:
                if tok.text not in Dict:
                    Dict[tok.text]=1
                else:
                    Dict[tok.text]+=1
        return Dict
    else:
        print "Eror:<segment.py->fileToDict()> File not found"

def HY_pymmseg(file1,file2):
    if(os.path.isfile(file1)):
        mmseg.dict_load_defaults()
        Dict={}
        f1=open(file1,'r')
        f2=open(file2,'w')
        for item in f1.readlines():
            alg=mmseg.Algorithm(item)
            wordlist=[]
            for tok in alg:
                wordlist.append(tok.text+"//")
                print "tok.text",tok.text
                if tok.text not in Dict:
                    Dict[tok.text]=1
                else:
                    Dict[tok.text]+=1
                    
            f2.writelines(wordlist)
        f1.close
        f2.close()
        print "HY_pymmseg FINISHED"
        """
        for item in Dict:
            print "DICT"
            print item
            print Dict[item]
        """
    else:
        print "EROR:HY_pymmseg eror"
def codeTransfer(file1,file2):
    f1=open(file1)
    text1=f1.read()
    f1.close()
    u1=text1.decode('gbk')
    f2=open(file2,'w')
    text2=u1.encode('utf-8')
    f2.write(text2)
    f2.close()
