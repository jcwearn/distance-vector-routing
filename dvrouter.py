import dvector

class DVRouter():
    def __init__(self, routerName):
        distanceVector = dvector.DVector(routerName)
        routingTable = distanceVector.getRoutes
        self.routerName = routerName
        self.dvector  = distanceVector
        self.routingTable = distanceVector.getRoutes()
        self.importedTables = {}
        
    def addLink(self, neighbor, dist):
        self.dvector.loadRoute(neighbor, dist)
        self.routingTable = self.getDVector().getRoutes()

    def removeLink(self, neighbor):
        self.dvector.removeRoute(neighbor)
        self.routingTable = self.getDVector().getRoutes()

    def exportDistanceVector(self, neighbor):
        routingTable = self.routingTable.copy()
        del routingTable[self.getRouterName()]
        return routingTable

    def importDistanceVectors(self, neighborTables):
        neighborTables[self.getRouterName()] = self.getRoutingTableExclusive()
        self.importedTables = neighborTables

    def updateRoutingTable(self):
        pass

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

    def getRouterName(self):
        return self.routerName
    
    def getDVector(self):
        return self.dvector
    
    def getRoutingTable(self):
        return self.routingTable

    def getRoutingTableExclusive(self):
        routingTableExclusive = self.routingTable.copy()
        del routingTableExclusive[self.getRouterName()]
        return routingTableExclusive

    def getImportedTables(self):
        return self.importedTables
