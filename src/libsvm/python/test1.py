# coding=utf-8
#THU huangyao
#12-19-2013
import os,sys
sys.path=[os.path.dirname(os.path.abspath(__file__))]+sys.path
import svmutil
import svm

y,x=svmutil.svm_read_problem('../thuboy')
#print y
#yy,xx=svmutil.svm_read_problem('../SVMTrainFile250')
m=svmutil.svm_load_model('../SVMTrainFile250.model')
#print m
a,b,c=svmutil.svm_predict(y,x,m)
print a
#print b
#print c
