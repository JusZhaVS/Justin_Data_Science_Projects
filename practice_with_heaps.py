import heapq

pq = []

#python by default is minheap
heapq.heappush(pq, (1, "low priority"))
heapq.heappush(pq, (3, "medium priority"))
heapq.heappush(pq, (0, "high priority"))


while pq:
    priority, value = heapq.heappop(pq)
    print(priority, value)