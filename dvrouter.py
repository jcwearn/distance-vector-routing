import dvector
from bellmanford import bellmanFord

class DVRouter():
    def __init__(self, routerName):
        distanceVector = dvector.DVector(routerName)
        routingTable = distanceVector.getRoutes
        self.routerName = routerName
        self.dvector  = distanceVector
        self.routingTable = distanceVector.getRoutes()
        self.firstHop = {}
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
        graph = self.getImportedTables()
        source = self.getRouterName()
        neighbors = self.getRoutingTableExclusive()
        distance, firstHop = bellmanFord(graph, source, neighbors)
        self.routingTable = distance
        self.firstHop = firstHop

    def formatNeighborTables(self, neighbors):
        neighborTables = {}
        for neighbor in neighbors:
            key = neighbor.getRouterName()
            value = neighbor.getRoutingTableExclusive()
            neighborTables[key] = value
        return neighborTables

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

    def getFirstHop(self):
        return self.firstHop

    def getImportedTables(self):
        return self.importedTables
