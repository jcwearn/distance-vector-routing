class DVector():
    '''Entity class that contains data about distance vectors'''
    def __init__(self, nodeName):
        '''Constructor. Takes in a string nodeName and sets the routes instance variable to contain nodeName with distance 0'''
        self.routes = {nodeName: 0}
        
    def destinations(self):
        '''Returns the routes instance variable'''
        return self.routes

    def distance(self, destination):
        '''Returns the distance from self to some destination.  If the destination is unreachable it returns 16 (infinity)'''
        if destination in self.routes.keys():
            return self.routes[destination]
        else:
            return 16        
    
    def loadRoute(self, destination, dist):
        '''Adds a route to the routes instance variable.  Takes in the destination, and the distance to that destionation.'''
        self.routes[destination] = dist

    def removeRoute(self, destination):
        '''Removes a route from the routes instance variable.  Takes in the destination to be removed.'''
        routes = self.destinations()
        del routes[destination]
        self.routes = routes
