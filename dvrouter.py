import dvector

class DVRouter():
    def __init__(self, routerName):
        distanceVector = dvector.DVector(routerName)
        routingTable = distanceVector.getRoutes
        self.dvector  = distanceVector
        self.routingTable = distanceVector.getRoutes()
        self.importedTable = {}
        
    def addLink(self, neighbor, dist):
        self.dvector.loadRoute(neighbor, dist)
        self.routingTable = self.getDVector().getRoutes()

    def removeLink(self, neighbor):
        self.dvector.removeRoute(neighbor)
        self.routingTable = self.getDVector().getRoutes()

    def exportDistanceVector(self, neighbor):
        return self.routingTable

    def importDistanceVectors(self, neighborTable):
        self.importedTable = neighborTable

    def updateRoutingTable():
        pass

    def getDVector(self):
        return self.dvector
    
    def getRoutingTable(self):
        return self.routingTable

    def getImportedTable(self):
        return self.importedTable
