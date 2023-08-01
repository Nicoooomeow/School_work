from random import seed, shuffle
import sys,time
def generate_permutation(for_seed, length):
    seed(for_seed)
    values = list(range(1, length + 1))
    shuffle(values)
    return values
def maps_to(values, x):
    return values.index(x)+1
def length_of_cycle_containing(values, x):
#     goodD = {value: index for index, value in enumerate(values, start=1)}
#     #定义一个字典，以位置，内容的成对方式存储
#     list.append(x)
#     while x in goodD:
#         x=goodD.pop(x)
#         list.append(x)#将位置存进一个列表
#         leng=len(list)
#     return leng
    count=2
    flag=0
    first=x
    while flag==0:
        if maps_to(values,maps_to(values,x))==first:
            flag+=1
        else:
            count+=1
            x=values.index(x)+1
    return count
def analyse(values):
    length=len(values)
    cycle=[0]*(length+1)
    goodD = {value: index for index, value in enumerate(values, start=1)}
    #定义一个字典，以位置，内容的成对方式存储
    #print(goodD)
    list=[]
    while goodD:#不为空的时候
        content, position = goodD.popitem()#内容和位置
        list.append(position)
        while position in goodD:
            position=goodD.pop(position)
            list.append(position)#将位置存进一个列表
        leng=len(list)
        while list:
            cycle[list.pop(0)]=leng
    return cycle
#     count=1
#     flag=0
#     first=x
#     super=0
#     for i in range(0,long):
#         if super!=0:
#             break
#         elif zero[i][0]!=0:#判断行里是否存过值：存过，
#             if zero[i][zero[i][0]]!=x:#看看是不是算过，没算过
#                 #print('aaa')
#                 continue#换下一行
#             else:#算过，返回数
#                 zero[i][0]+=1
#                 return zero[i][-1]
#         else:#没存过值
#             zero[i][0]=2#我存上啦
#             super=1
#             j=2
#             while flag==0:
#                 position=maps_to(values,x)
#                 if maps_to(values,first)==first:#环数1
#                     flag+=1
#                     zero[i][0]=0
#                 elif maps_to(values,position)==first:#环数2
#                     zero[i][1]=first
#                     zero[i][j]=position
#                     count+=1
#                     zero[i][-1]=count
#                     flag+=1
#                 else:#环数大于2
#                     #print('ddddd')
#                     count+=1
#                     x=values.index(x)+1
# #                     print(x)
#                     zero[i][j]=x
#                     j+=1
#                     zero[i][-1]=count
#                     #print(zero[i][j])
   
# start=time.process_time()
# values=generate_permutation(0,10000)
# # print(values)
# #maps_to(values,1)
# length_of_cycle_containing(values,3)
# #analyse(values)
# end=time.process_time()
# time=end-start
#print(time)
