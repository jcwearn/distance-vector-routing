class DVector():
    def __init__(self, nodeName):
        self.routes = {nodeName: 0}
        
    def destinations(self):
        return self.routes

    def distance(self, destination):
        if destination in self.routes.keys():
            return self.routes[destination]
        else:
            return 16        
    
    def loadRoute(self, destination, dist):
        self.routes[destination] = dist

    def removeRoute(self, destination):
        routes = self.getRoutes()
        del routes[destination]
        self.routes = routes

    def getRoutes(self):
        return self.routes
