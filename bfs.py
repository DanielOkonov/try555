from collections import deque
from constants import *

def bfs(grid, start, end):
    queue = deque([start])
    paths = {start: []}

    while queue:
        cur_pos = queue.popleft()

        for dx, dy in [(-10, 0), (10, 0), (0, -10), (0, 10)]:
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            if 0 <= next_pos[0] < WIDTH and 0 <= next_pos[1] < HEIGHT:
                if next_pos == end:
                    return paths[cur_pos] + [next_pos]
                if next_pos not in paths:
                    queue.append(next_pos)
                    paths[next_pos] = paths[cur_pos] + [next_pos]

    return None