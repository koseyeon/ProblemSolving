import copy
def solution(sizes):
    answer = 0
    wmax = [0,0]
    hmax = [0,0]
    
    for i in range(len(sizes)):
        if sizes[i][0] > wmax[0]:
            wmax = [sizes[i][0],i]
        if sizes[i][1] > hmax[0]:
            hmax = [sizes[i][1],i]
    while True:
        Flag = False
        if sizes[wmax[1]][0] <= hmax[0] and sizes[wmax[1]][1] < wmax[0]:
            sizes[wmax[1]] = [sizes[wmax[1]][1],sizes[wmax[1]][0]]
            Flag = True
        if sizes[hmax[1]][1] < wmax[0] and sizes[hmax[1]][0] <= hmax[0]:
            sizes[hmax[1]] = [sizes[hmax[1]][1],sizes[hmax[1]][0]]
            Flag = True
        if not Flag:
            break
        wmax = [0,0]
        hmax = [0,0]
        for i in range(len(sizes)):
            if sizes[i][0] > wmax[0]:
                wmax = [sizes[i][0],i]
            if sizes[i][1] > hmax[0]:
                hmax = [sizes[i][1],i]
    return wmax[0]*hmax[0]
        
        
            
            
        
        
    
    return answer