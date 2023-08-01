# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Prompts the user for a seed, a dimension dim, and an upper bound N.
# Randomly fills a grid of size dim x dim with numbers between 0 and N
# and computes:
# - the largest value n such that there is a path of the form (0, 1, 2,... n);
# - the number of such paths.
# A path is obtained by repeatedly moving in the grid one step north, south,
# west, or east.


import sys
from random import seed, randint


def display_grid():
    for row in grid:
        print(' '.join(f'{e:{len(str(upper_bound))}}' for e in row)) 

def value_and_number_of_longest_paths():
    arr=[[] for i in range(2)]
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]==0:
                scan(i,j,arr,0)
    return arr[0][-1], arr[1][-1]
    # REPLACE THE RETURN STATEMENT WITH YOUR CODE        
def scan(a,b,arr,num):
    if num not in arr[0]:
        arr[0].append(num)
        arr[1].append(1)
    else:
        arr[1][arr[0].index(num)]+=1
    if a>0 and grid[a-1][b]==num+1:
        scan(a-1,b,arr,num+1)
    if a<dim-1 and grid[a+1][b]==num+1:
        scan(a+1,b,arr,num+1)
    if b>0 and grid[a][b-1]==num+1:
        scan(a,b-1,arr,num+1)
    if b<dim-1 and grid[a][b+1]==num+1:
        scan(a,b+1,arr,num+1)
# POSSIBLY DEFINE OTHER FUNCTIONS

provided_input = input('Enter three integers: ').split()
if len(provided_input) != 3:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    for_seed, dim, upper_bound = (abs(int(e)) for e in provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randint(0, upper_bound) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

max_value, nb_of_paths_of_max_value = value_and_number_of_longest_paths()
if not nb_of_paths_of_max_value:
    print('There is no 0 in the grid.')
else:
    print('The longest paths made up of consecutive numbers starting '
          f'from 0 go up to {max_value}.'
         )
    if nb_of_paths_of_max_value == 1:
        print('There is one such path.')
    else:
        print('There are', nb_of_paths_of_max_value, 'such paths.')

