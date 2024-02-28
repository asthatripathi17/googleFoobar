from collections import deque
def solution(map):
    k = 1
    m = len(map)
    n = len(map[0])

    # for BFS
    que = deque()
    i = 0
    j = 0
    que.append([0, 0, k])  # Starting point

    # data structure to check visited nodes using the constraints given
    visited = [[[False] * 400 for _ in range(20)] for _ in range(20)]
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # defined the directions - Up|Down|Left|Right

    steps = 1
    # starting the BFS
    while que:
        size = len(que)
        # to traverse all the neighbours of popped elements
        while size > 0:
            temp = que.popleft()

            curr_i, curr_j, obst = temp[0], temp[1], temp[2]

            if curr_i == m - 1 and curr_j == n - 1:
                return steps  # End point reached

            for dir in directions:
                new_i, new_j = curr_i + dir[0], curr_j + dir[1]

                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue  # Out of bound

                if map[new_i][new_j] == 0 and not visited[new_i][new_j][obst]:
                    # If not visited and there is no obstacle as it is 0
                    que.append([new_i, new_j, obst])
                    visited[new_i][new_j][obst] = True  # Visited now
                elif map[new_i][new_j] == 1 and obst > 0 and not visited[new_i][new_j][obst - 1]:
                    # has obstacle but obstacle count > 0
                    que.append([new_i, new_j, obst - 1])
                    visited[new_i][new_j][obst - 1] = True

            size -= 1
        steps += 1

    return -1  # Target not found
