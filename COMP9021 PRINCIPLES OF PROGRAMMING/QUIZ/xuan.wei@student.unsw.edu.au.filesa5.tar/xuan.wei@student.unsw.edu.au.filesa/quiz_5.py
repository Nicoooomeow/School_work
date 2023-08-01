# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
# In both functions below, grid is supposed to be a sequence of strings
# all of the same length, consisting of nothing but spaces and *s,
# and represent one or more "full polygons" that do not "touch" each other.
def display(*grid):
    for i in range(len(grid)):
        print(*grid[i])
    # REPLACE pass ABOVE WITH YOUR CODE

def display_leftmost_topmost_boundary(*grid):
    max_length=max(len(x) for x in grid)
    pattern=[[" " for col in range(max_length)] for row in range(len(grid))]
    #装进数组带走
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pattern[i][j]=grid[i][j]
    flag=0
    for i in range(len(pattern)):
        for j in range(max_length):
            if pattern[i][j]=="*":
                scan(pattern,flag,i,j)
                flag+=1
    # remain=[0]*flag
    # for i in range(len(pattern)):
    #     for j in range(flag):
    #         remain[j]+=pattern[i].count(j)
#     stay=remain.index(max(remain))
    for i in range(len(pattern)):
        for j in range(max_length):
            if pattern[i][j]==0:
                pattern[i][j]="*"
                continue
            if pattern[i][j]!=" ":
                pattern[i][j]=" "
    #以前的代码，现在已经不知道以前是咋写的了
    for i in range(len(grid)):
        for j in range(max_length):
            if pattern[i][j]=="*" and i!=0 and j>0 and i<len(grid)-1 and j <len(grid[i-1])-1 and j<len(grid[i+1])-1:
                if pattern[i-1][j]!=" " and pattern[i][j-1]!=" " and pattern[i+1][j]!=" " and pattern [i][j+1]!=" ":
                    pattern[i][j]="#"
    for i in range(len(grid)):
        for j in range(max_length):
            if pattern[i][j]=="#":
                pattern[i][j]=" "
    for i in range(len(pattern)):
        print(*pattern[i])
def scan(pattern,full,a,b):
    pattern[a][b]=full
    if a>0 and pattern[a-1][b]=="*":
        scan(pattern,full,a-1,b)
    if a<len(pattern)-1 and pattern[a+1][b]=="*":
        scan(pattern,full,a+1,b)
    if b>0 and pattern[a][b-1]=="*":
        scan(pattern,full,a,b-1)
    if b<len(pattern[a])-1 and pattern[a][b+1]=="*":
        scan(pattern,full,a,b+1)
# grid_2 = (' * ','***   ** ',' *** *** ',' ***  * ','**** ',' ** ')
# display(*grid_2)
# display_leftmost_topmost_boundary(*grid_2)

