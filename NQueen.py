'''
This only find one possible solution, to get all arrangements use NAllQueen
comments start with #
debugging lines commentd with ###, uncommnt these to trace
'''

N=5
mcount = 0
loopc = 0
def isSafe(pos,q,row,col):
    ###print(f'Checking safty of queen {row} to place at ({row},{col}) w.r.t queen {q} ')
    ###print(f'Positions of queen {q} - ',pos[q])
    if(pos[q][0] == row
       or pos[q][1] == col
       or pos[q][0] + pos[q][1] == row + col
       or pos[q][0] - pos[q][1] == row - col):
        ###print('returning False\n')
        return False
    ###print('returning true\n')
    return True

def solveNQutil(board, row, pos):
    global mcount,loopc;
    mcount+=1;
    if row == N:
        # if its th last row return True all queens are placed
        return True
    # iterate each column for the row to see if we can find a safe position,
    #if safe position found recusively call solveNQUtil for placing another queen
    #if safe not found check for next colum, if safe not found for all columns backtrack
    for col in range(N):
        loopc+=1
        foundSafe = True
        for q in range(row):
            loopc +=1
            if(not isSafe(pos,q,row,col)):
                foundSafe = False
                break
        ###print(foundSafe)
        if(foundSafe) :
            ###print(f'found Safe position for queen {row} at {row},{col}')
            pos[row][0] = row
            pos[row][1] = col
            board[row][col] = 1
            ###print(f'calling solveNQ for Queen - {row+1}\n')
            if(solveNQutil(board,row+1,pos)):
                return True
            ###print(f'Did not find a place for queen {row+1} backtracking to adjust queen {row}\'s place')
            board[row][col] = 0
    return False        
        
    
if __name__ == '__main__':
    board = [[0 for i in range(N)] for j in range(N)]
    pos = [[0 for i in range(2)] for j in range(N)]
    if solveNQutil(board,0,pos):
        print(pos)
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
    else: print('No Solution')
    print(f'method count {mcount}, loop count {loopc}')