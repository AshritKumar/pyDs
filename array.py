def OD_array():
    from array import array
    arr = array('f',[1,2,3,4,5.5])
    for i in arr:
        print(i)
    
# 2d array
def TD_array():
    tDarr = [[col+1 for col in range(5)] for row in range(6)]
    tDarr[5][4] = 999
    print(tDarr)
    for c in range(5):
        for r in range(6):
            print(tDarr[r][c], end=" ")
        print()

#TD_array()
path = []
l = [1,1,1,1,]
path.append(l)
path.append([1,2,3,4,5])
path[0][0] = 8
print(path)