from collections import deque

def searching_algo_BFS(graph, s, t, parent):
  ROW = len(graph)
  visited = [False] * ROW
  queue = deque()

  queue.append(s)
  visited[s] = True

  while queue:
      u = queue.popleft()

      for ind, val in enumerate(graph[u]):
          if visited[ind] == False and val > 0:
              queue.append(ind)
              visited[ind] = True
              parent[ind] = u
              if ind == t:
                return True, [ind]

  return False, []

def ford_fulkerson(graph, source, sink):
   ROW = len(graph)
   parent = [-1] * ROW
   max_flow = 0

   while True:
       path_exists, path = searching_algo_BFS(graph, source, sink, parent)
       if not path_exists:
           break

       path_flow = float("Inf")
       s = sink
       while s != source:
           path_flow = min(path_flow, graph[parent[s]][s])
           s = parent[s]

       max_flow += path_flow

       v = sink
       while v != source:
           u = parent[v]
           graph[u][v] -= path_flow
           graph[v][u] += path_flow
           v = parent[v]

   return max_flow

def solution(entrances, exits, path):
   num_rooms = len(path)
   total_nodes = num_rooms + 2
   flow_graph = [[0] * total_nodes for _ in range(total_nodes)]

   for i in range(num_rooms):
       for j in range(num_rooms):
           flow_graph[i + 1][j + 1] = path[i][j]

   for entrance in entrances:
       flow_graph[0][entrance + 1] = float("Inf")

   for exit in exits:
       flow_graph[exit + 1][total_nodes - 1] = float("Inf")

   max_flow = ford_fulkerson(flow_graph, 0, total_nodes - 1)

   return max_flow
