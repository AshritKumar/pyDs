'''
This algo gives all of the available routes, to get one of the possible routes use maze.py
Alternate to findAllRoutes
comments start with #
debugging lines commentd with ###, uncommnt these to trace
'''

R,C=5,5
Routes = 0
Steps = 0
def isSafe(maze,x,y):
    if(x >= 0 and x < R and y>=0 and y<C and maze[x][y] == 1):
        return True
    return False
def printRoutes(sol):
    for i in range(R):
        for j in range(C):
            print(sol[i][j], end=" ")
        print('')
        
def findAllPathsUtil(maze,i,j,sol):
    global Routes,Steps
    if i==R-1:
        #reached botom edge
        a = True
        for k in range(j,C):
            if(not isSafe(maze,i,k)):
                a = False
                break
        if(a):
            for k1 in range(j,C):
                sol[i][k1] = 1
                Steps+=1
            ###print(f'Reached {i}, {j} - returning true - sol matrix *')
            #count no of routes
            Routes+=1
            print(f'route {Routes}')
            print('--------')
            printRoutes(sol)
            print()
            return True
        else: return False
        
    if j==C-1:
        #reached right edge
        a = True
        for k in range(i,R):
            if(not isSafe(maze,k,j)):
                a = False
                break
        if(a):
            for k1 in range(i,R):
                sol[k1][j] = 1
                Steps+=1
            ###print(f'Reached {i}, {j} - returning true - sol matrix *')
            #count no of routes
            Routes+=1
            print(f'\nroute {Routes}')
            print('--------')
            printRoutes(sol)
            print()
            return True
        else: return False
      
    if(isSafe(maze,i,j)):
        sol[i][j] = 1
        ###print(f'current point({i},{j}) - sol matrix ')
        #printRoutes(sol)
        b = False
        # x direction
        if(findAllPathsUtil(maze,i,j+1,sol)):
            b = True
            Steps+=1
        
        #Y direction
        if(findAllPathsUtil(maze,i+1,j,sol)):
            b = True
            Steps+=1
        
        if(not b):
            #backtrack if no route available after i,j
            sol[i][j] = 0
            Steps-=1
            return False
        else: return True
    else: return False
        
            
            

if __name__ == '__main__':
    maze = [[1,1,1,1,1],
            [0,1,1,1,1],
            [0,1,1,1,1],
            [0,1,1,1,1],
            [0,0,0,0,1]]
    sol = [[0 for k in range(C)]  for i in range(R) ]
    findAllPathsUtil(maze,0,0,sol)
    print(f'{Routes} routes available')
    if(Routes != 0):
        print('Overall matrix')
        printRoutes(sol)