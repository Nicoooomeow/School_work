from math import sqrt
from itertools import permutations
import math
def is_good_prime(number):
    while is_prime(number):
        zero=1
        repeat=[]
        while number>=10:
            zero=number%10
            if zero==0:#不为0
                return False
            for i in range(len(repeat)):#不重复
                if zero==repeat[i]:
                    return False
            repeat.append(zero)
            number=int(number/10)
        for i in range(len(repeat)):#不重复
                if number==repeat[i]:
                    return False
        return True
    return False
#     # REPLACE PASS ABOVE WITH YOUR CODE
# # pattern is expected to be a nonempty string consisting of underscores
# # and digits of length at most 7.
# # Underscores have to be replaced by digits so that the resulting number
# # is the smallest good prime, in case it exists.
# # The function returns that number if it exists, None otherwise.
# def smallest_good_prime(pattern):
#     length=len(pattern)
#     num=[]
#     pos=[]
#     posi=0
#     for i in range(length):
#         if pattern[i]=='_':
#             num.append(1)
#             pos.append(i)
#             posi+=1
#         elif pattern[i]=='0':
#             return None
#         else:
#             num.append(int(pattern[i]))
#     w_test=0
#     if pos==[]:
#         if is_good_prime(int(pattern)):
#             return pattern
#         else:
#             return None
#     for i in range(len(pos)-1,-1,-1):
#         for j in range(1,10):
#             num[pos[i]]=j
#             for k in range(len(num)):
#                 w_test+=num[k]*(10**(len(num)-k-1))
#                 if is_good_prime(w_test):
#                     return w_test
#             w_test=0
#     return None
#     # REPLACE PASS ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
def smallest_good_prime(pattern):
    if '_'not in pattern:#不含_
        if is_good_prime(int(pattern)):
            return pattern
        else:
            return None
    if '0' in pattern:#含0
        return None
    if [1 for i in pattern if i != '_' and pattern.count(i) > 1]:#重复
        return None
    length=len(pattern)
    num=[]
#     pos=[]#_的位置
    count=0
    test=[]#increase number
    for i in range(length):
        if pattern[i]=='_':
            num.append('_')
            count+=1
        else:
            num.append(int(pattern[i]))
    w_test=0
#     print(num,pos)
    flag=len(test)-1
    for i in range(count):
        test.append(1)
    while 1:
        for i in range(len(num)):
            if num[i]=='_':
#                 print(flag,i,len(num))
                w_test+=test[flag]*(10**(len(num)-i-1))
                flag-=1
#                 print(w_test)
                continue
            w_test+=num[i]*(10**(len(num)-i-1))
#             print(w_test)
        if is_good_prime(w_test):
            return w_test
        else:
            test[0]+=1
            flag=len(test)-1
            w_test=0
            while 10 in test:
                for i in range(len(test)):
                    if test[i]==10 and i!=len(test)-1:
                        test[i]=1
                        test[i+1]+=1
                        break
                    elif test[i]==10 and i==len(test)-1:
                        return None
        
    
def get_prime(lower,upper):
    prime=[]
    for num in range(lower,upper + 1):
        if num > 1:
            if num == 2:
                prime.append(2)
            if num % 2 == 0:
                break
            for current in range(3, int(math.sqrt(number) + 1), 2):
                if number % current == 0: 
                    return False
            return True
        return False
# print(is_good_prime(867))
# print(is_good_prime(4027))
# print(is_good_prime(12923))
# print(is_good_prime(16879))
# print(is_good_prime(26317))
# print(smallest_good_prime('_0_'))
# print(smallest_good_prime('2_2'))
# print(smallest_good_prime('123'))
# print(smallest_good_prime('_98'))
# print(smallest_good_prime('3167'))
# print(smallest_good_prime('__'))
# print(smallest_good_prime('___'))
# print(smallest_good_prime('1_7'))
# print(smallest_good_prime('_89'))
# print(smallest_good_prime('_89_'))
# print(smallest_good_prime('_2_4_'))
# print(smallest_good_prime('1__4_7'))

