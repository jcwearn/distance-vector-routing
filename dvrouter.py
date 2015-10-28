import dvector
from bellmanford import bellmanFord

class DVRouter():
    '''Creates a distance vector router that can interact with other routers.'''
    def __init__(self, routerName):
        '''Constructor.  This method takes in a routerName and initializes all the necessary instance variables for a router.'''
        distanceVector = dvector.DVector(routerName)
        self.routerName = routerName
        self.dvector  = distanceVector
        self.routingTable = distanceVector.destinations()
        self.firstHop = {}
        self.importedTables = {}
        
    def addLink(self, neighbor, dist):
        '''Adds a link with distance 'dist' from self to another router.  It takes in the neighbor routerName and distance value.'''
        self.dvector.loadRoute(neighbor, dist)
        self.routingTable = self.getDVector().destinations()

    def removeLink(self, neighbor):
        '''Removes a link between self and a neighbor router.  It takes in a neighbor routerName.'''
        self.dvector.removeRoute(neighbor)
        self.routingTable = self.getDVector().destinations()

    def exportDistanceVector(self):
        '''Prepares a distance vector table to be exported to a neighbor.  Returns the distance vector table'''
        routingTable = self.routingTable.copy()
        del routingTable[self.getRouterName()]
        return routingTable

    def importDistanceVectors(self, neighborTables):
        '''Imports a distance vector table from one or more routers.  It sets this table to the instance variable importedTables.  It takes in a graph of neighborTables that can be formated using formatNeighborTables()'''
        neighborTables[self.getRouterName()] = self.getRoutingTableExclusive()
        self.importedTables = neighborTables

    def updateRoutingTable(self):
        '''Updates the routing table based on the contents of importedTables instance variable. It updates the value of the routingTable and firstHop instance variables.  It uses the bellmanFord function implementef in bellmanford.py'''
        graph = self.getImportedTables()
        source = self.getRouterName()
        neighbors = self.getRoutingTableExclusive()
        distance, firstHop = bellmanFord(graph, source, neighbors)
        self.routingTable = distance
        self.firstHop = firstHop

    def formatNeighborTables(self, neighbors):
        '''Formats routing tables from an array of neighbor routers.  It takes in an array of routers and returns the correctly formated graph of the neighbor tables to be used in the importDistanceVectors() method.  '''
        neighborTables = {}
        for neighbor in neighbors:
            key = neighbor.getRouterName()
            value = neighbor.getRoutingTableExclusive()
            neighborTables[key] = value
        return neighborTables

    def getRouterName(self):
        '''Getter method for routerName instance variable'''
        return self.routerName
    
    def getDVector(self):
        '''Getter method for dvector instance variable'''
        return self.dvector
    
    def getRoutingTable(self):
        '''Getter method for routingTable instance variable'''
        return self.routingTable

    def getRoutingTableExclusive(self):
        '''Getter method for routingTable instance variable. However it removes the entry for the router that the method is being called on'''
        routingTableExclusive = self.routingTable.copy()
        del routingTableExclusive[self.getRouterName()]
        return routingTableExclusive

    def getFirstHop(self):
        '''Getter method for firstHop instance variable'''
        return self.firstHop

    def getImportedTables(self):
        '''Getter method for importedTables instance variable'''
        return self.importedTables
