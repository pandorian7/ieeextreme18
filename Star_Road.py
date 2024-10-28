from collections import defaultdict

n = int(input())

I = lambda i:i-1

graph = defaultdict(list)
        
stars = list(map(int, input().split()))

def add_to_graph(path):
    u, v = path
    graph[I(u)].append(I(v))
    graph[I(v)].append(I(u))

for _ in range(n-1):
    add_to_graph(map(int, input().split()))


print(stars)
print(graph)

def dfs(start, prv_star):
    count = 0
    

# def max_dining_experience(N, stars, roads):
#     from collections import defaultdict

#     # Build the graph
#     graph = defaultdict(list)
#     for u, v in roads:
#         graph[u].append(v)
#         graph[v].append(u)

#     def dfs(city, last_star):
#         count = 0
#         for neighbor in graph[city]:
#             if visited[neighbor]:
#                 continue
#             if stars[neighbor - 1] > last_star:  # stars are 1-indexed in the problem
#                 visited[neighbor] = True
#                 count = max(count, dfs(neighbor, stars[neighbor - 1]) + 1)
#                 visited[neighbor] = False  # backtrack
#         return count

#     max_count = 0

#     for start_city in range(1, N + 1):
#         visited = [False] * (N + 1)  # To track visited cities
#         visited[start_city] = True
#         max_count = max(max_count, dfs(start_city, stars[start_city - 1]))

#     return max_count

# # Example usage
# N = n
# stars = [city.star for city in cities]
# roads = [tuple(map(int, input().split())) for i in range(n-1)]

# result = max_dining_experience(N, stars, roads)
# print(result)


    