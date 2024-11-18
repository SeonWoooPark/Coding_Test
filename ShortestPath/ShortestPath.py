# 문제 1. 전보
# import heapq
# n, e, start = map(int, input().split())
# INF = int(1e9)
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(e):
#     s, e, t = map(int, input().split())
#     graph[s].append((e, t))
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (distance[start], start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(start)
#
# result = 0
# cnt = 0
# for d in distance:
#     if d != INF and d != 0:
#         cnt += 1
#         if result < d:
#             result = d
#
# print(cnt, result)

# 문제 2. 미래 도시
# n, m = map(int, input().split())
# INF = int(1e9)
# distance = [[INF] * (n+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     distance[i][i] = 0
#
#
# for _ in range(m):
#     s, e = map(int, input().split())
#     distance[s][e] = 1
#     distance[e][s] = 1
#
# x, k = map(int, input().split())
#
# for u in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             distance[i][j] = min(distance[i][j], distance[i][u] + distance[u][j])
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(distance[i][j], end=' ')
#     print()
#
# result = distance[1][k] + distance[k][x]
# if result >= INF:
#     print(-1)
# else:
#     print(result)

# 문제 3. 최단 경로
# import heapq
#
# INF = int(1e9)
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     x, y, c = map(int, input().split())
#     graph[x].append((y, c))
#
# def dijkstra(start):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (0, start))
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(start)
#
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print('INF')
#     else:
#         print(distance[i])

# 문제 4. 경로 찾기
# INF = int(1e9)
# n = int(input())
# graph = []
#
# for _ in range(n):
#     graph_row = list(map(int, input().split()))
#     graph_row = [x if x == 1 else INF for x in graph_row]
#     graph.append(graph_row)
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == INF or graph[i][j] == 0:
#             print(0, end=' ')
#         else:
#             print(1, end=' ')
#     print()

# 문제 5. 플로이드
# INF = int(1e9)
# n = int(input())
# bus = int(input())
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for i in range(n+1):
#     graph[i][i] = 0
#
# for _ in range(bus):
#     x, y, c = map(int, input().split())
#     graph[x][y] = min(graph[x][y], c)
#
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print(0, end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()

# 문제 6. 특별한 최단 경로
# import heapq
# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# distance_1 = [INF] * (n+1)
# distance_2 = [INF] * (n+1)
# distance_3 = [INF] * (n+1)
#
# for _ in range(m):
#     x, y, c = map(int, input().split())
#     graph[x].append((y, c))
#     graph[y].append((x, c))
#
# mid_1, mid_2 = map(int, input().split())
#
# def dijkstra(start, distance):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (0, start))
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = distance[now] + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(1, distance_1)
# dijkstra(mid_1, distance_2)
# dijkstra(mid_2, distance_3)
#
#
# # 1 -> mid_1 -> mid_2 -> n
# case_1 = distance_1[mid_1] + distance_2[mid_2] + distance_3[n]
# # 1 -> mid_2 -> mid_1 -> n
# case_2 = distance_1[mid_2] + distance_3[mid_1] + distance_2[n]
# result = min(case_1, case_2)
#
# if result >= INF:
#     print(-1)
# else:
#     print(result)

# 문제 7. 최소 비용 구하기
# import heapq
# INF = int(1e9)
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     x, y, c = map(int, input().split())
#     graph[x].append((y, c))
#
# start, end = map(int, input().split())
#
# def dijkstra(start):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (0, start))
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for i in graph[now]:
#             cost = distance[now] + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(start)
#
# print(distance[end])

# 문제 8. 케빈 베이컨의 6단계 법칙
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_v = INF
min_idx = -1
for i in range(1, n+1):
    sum_k = sum(graph[i][1:])
    if min_v > sum_k:
        min_v = sum_k
        min_idx = i

print(min_idx)



