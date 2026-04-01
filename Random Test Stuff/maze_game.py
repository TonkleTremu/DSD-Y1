maze = '''
########E#|
#..#####.#|
#.####...#|
#......###|
#.###.####|
#P########'''

def MovePlayer():
    player_pos = (0,0)
    split_maze = maze.split("|")
    for i in range(0, len(split_maze)):
        if("P" in split_maze[i]):
            player_pos = (i,split_maze[i].index("P"))
            print(player_pos)
    choix = input("Move North (N), South (N), East (E) or West (W)?\n").lower()
    if(choix == "n"):
        changed_val1 = split_maze[player_pos[0]]
        changed_val1 = list(changed_val1)
        changed_val1[player_pos[1]] = "."
        split_maze[player_pos[0]] = changed_val1
    
while(True):
    MovePlayer()