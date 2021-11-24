def webSpiral (n):
    grid = []
    result = []
    count = 1
    if(n == 1): return result.append(1)
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(count)
            count += 1
        grid.append(tmp)
    while( True ):
        
        # right
        [result.append(i) for i in grid[0]]
        del grid[0]
        
        #down
        if len(grid) > 0:
            for i in range (len(grid)):
                result.append(grid[i][-1]) 
                del grid[i][-1]
            
            #left
            if len(grid[-1]) > 0 :
                [result.append(i) for i in grid[-1][::-1]]
                del grid[-1]
            
            #up
            for i in reversed(grid):
                result.append(i[0])
                del i[0]
        if not grid : break
    return result
        