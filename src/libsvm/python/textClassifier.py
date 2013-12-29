# -*- coding= utf-8 -*-
#HuangYao THU
#12-19-2013

import VSM
import svmutil

def classify(filename,classLabel=0):
    str=('/Thu_Life/CS/SVM/data/trainData/Test_SVMFile/singleSVM_TestFile')
    f=open(str,'wb')
    t=VSM.TextToVector2(filename)
    slabel=('%d ') % classLabel
    if len(t)>0:
        f.write(slabel)
        for k in range(len(t)):
            str1=('%d:%d ') % (t[k][0],t[k][1])
            f.write(str1)
        f.write('\r\n')
    else:
        print "The text can't be classified to the Four Labels!"
        return "Can't be classified ! "
    f.close()
    y,x=svmutil.svm_read_problem(str)
    model=svmutil.svm_load_model('../SVMTrainFile250.model')
    label,b,c=svmutil.svm_predict(y,x,model)
    print "label",label
    if label[0]==1:
        print "类别：财经"
        return '财经'
    elif label[0]==2:
        print "类别：IT"
        return 'IT'
    elif label[0]==3:
        print "类别:旅游"
        return '旅游'
    elif label[0]==4:
        print "类别：体育"
        return '体育'
def classify2(filename,classLabel=0):
    str=('/Thu_Life/CS/SVM/data/trainData/Test_SVMFile/singleSVM_TestFile')
    f=open(str,'wb')
    t=VSM.TextToVector2(filename)
    slabel=('%d ') % classLabel
    if len(t)>0:
        f.write(slabel)
        for k in range(len(t)):
            str1=('%d:%d ') % (t[k][0],t[k][1])
            f.write(str1)
        f.write('\r\n')
    else:
        return 0
    f.close()
    y,x=svmutil.svm_read_problem(str)
    model=svmutil.svm_load_model('../SVMTrainFile250.model')
    label,b,c=svmutil.svm_predict(y,x,model)
    return label[0]

 
if __name__=='__main__':
    filename=('/Thu_Life/CS/SVM/data/trainData/Data/class4/789.txt')
    classify(filename)


