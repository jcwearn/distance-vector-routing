import dvector

class DVRouter():
    def __init__(self, routerName):
        routingTable = dvector.DVector(routerName)
        self.routingTable = routingTable.getRoutes()
        
    def addLink():
        pass

    def removeLink():
        pass

    def exportDistanceVector(neighbor):
        pass

    def importDistanceVectors(neighbor_table):
        pass

    def updateRoutingTable():
        pass

    def getRoutingTable(self):
        return self.routingTable
