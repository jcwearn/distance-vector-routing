def initialize(graph, source):
    d = {} 
    p = {} 
    for node in graph:
        d[node] = 16
        p[node] = None
    d[source] = 0 
    return d, p

def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellmanFord(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): 
        for u in graph:
            for v in graph[u]: 
                relax(u, v, graph, d, p) 

    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p
