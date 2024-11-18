# 문제 1. 보급로
import heapq
result_list = []

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    INF = int(1e9)
    n = int(input())
    graph = []
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = 0
    start = [0, 0]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for _ in range(n):
        graph.append(list(map(int, input())))

    def dijkstra(start, n):
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, r_c = heapq.heappop(q)
            r = r_c[0]
            c = r_c[1]

            if distance[r][c] < dist:
                continue

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < n and 0 <= nc < n:
                    cost = dist + graph[nr][nc]
                    if cost < distance[nr][nc]:
                        distance[nr][nc] = cost
                        heapq.heappush(q, (cost, [nr, nc]))

    dijkstra(start, n)
    result_list.append(distance[n-1][n-1])

for i in range(1, T+1):
    print(f'#{i} {result_list[i-1]}')