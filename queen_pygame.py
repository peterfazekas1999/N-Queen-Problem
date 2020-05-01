import pygame

import numpy as np
k=1

grid = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
grid[0][k]=1
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
    if(count>=n):
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
if(solve(grid)):
    print_grid(grid)
else:
    print("No solution")
print("\n")

pygame.init()
white,black = (255,255,255),(0,0,0)
size = 50
n=len(grid)
queenImg = pygame.image.load('queenS.png')
gameDisplay = pygame.display.set_mode((size*n,size*n))
pygame.display.set_caption("Queen-problem")
gameDisplay.fill(white)
gameExit = False

def queen(x,y):
    gameDisplay.blit(queenImg,(x,y))


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    if(solve(grid)):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i][j]==1):
                    queen(size*j,size*i)

    for i in range(1,n):
        pygame.draw.rect(gameDisplay,black,[size*i,0,2,size*n])
    for i in range(1,n):
        pygame.draw.rect(gameDisplay,black,[0,size*i,size*n,2])
    pygame.draw.rect(gameDisplay,black,[0,0,size*n,size*n],1)
    pygame.display.update()

    
