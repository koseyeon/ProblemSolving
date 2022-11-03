n,m,x,y,k = map(int,input().split())
dice_state = {
  "north":0,
  "south":0,
  "east":0,
  "west":0,
  "top":0,
  "bottom":0
}
def rolling_east():
  prev_dice_state = dice_state.copy()
  dice_state["east"] = prev_dice_state["top"]
  dice_state["bottom"] = prev_dice_state["east"]
  dice_state["west"] = prev_dice_state["bottom"]
  dice_state["top"] = prev_dice_state["west"]
def rolling_west():
  prev_dice_state = dice_state.copy()
  dice_state["west"] = prev_dice_state["top"]
  dice_state["bottom"] = prev_dice_state["west"]
  dice_state["east"] = prev_dice_state["bottom"]
  dice_state["top"] = prev_dice_state["east"]
def rolling_north():
  prev_dice_state = dice_state.copy()
  dice_state["north"] = prev_dice_state["top"]
  dice_state["bottom"] = prev_dice_state["north"]
  dice_state["south"] = prev_dice_state["bottom"]
  dice_state["top"] = prev_dice_state["south"] 
def rolling_south():
  prev_dice_state = dice_state.copy()
  dice_state["south"] = prev_dice_state["top"]
  dice_state["bottom"] = prev_dice_state["south"]
  dice_state["north"] = prev_dice_state["bottom"]
  dice_state["top"] = prev_dice_state["north"] 
def bottom_copy():
  if(grid[x][y]==0):
    grid[x][y] = dice_state["bottom"]
  else:
    dice_state["bottom"] = grid[x][y]
    grid[x][y]=0
grid = []
for _ in range(n):
  grid.append(list(map(int,input().split())))
cmd_list = list(map(int,input().split()))
for cmd in cmd_list:
  if(cmd == 1):
    if(y>=m-1):
      continue
    y+=1
    rolling_east()
    bottom_copy()
  elif(cmd == 2):
    if(y<=0):
      continue
    y-=1
    rolling_west()
    bottom_copy()
  elif(cmd == 3):
    if(x<=0):
      continue
    x-=1
    rolling_north()
    bottom_copy()
  elif(cmd == 4):
    if(x>=n-1):
      continue
    x+=1
    rolling_south()
    bottom_copy()
  print(dice_state["top"])