def initialize(graph, source):
    distance = {} 
    predecessor = {}
    for node in graph:
        '''initialize the distance and predecessor dictionaries'''
        distance[node] = 16
        predecessor[node] = None
    distance[source] = 0 
    return distance, predecessor

def relax(node, neighbor, graph, distance, predecessor):
    if distance[neighbor] > distance[node] + graph[node][neighbor]:
        distance[neighbor]  = distance[node] + graph[node][neighbor]
        predecessor[neighbor] = node

def calcFirstHop(predecessor, source, neighbors):
    firstHop = predecessor.copy()
    for key, value in firstHop.iteritems():
        '''set correct first hop for each key based on the predecessor'''
        if key == source or value == source and key != source:
            firstHop[key] = key
        elif key not in neighbors:
            if value in neighbors:
                firstHop[key] = firstHop[value]
            else:
                firstHop[key] = firstHop[firstHop[value]]

    return firstHop

def bellmanFord(graph, source, neighbors):
    distance, predecessor = initialize(graph, source)
    for i in range(len(graph)-1):
        '''iterate n times where n is the number of nodes in the graph'''
        for u in graph:
            '''for each of the above iterations, also iterate through each node in the graph'''
            for v in graph[u]:
                '''relax graph for each neighbor node'''
                relax(u, v, graph, distance, predecessor) 

    firstHop = calcFirstHop(predecessor, source, neighbors)
    return distance, firstHop
