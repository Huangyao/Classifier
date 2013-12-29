#-*- coding=utf-8 -*-
#12-28-2013


import matplotlib.pyplot as plt
#import matplotlib
#zhfont1 = matplotlib.font_manager.FontProperties(fname='/usr/share/fonts/cjkunifonts-ukai/ukai.ttc')
left=[1,2,3,4]
height=[80,85,95,90]
weight=[0.3,0.3,0.3,0.3]

fig=plt.figure()
plt.xlabel('Label')
plt.ylabel('Data')
plt.title('Predict Accuracy')
#plt.title(u'预测准确率',fontproperties=zhfont1)
ax=fig.add_subplot(111)
rects=ax.bar(left,height,weight,color='#ffff00',linewidth=2)
plt.show()
plt.savefig('bar.jpg')
