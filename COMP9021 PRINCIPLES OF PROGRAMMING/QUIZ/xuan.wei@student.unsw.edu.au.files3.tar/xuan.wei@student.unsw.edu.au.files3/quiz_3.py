from random import seed, randrange
from collections import Counter
import linecache, time
def give_values_to_letters(for_seed):
    seed(for_seed)
    return [randrange(1, 10) for _ in range(26)]
# word and letters are both meant to be strings of nothing but
# uppercase letters, values, a list returned by
# give_values_to_letters(). Returns:
# - -1 if word is not in dictionary.txt
# - 0 if word is in dictionary.txt but cannot be built from letters
# - the value of word according to values otherwise.
def can_be_built_from_with_value(word, letters, values):
    # word在txt里没出现，字母在letter里没能全出现，返回-1
    # word在txt里出现，字母在letter里没能全出现，返回0
    # word在txt里出现，字母在letter里全出现，返回word在values里面对应的值
    f = open('dictionary.txt', 'r', encoding='utf-8')
    count = -1
    for count, line in enumerate(f):
        pass
    count += 1
#     print(count)
    # 得出文件行数
    low = 0
    high = count - 1
    while low <= high:  # 二分搜索
        mid = int((low + high) / 2)
        line = linecache.getline(r'dictionary.txt', mid)
        index = line.find('\t')
        key = line[:index]
        if word == key:
            length = len(word)
            ala = 0
            l_letters = len(letters)
            letter = [0] * l_letters
            for n in range(l_letters):
                letter[n] = letters[n]
            for i in range(length):
                for j in range(l_letters):
                    if word[i] == letter[j]:
                        letter[j] = 0
                        ala += 1
                        break
                if ala == length:
                    amount = 0
                    for k in range(length):
                        amount += values[ord(word[k]) - 65]
                    return amount
            return 0
        else:
            same=0
            for i in range(min(len(key),len(word))):
                if word[i] > key[i]:
                    low = mid + 1
                    same+=1
                    break
                if word[i] < key[i]:
                    high = mid - 1
                    same+=1
                    break
                if i==min(len(key),len(word))-1 and same==0:
                    if min(len(key),len(word))==len(key):
                        low = mid + 1
                    else:
                        high = mid - 1
                        
    return -1
    # REPLACE PASS ABOVE WITH YOUR CODE
# letters is meant to be a string of nothing but uppercase letters.
# Returns the list of words in dictionary.txt that can be built
# from letters and whose value according to values is maximal.
# Longer words come before shorter words.
# For a given length, words are lexicographically ordered.
def most_valuable_solutions(letters, values):
    l_letters = len(letters)
    letter = [0] * l_letters
    for n in range(l_letters):
        letter[n] = letters[n]
    for j in range(l_letters, 0, -1):
        for i in range(0, j - 1):
            if letter[i] > letter[i + 1]:
                letter[i], letter[i + 1] = letter[i + 1], letter[i]
#     print(letter)
    f = open('dictionary.txt', 'r', encoding='utf-8')
    count = -1
    for count, line in enumerate(f):
        pass
    count += 1
    not_exist = ""
    bingo=[]
    for i in range(count):
        list = ['0'] * l_letters
        for k in range(l_letters ):
            list[k] = letter[k]
        line = linecache.getline(r'dictionary.txt', i)
        index = line.find('\t')
        key = line[:index]
        length = len(key)
        for j in range(length):
            flag = 0
            low = 0
            high = len(list) - 1
            not_exist = ""
            while low <= high:
                mid = int((low + high) / 2)
                if key[j] == not_exist:
                    break
                if key[j] == list[mid]:
                    del list[mid]
                    flag = 1
                    if j == length - 1:
#                         print(key,test(key, values))
                        bingo.append(key)
                    break
                elif key[j] > list[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            if flag == 0:
                not_exist = key[j]
                break
    if bingo!=[]:
        result=[]
        result.append(bingo[-1])
        del bingo[-1]
        while bingo!=[]:
            if test(result[0],values)>test(bingo[-1],values):
                del bingo[-1]
            elif test(result[0],values)==test(bingo[-1],values):
                result.append(bingo[-1])
                del bingo[-1]
            else:
                result=[]
                result.append(bingo[-1])
                del bingo[-1]
        result.reverse()
        for j in range(len(result)-1, 0, -1):#排长度
            for i in range(0, j):
                if len(result[i]) < len(result[i+1]):
                    result[i], result[i + 1] = result[i + 1], result[i]
        return result
    elif bingo==[]:
        return bingo
#         for j in range(len(bingo)-1, 0, -1):
#             for i in range(0, j - 1):
#                 if test(bingo[i],values) < test(bingo[i + 1],values):
#                     bingo[i], bingo[i + 1] = bingo[i + 1], bingo[i]
#         while test(bingo[-1],values)<test(bingo[0],values):
#             del bingo[-1]
#         for j in range(len(bingo)-1, 0, -1):#排长度
#             for i in range(0, j - 1):
#                 if len(bingo[i]) < len(bingo[i+1]):
#                     bingo[i], bingo[i + 1] = bingo[i + 1], bingo[i]
    return(bingo)
    
    
# REPLACE PASS ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
def test(word, values):
    amount = 0
    for k in range(len(word)):
        amount += values[ord(word[k]) - 65]
    return amount

# start = time.process_time()
values = give_values_to_letters(0)
print(f'A is worth {values[0]}, '
      f'B is worth {values[1]}, ' 
      f'C is worth {values[2]}, '
      f'D is worth {values[3]}, '
      f'E is worth {values[4]}, '
      f'F is worth {values[5]}, '
      f'G is worth {values[6]}, '
      f'H is worth {values[7]}, '
      f'I is worth {values[8]}, '
      f'J is worth {values[9]}, '
      f'K is worth {values[10]}, '
      f'L is worth {values[11]}, '
      f'M is worth {values[12]}, '
      f'N is worth {values[13]}, '
      f'O is worth {values[14]}, '
      f'P is worth {values[15]}, '
      f'Q is worth {values[16]}, '
      f'R is worth {values[17]}, '
      f'S is worth {values[18]}, '
      f'T is worth {values[19]}, '
      f'U is worth {values[20]}, '
      f'V is worth {values[21]}, '
      f'W is worth {values[22]}, '
      f'X is worth {values[23]}, '
      f'Y is worth {values[24]},'
      f'Z is worth {values[25]}')
# print(can_be_built_from_with_value('FIFHT', 'ABZUFTTHI', values))
# print(can_be_built_from_with_value('FIFTH', 'ABZUFTTHI', values) )
# print(can_be_built_from_with_value('FIFTH', 'ABFZUFTTHI', values))
# print(can_be_built_from_with_value('ZOOME', 'ABZYABZOYABZY', values))
# print(can_be_built_from_with_value('ZOOM', 'ABZYABZOYABZY', values))
# print(can_be_built_from_with_value('ZOOM', 'OABZYABZMOMYABZYO', values))
# print(most_valuable_solutions('UUU', values))
# print(most_valuable_solutions('ABFZUFTTHI', values))
# print(most_valuable_solutions('OABZYABZMOMYABZYO', values))
# print(most_valuable_solutions('ABCDEFGHIJKLMNOPQRSTUVWXYZ', values))
# print(most_valuable_solutions('AAAEEEIIIOOOUUUBMNOPR', values))
# print(most_valuable_solutions('THISORTHAT', values))
# values = give_values_to_letters(1)
# print(values)
# print(can_be_built_from_with_value('WRISTWATCHES','HTWSRWSITACE', values))
# print(most_valuable_solutions('HTWSRWSITACE', values))
# print(most_valuable_solutions('THISORTHAT', values) )
# print(most_valuable_solutions('LEURA', values))
# print(most_valuable_solutions('OBAMA', values))
# print(most_valuable_solutions('QWERTYUIO', values))

# end = time.process_time()
# time = end - start
# print(time)

