#-*- coding=utf-8 -*-
#Huangyao THU
#12-8-2013

class Counter(dict):
  def __getitem__(self,idx):
    self.setdefault(idx,0)
    return dict.__getitem__(self,idx)
  def argMax(self):
    if len(self.keys())==0:return None
    all=self.items()
    values=[x[1] for x in all]
    maxIndex=values.index(max(values))
    return all[maxIndex][0]
  def sortedKeys(self):
    sortedItems=self.items()
    compare=lambda x,y: sign(y[1]-x[1])
    sortedItems.sort(cmp=compare)
    return [x[0] for x in sortedItems]

  def totalCount(self):
    """
    return the sum of counts for all keys
    """
    return sum(self.values())
  def copy(self):
    return Counter(dict.copy(self))
  def __mul__(self,y):
    sum=0
    x=self
    if len(x)>len(y):
        x,y=y,x
    for key in x:
        if key not in y:
            continue
        sum+=x[key]*y[key]
    return sum
  def __radd__(self,y):
    for key,value in y.items():
        self[key]+=value

  def __add__(self,y):
    """
    add two counters gives a counter with the union of all counts
    c=a+b
    """
    addend=Counter()
    for key in self:
        if key in y:
            addend[key]=self[key]+y[key]
        else:
            addend[key]=self[key]
    for key in y:
        if key in self:
            continue
        addend[key]=y[key]
    return addend
  def incrementAll(self,count):
    """
    Increaments all elements of keys by the same count
    """
    for item in self:
        self[item]+=count
  def divideAll(self,divisor):
    """
    divide all counts by divisor
    """
    divisor=float(divisor)
    for key in self:
        self[key]/=divisor
  def normalize(self):
    """
    all keys sums to 1
    """
    total=float(self.totalCount())
    if total==0:return
    for key in self.keys():
        self[key]=self[key]/total
