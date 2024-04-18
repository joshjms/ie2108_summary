import heapq

def dijkstra(g, start, end):
    # Assume g is an adjacency list

    # Initialize the distance array
    distance = [float('inf')] * len(g)
    distance[start] = 0

    # Initialize the priority queue
    pq = [(0, start)]
    heapq.heapify(pq)

    while pq:
        # Pop the vertex with the smallest distance
        d, u = heapq.heappop(pq)

        # If the distance is larger than the current distance, skip 
        # because it has already been processed before with a smaller distance
        if d > distance[u]:
            continue

        # If the vertex is the end vertex, return the distance
        if u == end:
            return d

        # For each neighbor of the vertex
        for v, w in g[u]:
            # Relax the edge
            if distance[u] + w < distance[v]:
                # if the new distance is smaller, update the distance
                distance[v] = distance[u] + w
                heapq.heappush(pq, (distance[v], v))

