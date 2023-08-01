# Written by *** and Eric Martin for COMP9021
#
# Generates a random list of integers between 1 and 6
# whose length is chosen by the user, displays the list,
# outputs the difference between last and first values,
# then displays the values as horizontal bars of stars,
# then displays the values as vertical bars of stars
# surrounded by a frame.


from random import seed, randrange
import sys


try: 
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                             ).split()
                       )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(1, 7) for _ in range(length)]
print('Here are the generated values:', values)
# INSERT CODE HERE
print('\n',end="")
print('The difference between last and first values is:')
#Format required
print('   ',end="")
print( values[length-1] - values[0])
print('\n',end="")
print('Here are the values represented as horizontal bars:')
print('\n',end="")
for x in range(length):
    print('    ',end="")
    print(' * '*(values[x]))
# INSERT CODE HERE
print('\n',end="")
print('Here are the values represented as vertical bars, '
      'with a surrounding frame:' )
print('\n',end="")
print('   ',end="")
print(3*length*'-'+'--')
pattern=[[0 for col in range(max(values))] for row in range(length)]
for x in range(length):
    if values[x]<max(values):
        for y in range(values[x]):
            pattern[x][y]=1
        for y in range(values[x],max(values)):
            pattern[x][y]=0
    else:
        for y in range(max(values)):
            pattern[x][y]=1

for x in range(max(values)-1,-1,-1):
    print('   |',end="")
    for y in range(length):
        if pattern[y][x]==0:
            print('   ',end="")
        else:
            print(' * ',end="")
    print('|')
print('   ',end="")
print(3*length*'-'+'--')
print('\n',end="")
#print(pattern)
# INSERT CODE HERE
