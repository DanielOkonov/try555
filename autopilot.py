from bfs import bfs

def auto_pilot(snake, food):
    grid = []  # Not really used for now but can be used to check for obstacles
    start = tuple(snake.get_head_position())
    end = tuple(food.position)
    path = bfs(grid, start, end)

    if path:
        next_move = path[0]
        if next_move[0] > start[0]:
            snake.change_direction('RIGHT')
        elif next_move[0] < start[0]:
            snake.change_direction('LEFT')
        elif next_move[1] > start[1]:
            snake.change_direction('DOWN')
        elif next_move[1] < start[1]:
            snake.change_direction('UP')