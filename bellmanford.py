def initialize(graph, source):
    '''Initializes the distance and predecessor dictionaries for the Bellman-Ford algorithm.  This method takes in a graph of weighted nodes, and a source node from the graph.  It returns a distance and predecessor dictionary'''
    distance = {} 
    predecessor = {}
    for node in graph:
        '''initialize the distance and predecessor dictionaries'''
        distance[node] = 16
        predecessor[node] = None
    distance[source] = 0 
    return distance, predecessor

def relax(node, neighbor, graph, distance, predecessor):
    '''Relaxes the distance value for a given node in a graph.  It updates the distance and predecessor dictionary if the distance between the node and it's neighbor is smaller than what is already held in the distance dictionary.  This function takes in a node, it's neighbor node, the full graph, the distance dictrionary, and the predecessor dictionary'''
    if distance[neighbor] > distance[node] + float(graph[node][neighbor]):
        distance[neighbor]  = distance[node] + float(graph[node][neighbor])
        predecessor[neighbor] = node

def calcFirstHop(predecessor, source, neighbors):
    '''Calculates the firstHop to each node from a source node.  It uses the predecessor dictionary that is returned from the Bellman-Ford algorithm.  It takes in the predecessor dictionary, the source node, and the source nodes neighbors.  This function returns a dictionary containing the first hops to all other nodes from the source node.'''
    firstHop = predecessor.copy()
    for key, value in firstHop.iteritems():
        '''set correct first hop for each key based on the predecessor'''
        if key == source or (value == source and key != source):
            firstHop[key] = key
        elif key not in neighbors:
            if value not in neighbors:
                firstHop[key] = firstHop[firstHop[value]]

    return firstHop

def bellmanFord(graph, source, neighbors):
    '''Runs the Bellman-Ford algorithm on a graph given it's source and neighbors.  It takes in a graph, the source node to start the algorithm from, and the neighbors of the source node.  It returns a distance dictionary containing the shortest distances to all other nodes and a firstHop dictionary which contains the first hop from the source node to all other nodes'''
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
