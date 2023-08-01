from random import seed, shuffle
def generate_dial_and_centre(for_seed):
    colours = 'CDHS' # Clubs梅花, Diamonds方片, Hearts红桃, Spades黑桃,
    #                                            jacks, queens, kings
    ranks = list(str(x) for x in range(1, 11)) + list('jqk')
    seed(for_seed)
    cards = [colour + rank for colour in colours for rank in ranks]
    shuffle(cards)
    dial = dict.fromkeys(range(1, 13))
    for i in range(12):
        dial[i + 1] = [cards[i + 13 * j] for j in range(4)]
    centre=[cards[12 + 13 * j] for j in range(4)]
    return dial, centre
def get_real(hour,dial,i):
    orl='\\U0001f0'
    output=orl+get_color(dial,hour,i)+get_uni_num(dial,hour,i)
    return output.encode('utf-8').decode('unicode_escape')
def get_move(move):
    orl='\\U0001f0'
    num=move[1:]
    jqk=0
    color=0
    if num=='10':
        jqk='a'
    elif num=='j':
        jqk='b'
    elif num=='q':
        jqk='d'
    elif num=='k':
        jqk='e'
    else:
        jqk=num
    if move[0]=='S':
        color= 'a'
    elif move[0]=='H':
        color= 'b'
    elif move[0]=='D':
        color= 'c'
    else:
        color= 'd'
    output=orl+color+jqk
    return output.encode('utf-8').decode('unicode_escape')
def initial_hour(hour, dial):
    orl='\\U0001f0'
    output_1=orl+get_color(dial,hour,0)+get_uni_num(dial,hour,0)
    output_2=orl+get_color(dial,hour,1)+get_uni_num(dial,hour,1)
    output_3=orl+get_color(dial,hour,2)+get_uni_num(dial,hour,2)
    output_4=orl+get_color(dial,hour,3)+get_uni_num(dial,hour,3)
    result="hidden"+output_1.encode('utf-8').decode('unicode_escape')+"  hidden"+output_2.encode('utf-8').decode('unicode_escape')+"  hidden"+output_3.encode('utf-8').decode('unicode_escape')+"  hidden"+output_4.encode('utf-8').decode('unicode_escape')
    print(result)
#     return result
    # REPLACE PASS ABOVE WITH YOUR CODE
def get_uni_num(dial,hour,i):
    num=dial[hour][i][1:]
    jqk=0
    if num=='10':
        jqk='a'
    elif num=='j':
        jqk='b'
    elif num=='q':
        jqk='d'
    elif num=='k':
        jqk='e'
    else:
        jqk=num
    return jqk

def get_color(dial,hour,i):
    if dial[hour][i][0]=='S':
        return 'a'
    elif dial[hour][i][0]=='H':
        return 'b'
    elif dial[hour][i][0]=='D':
        return 'c'
    else:
        return 'd'
def get_pok_position1(luo):
    num=luo[1:]
    pok=0
    if num=='j':
        pok=11
    elif num=='q':
        pok=12
    elif num=='k':
        pok=13
    elif num=='10':
        pok=10
    else:
        pok=int(num)
    return pok
# def test(dial,centre):
#     if get_pok_position1(centre[0])==get_pok_position1(centre[1])==get_pok_position1(centre[2])==get_pok_position1(centre[3])==13:
#             for i in range(1,13):
#                 if get_pok_position1(dial[i][0])==get_pok_position1(dial[i][1])==get_pok_position1(dial[i][2])==get_pok_position1(dial[i][3])==i:
#                         pass
#                 else:
#                     return 0
#     else:
#         return 0
#     return 1
def hour_after_playing_from_beginning_for_at_most(hour, nb_of_steps, dial,centre):
    dic={}
    test=[0]*13
    for i in range(4):
        dic[dial[hour][i]]="hidden"
    move=centre[-1]
    pok=get_pok_position1(move)#对应第一张牌的点数
    del centre[-1]
    for i in range(nb_of_steps-1):
        if pok==13:
            centre.insert(0,move)
            move=centre[-1]
            del centre[-1]
            test[12]+=1
            pok=get_pok_position1(move)
            if test[12]==4:
                if test.count(4)==13:
                    print(get_real(hour,dial,0)+"  "+get_real(hour,dial,1)+"  "+get_real(hour,dial,2)+"  "+get_real(hour,dial,3))
                else:
                    print("Could not play that far...")
                return
        else:
            dial[pok].insert(0,move)#放到牌堆顶部
            test[pok-1]+=1
            if pok==hour:
                dic[move]=''
            move=dial[pok][-1]#牌堆底部下一个要移动的牌
            del dial[pok][-1]
            if pok==hour:
                dic.pop(move)
            pok=get_pok_position1(move)#下一个要移动的牌的数字
            if test[pok-1]==4:
                if test.count(4)==13:
                    print(get_real(hour,dial,0)+"  "+get_real(hour,dial,1)+"  "+get_real(hour,dial,2)+"  "+get_real(hour,dial,3))
                else:
                    print("Could not play that far...")
                return
    result=get_move(move)
    for i in range(len(dial[hour])):
        result+="  "+dic[dial[hour][i]]+get_real(hour,dial,i)
    print(result)
    
    # REPLACE PRINT() ABOVE WITH YOUR CODE

def kings_at_end_of_game(dial, centre):
#     move=centre[-1]
#     pok=get_pok_position1(move)#对应第一张牌的点数,从中心开始
#     del centre[0]
#     bingo=0
#     next_p=0
#     while centre:
#         if pok==13:
#             centre.append(move)
#             move=centre[0]
#             next_p=get_pok_position1(move)
#             if pok==next_p:
#                 bingo+=1
#                 if bingo==4:
#                     result=test(dial,centre)
#                     if result==1:
#                         print(centre)
#                         return 1
#                     else:
#                         print("No success...")
#                         return
#             else:
#                 bingo=0
#             pok=next_p
#             del centre[0]
#         else:
#             dial[pok].append(move)#放到牌堆底部
#             move=dial[pok][0]#牌堆顶部下一个要移动的牌
#             if pok==13:
#                 del centre[0]
#             else:
#                 del dial[pok][0]
#             next_p=get_pok_position1(move)#下一个要移动的牌的数字
#             if pok==next_p:
#                 bingo+=1
#                 if bingo==4: 
#                     return 0
#             else:
#                 bingo=0
#             pok=next_p
    # REPLACE PRINT() ABOVE WITH YOUR CODE
    test=[0]*13
    move=centre[-1]
    pok=get_pok_position1(move)#对应第一张牌的点数
    del centre[-1]
    while centre:
        if pok==13:
            centre.insert(0,move)
            move=centre[-1]
            del centre[-1]
            test[12]+=1
            pok=get_pok_position1(move)
            if test[12]==4:
                if test.count(4)==13:
                    print(get_move(centre[0])+"  "+get_move(centre[1])+"  "+get_move(centre[2])+"  "+get_move(move))
                else:
                    print("No success...")
                return
        else:
            dial[pok].insert(0,move)#放到牌堆顶部
            test[pok-1]+=1
            move=dial[pok][-1]#牌堆底部下一个要移动的牌
            del dial[pok][-1]
            pok=get_pok_position1(move)#下一个要移动的牌的数字
            if test[pok-1]==4:
                print("No success...")
                return
    # result=get_move(move)
    # for i in range(len(dial[hour])):
    #     result+="  "+dic[dial[hour][i]]+get_real(hour,dial,i)
    # print(result)
# POSSIBLY DEFINE OTHER FUNCTIONS
# dial,centre=generate_dial_and_centre(0)
# initial_hour(1, dial)
# hour_after_playing_from_beginning_for_at_most(8, 13, dial,centre)
# print(dial,centre)
# dial,centre=generate_dial_and_centre(2)
# dial,centre=generate_dial_and_centre(18)
# hour_after_playing_from_beginning_for_at_most(1, 53, dial,centre)
# kings_at_end_of_game(dial, centre)
# initial_hour(1, dial)
# print(centre)

