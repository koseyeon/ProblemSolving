def rotate_table(table):
    n = len(table)
    new_table = [[0]*n for _ in range(n)]
    for i in range(len(table)):
        for j in range(len(table)):
            new_table[j][n-1-i] = table[i][j]
    return new_table
def find_blocks_first(table,block_dict):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(table)
    number = 2
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                table[i][j] = number
                s = [[i,j]]
                block = [[i,j]]
                while s:
                    x,y = s.pop()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<n and table[nx][ny] == 1:
                            table[nx][ny] = number
                            s.append([nx,ny])
                            block.append([nx,ny])
                normalized_block = []
                for x,y in block:
                    normalized_block.append((x-i,y-j))
                block_dict[number] = block_dict.get(number,[]) + [normalized_block]
                number += 1
def find_blocks_next(table,block_dict):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(table)
    for key in block_dict.keys():
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if found:
                    break
                if abs(table[i][j]) == key:
                    found = True
                    target = table[i][j]
                    table[i][j] = -target
                    s = [[i,j]]
                    block = [[i,j]]
                    while s:
                        x,y = s.pop()
                        for k in range(4):
                            nx,ny = x+dx[k],y+dy[k]
                            if 0<=nx<n and 0<=ny<n and table[nx][ny] == target:
                                table[nx][ny] = -target
                                s.append([nx,ny])
                                block.append([nx,ny])
                    normalized_block = []
                    for x,y in block:
                        normalized_block.append((x-i,y-j))
                    block_dict[key] = block_dict.get(key,[]) + [normalized_block]
def match(game_board,block_dict):
    count = 0
    n = len(game_board)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                s = [[i,j]]
                space = [[i,j]]
                while s:
                    x,y = s.pop()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<n and game_board[nx][ny] == 0:
                            game_board[nx][ny] = 1
                            s.append([nx,ny])
                            space.append([nx,ny])
                normalized_space = []
                for x,y in space:
                    normalized_space.append((x-i,y-j))
                found = False
                for key in block_dict.keys():
                    for block in block_dict[key]:
                        if set(block) == set(normalized_space):
                            found = True
                            count += len(set(normalized_space))
                            del block_dict[key]
                        if found:
                            break
                    if found:
                        break
    return count
def solution(game_board, table):
    answer = -1
    block_dict = {}
    find_blocks_first(table,block_dict)
    table = rotate_table(table)
    find_blocks_next(table,block_dict)
    table = rotate_table(table)
    find_blocks_next(table,block_dict)
    table = rotate_table(table)
    find_blocks_next(table,block_dict)
    answer = match(game_board,block_dict)
    return answer