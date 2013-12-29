#coding=utf-8

import svmutil
y,x=svmutil.svm_read_problem('../thuboy')
m=svmutil.svm_load_model('../SVMTrain250.model')
#m=svmutil.svm_train(y,x,'-c 5')
p1,p2,p3=svmutil.svm_predict(y,x,m)
print p1
print p2
print p3
