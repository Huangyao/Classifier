#-*- coding=utf-8  -*-
#HuangYao THU
#12-19-2013

import wx
import textClassifier
import BayesClassify
import resultPlot

#app=wx.App(False)
class myFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='Chinese Text Classifier',size=(410,340))
        self.open_button=wx.Button(self,label='Filename',pos=(5,5),size=(80,25))
        self.text1=wx.TextCtrl(self,pos=(90,5),size=(300,25))
        self.class_button=wx.Button(self,label='SVM',pos=(5,80),size=(80,25))
        #2013-12-23
        self.baye_button=wx.Button(self,label='Bayes',pos=(200,80),size=(80,25))
        ##
        self.result_button=wx.Button(self,label='Result',pos=(5,160),size=(80,25))
        self.ansys_button=wx.Button(self,label='Ansys',pos=(200,160),size=(80,25))

        self.text2=wx.TextCtrl(self,pos=(5,190),size=(400,120),style=wx.TE_MULTILINE)
        self.Bind(wx.EVT_BUTTON,self.Click_Class_Button,self.class_button) 
        self.Bind(wx.EVT_BUTTON,self.Click_Result_Button,self.result_button)
        self.Bind(wx.EVT_TEXT_ENTER,self.OnText1,self.text1)
        #12-23
        self.Bind(wx.EVT_BUTTON,self.Click_Bayes_Button,self.baye_button)
        self.Bind(wx.EVT_BUTTON,self.Click_Ansys_Button,self.ansys_button)
    def Click_Ansys_Button(self,event):
        resultPlot.plotR()
    def Click_Bayes_Button(self,event):
        self.filename='/Thu_Life/CS/SVM/data/trainData/Data/'+self.text1.GetValue()
        self.result=BayesClassify.classify(self.filename)
        print 'Bayes result:',self.result
    def Click_Class_Button(self,event):
        #print "open"
        self.filename='/Thu_Life/CS/SVM/data/trainData/Data/'+self.text1.GetValue()
        #print "self.filename",self.filename
        self.result=textClassifier.classify(self.filename)
        print 'SVM result',self.result
    def Click_Result_Button(self,event):
        print "result"
        #result=textClassifier.classify(self.filename)
        self.text2.SetValue(self.result)
        #print 'result',result
    def OnText1(self,event):
        self.text1.SetValue()
    
if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=myFrame(parent=None,id=-1)
    frame.Show(True)
    app.MainLoop()
