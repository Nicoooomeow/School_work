from random import randint,seed
def play():
    dic={0:'Ace',1:'King',2:'Queen',3:'Jack',4:'10',5:'9'}
    dic2={'Ace':0,'King':1,'Queen':2,'Jack':3,'10':4,'9':5}
    poke=[]
    stay=[]
    ini=[]
    flag=1#1，留下的不存在 2，留下的继续或全部留下跳出 0 继续下一轮 3全不要
    for i in range(5):
        ini.append(randint(0,5))
    ini=sorted(ini)
    for i in range(5):
        poke.append(dic[ini[i]])
    for j in range(2):
        print("The roll is: ",end="")
        print(*poke)
        get_result(poke)
        flag=1
        while flag==1:#让用户进行保留
            copy=[]#防止不是全等
            for i in range(len(poke)):
                copy.append(poke[i])
            string=""
            if j==0:
                string=input("Which dice do you want to keep for the second roll? ")
            if j==1:
                string=input("Which dice do you want to keep for the third roll? ")
            stay=string.split(" ")
            if stay[0]=="All" or stay[0]=="all":#结束了的情况
                print("Ok, done.")
                flag=2
                break
            flag=0
            if stay==['']:#全放弃的情况
                flag=3
                break
            for i in range(len(stay)):#检测留下的不存在的情况
                if stay[i] not in poke:
                    print("That is not possible, try again!")
                    flag=1
                    break
                else:
                    copy.remove(stay[i])
            if len(stay)==5:
                print("Ok, done.")
                flag=2
                break
        if flag==2:
            break
        poke=[]
        ini=[]
        if flag==3:
            length=0
            if j==1:
                flag=0
        else:
            length=len(stay)
        for k in range(length):
            ini.append(dic2[stay[k]])
        for i in range(5-length):
            ini.append(randint(0,5))
        ini=sorted(ini)
        for i in range(5):
            poke.append(dic[ini[i]])
    if flag==0:
        print("The roll is: ",end="")
        print(*poke)
        get_result(poke)
def get_result(poke):
    lis=set(poke)
    a=len(lis)
    if a==5:
        if '9' not in lis or 'Ace'not in lis:
            print("It is a Straight")
        else:
            print("It is a Bust")
    elif a==4:
        print("It is a One pair")
    elif a==1:
        print("It is a Five of a kind")
    elif a==2:
        if max(poke.count(lis.pop()),poke.count(lis.pop()))==4:
            print("It is a Four of a kind")
        else:
            print("It is a Full house")
    else:
        get_max=[]
        while lis:
            get_max.append(poke.count(lis.pop()))
        if max(get_max)==3:
            print("It is a Three of a kind")
        else:
            print("It is a Two pair")
            
def simulate(n):
    count=[0]*7#记录每个都多少次
    for i in range(n):
        poke=[]#苦逼的数字
        for j in range(5):
            poke.append(randint(0,5))
        lis=set(poke)
        a=len(lis)
        if a==5:
            if 5 not in lis or 0 not in lis:#Straight
                count[3]+=1
            else:
                continue
        elif a==4:#One pair
            count[6]+=1
        elif a==1:#Five of a kind
            count[0]+=1
        elif a==2:
            if max(poke.count(lis.pop()),poke.count(lis.pop()))==4:#Four of a kind
                count[1]+=1
            else:#Full house
                count[2]+=1
        else:
            get_max=[]
            while lis:
                get_max.append(poke.count(lis.pop()))
            if max(get_max)==3:#Three of a kind
                count[4]+=1
            elif max(get_max)==2:#Two pair
                count[5]+=1
    print("Five of a kind : "+"%.2f" % (count[0]/n*100)+"%" )
    print("Four of a kind : "+"%.2f" % (count[1]/n*100)+"%")
    print("Full house     : "+"%.2f" % (count[2]/n*100)+"%")
    print("Straight       : "+"%.2f" % (count[3]/n*100)+"%")
    print("Three of a kind: "+"%.2f" % (count[4]/n*100)+"%")
    print("Two pair       : "+"%.2f" % (count[5]/n*100)+"%")
    print("One pair       : "+"%.2f" % (count[6]/n*100)+"%")
# seed(0)
# play()
