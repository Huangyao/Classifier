# -*- coding=utf-8 -*-
#THU
#12-27-2013

import numpy as np
import matplotlib.pyplot as plt

def plotR():
    n_groups=4

    SVM=(76.7,87.2,89.8,86.1)

    Bayes=(72.6,90.3,93.0,92.3)

    #C=('b','y','r','g')
    fig,ax=plt.subplots()
    index=np.arange(n_groups)
    bar_width=0.3
    opacity=0.4
    #eror_config={'ecolor':'0.3'}
    rects1=plt.bar(index,SVM,bar_width,alpha=opacity,color='r',label='SVM')
    rects2=plt.bar(index+bar_width,Bayes,bar_width,alpha=opacity,color='g',label='Bayes')
    plt.xlabel('Label')
    plt.ylabel('Accuracy / ( % )')
    plt.title('Predict Accuracy Plot')
    plt.xticks(index+bar_width,('Label1','Label2','Label3','Label4'))
    plt.legend()

    plt.tight_layout()
    plt.show()
    #plt.savefig('SVM-Bayes.jpg')

