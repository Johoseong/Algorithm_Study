import heapq

def solution(n, paths, gates, summits):
    answer = [10 ** 10, 10 ** 10]
    graph = [[] for _ in range(n + 1)]
    summits.sort()
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])

    heap = []
    distance = [10 ** 10] * (n + 1)
    
    for g in gates:
        for i, [node, dist] in enumerate(graph[g]):
            heapq.heappush(heap, [dist, node])
    for g in gates:
        distance[g] = 0

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if distance[cur_node] <= cur_dist:
            continue
        distance[cur_node] = cur_dist

        if cur_node in summits:
            continue
        for next_node, next_dist in graph[cur_node]:
            if cur_dist < distance[next_node]:
                heapq.heappush(heap, [max(cur_dist, next_dist), next_node])

    for s in summits:
        if answer[1] > distance[s]:
            answer[0] = s
            answer[1] = distance[s]

    return answer