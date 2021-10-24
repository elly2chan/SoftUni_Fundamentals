rows_in_the_maze = int(input())
maze = []

for row in range(rows_in_the_maze):
    maze_row = input()
    maze.append(maze_row)

# #check if there are only walls
# for level in maze:
#     if level.count('#') == len(level):