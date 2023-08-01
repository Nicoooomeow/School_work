class CircularList:
    def __init__(self,*args):#args元组类型参数，kwargs字典类型参数
        # print(args)
        self.items=[item for item in args]
    def __len__(self):
        return len(self.items)
    def __str__(self):
        result=[str(item) for item in self.items]
        result="["+", ".join(result)+"]"
        return result
    def __setitem__(self,key,value):
        if self.items:
            self.items[key%len(self.items)]=value
    def __getitem__(self,item):
        if self.items:
            if isinstance(item,int):#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
                                    # isinstance() 与 type() 区别：
                                    # type() 不会认为子类是一种父类类型，不考虑继承关系。
                                    # isinstance() 会认为子类是一种父类类型，考虑继承关系。
                                    # 如果要判断两个类型是否相同推荐使用 isinstance()。
                return self.items[item%len(self.items)]
            else:
                L=[]
                result=[]
                start,stop,step=item.start,item.stop,item.step
                if step is None:#步长为空的情况
                    step=1
                if step==0:#异常的情况
                    raise ValueError("slice step cannot be zero")
                if start is None:#开始为空的情况
                    if step>0:
                        start=0
                    else:
                        start=-1
                if stop is None:#结束为空的情况
                    if step>0:
                        stop=len(self.items)
                    if step<0:
                        stop=-len(self.items)-1
                if start-stop>0 and step>0:
                    return result
                if start-stop<0 and step<0:
                    return result
                while start<0 or stop<0:
                    start+=len(self.items)
                    stop+=len(self.items)
                while len(L)<max(start,stop):
                    L.extend(self.items)
                if stop-start==1 or stop-start==-1:
                    while start>len(L)-1:
                        start-=len(L)
                    result.append(L[start])
                    return result
                return L[start:stop:step]
    # REPLACE PASS ABOVE WITH YOUR CODE
# L = CircularList(*range(10, 20))
# L[:0:-1]
