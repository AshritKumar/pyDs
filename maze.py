N=5
steps=0
##Function to check if move is safe
def isSafe(maze,x,y):
    if(x >= 0 and x < N and y>=0 and y<N and maze[x][y] == 1):
        return True
    return False
# print the sol'n matrix
def printRoute(sol):
    for i in range(N):
        for j in range(N):
            print(sol[i][j], end=" ")
        print('')

def solveMaze(maze,x,y):
    #create a solution matrix of N*N initialized to 0
    sol = [[0 for i in range(N)] for j in range(N)]
    if(solveMazeUtil(maze,x,y,sol)):
        print(f'solution exits with {steps} steps')
        printRoute(sol)
        return True
    print('No route to go out..!')
    return False
def solveMazeUtil(maze,x,y,sol):
    global steps
    #if x,y is the exit point retuen true
    if(x== N-1 and y == N-1):
        if(isSafe(maze,x,y)):
            sol[x][y] = 1
            steps =  steps+1
            return True
        steps -= 1
        return False
    # check if step is valid
    if(isSafe(maze,x,y)):
        # mark x,y in sol'n matrix
        sol[x][y] = 1
        
        # move in x direction
        if(solveMazeUtil(maze,x,y+1,sol)):
            steps =  steps+1
            return True
        # if not x move in Y direction
        if(solveMazeUtil(maze,x+1,y,sol)):
            steps =  steps+1
            return True
        # else, the move taken is not right,
        # backtrack to previous x,y positon and remove current x,y from sol'n matrix
        sol[x][y] = 0
        steps -= 1
        return False

if __name__ == '__main__':
    maze = [[1,1,1,1,0],
            [0,1,1,0,0],
            [0,1,1,1,0],
            [0,1,1,1,1],
            [0,0,0,0,1]]
    solveMaze(maze,0,0)