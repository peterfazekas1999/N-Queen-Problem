grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = len(grid)
def print_grid(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print("\n")

def is_empty(grid,l):
    for row in range(n):
        for col in range(n):
            if (grid[row][col]== 0):
                l[0] = row
                l[1] = col
                return True
    return False

def queen_count(grid):
    count = 0
    for i in range(n):
        for j in range(n):
            if(grid[i][j]==1):
                count +=1
    if(count>=4):
        return True
    return False

def is_row_used(grid,row):
    for i in range(n):
        if(grid[row][i]==1):
            return True
    return False
def is_col_used(grid,col):
    for i in range(n):
        if(grid[i][col] == 1):
            return True
    return False
                      
def is_diag_usedDR(grid,row,col):
    for i in range(0,n):
        if(row+i>=0 and row+i<n and col+i>=0 and col+i<n):
            if(grid[row+i][col+i]==1):
                return True
    return False

def is_diag_usedDL(grid,row,col):
    for i in range(0,n):
        if(row+i>=0 and row+i<n and col-i>=0 and col-i<n):
            if(grid[row+i][col-i] == 1):
                return True
    return False
        

def is_diag_usedUL(grid,row,col):
    for i in range(0,n):
        if(row-i>=0 and row-i<n and col-i>=0 and col-i<n):
            if(grid[row -i][col-i]==1):
                return True
    return False
    

def is_diag_usedUR(grid,row,col):
    for i in range(0,n):
        if(row-i>=0 and row-i<n and col+i>=0 and col+i<n):
            if(grid[row -i][col +i]==1):
                return True
    return False

def is_valid(grid,row,col):
    return not is_col_used(grid,col) and not is_row_used(grid,row) and not is_diag_usedDL(grid,row,col) and not is_diag_usedDR(grid,row,col) and not is_diag_usedUL(grid,row,col) and not is_diag_usedUR(grid,row,col)

def solve(grid):
    
    if(queen_count(grid)):
            return True

    for row in range(n):
        for col in range(n):
            if(is_valid(grid,row,col)):
                grid[row][col] = 1

                if(solve(grid)):
                    return True
                grid[row][col] = 0
    
    return False


for i in range(n):
    grid[0][i] = 1
    if(solve(grid)):
        print_grid(grid)
    else:
        print("No solution")
    print("\n")
    grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
