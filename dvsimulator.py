import dvrouter, argparse

def isNumber(s):
    '''Checks if a string is a number.  Takes in a string s and returns true or false.'''
    try:
        float(s)
        return True
    except ValueError:
        return False

def parseArgs():
    '''Parses the arguments entered into the command line.  Returns the parsed arguments.'''
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="A configuration file that contains a list of routers and how they are linked together.")
    args = parser.parse_args()
    return args

def parseFile(filename):
    '''Parses the network configuration file.  It takes in a string represenation of a filename.  Returns a multidimensional array where each line is an array of 3 elements.'''
    with open(filename) as f:
        content = f.readlines()

    parsedContent = []

    for line in content:
        '''splits each element in a line into an array'''
        parsedContent.append(line.split())

    for row in parsedContent:
        '''loops through the rows in parsedContent'''
        for col in row:
            '''loops through the cols in parsedContent'''
            if isNumber(col):
                col = float(col)

    return parsedContent, content

def importAndUpdateRouters(router, tablesToImport):
    '''Imports distance vectors and updates routing tables for a giben router.  This method takes in the tables and the router that will be importing them'''
    neighborTables = tablesToImport.copy()
    del neighborTables[router.getRouterName()]
    router.importDistanceVectors(neighborTables)
    router.updateRoutingTable()

class DVSimulator:
    '''Creates a simulation of a network of routers using a distance vector algorithm to find the routes between nodes.'''
    def __init__(self, networkConfig):
        '''Constructer. This builds the network based on a config file. It takes in the netwrokConfig.'''
        self.routers = self.buildNetwork(networkConfig)

    def dist(firstRouter, secondRouter):
        pass

    def buildNetwork(self, networkConfig):
        '''Builds the simulation network. It creates all the routers and adds links in between neighbors.  It takes in a network configuagtion and returns a dictionary containing all the routers.'''
        routers = {}
        for row in networkConfig:
            '''Create a router for the first and second element in row array.  Add links between these routers given the distance at the third element'''
            firstRouter = row[0]
            secondRouter = row[1]
            distance = row[2]
            if firstRouter not in routers.keys():
                routers[firstRouter] = dvrouter.DVRouter(firstRouter)
            if secondRouter not in routers.keys():
                routers[secondRouter] = dvrouter.DVRouter(secondRouter)

            routers[firstRouter].addLink(secondRouter, distance)
            routers[secondRouter].addLink(firstRouter, distance)

        return routers

    def buildExport(self):
        '''Formats routingTables to be imported into a router.'''
        routers = self.getRouters()
        routerList = []
        for key in routers:
            '''Append each router in routers to routerList'''
            routerList.append(routers[key])

        return routerList[0].formatNeighborTables(routerList)

    def getRouters(self):
        return self.routers
    
if __name__ == '__main__':
    args = parseArgs()
    networkConfig, rawText = parseFile(args.config_file)
    
    simulator = DVSimulator(networkConfig);
    routers = simulator.getRouters()

    currentRouterState = []
    previousRouterState = []
        
    print 'Simulator starting, network config file: ' + args.config_file
    print 'Network config file contents:'
    for row in rawText:
        '''Print contents of each line in the rawText list'''
        print row.rstrip('\n')
    print '\nInitial tables before DV iterations:'
    for key in routers:
        '''Print initial state of routers'''
        print 'Routing table at ' + key
        print 'Dest dist firstHop'
        print '---- ---- --------'
        routingTable = routers[key].getRoutingTable()
        for route in routingTable:
            if isinstance(routingTable[route], int):
                extraSpace = '  '
            else:
                extraSpace = ''
            print '  ' + route  + '   ' + extraSpace + str(routingTable[route])  + '   ' + route
        print
        print

    try:    
        for x in xrange(0, 16):
            '''Run bellman ford algorithm until the network converges'''
            export =  simulator.buildExport()
            for key in routers:
                '''Import routingTables and Update router for every router in simulation'''
                importAndUpdateRouters(routers[key], export)
            print 'After DV Interation ' + str(x + 1)
            for key in routers:
                '''Print the state of routers after each iteration of DV algorithm'''
                print 'Routing table at ' + key
                print 'Dest dist firstHop'
                print '---- ---- --------'
                routingTable = routers[key].getRoutingTable()
                firstHop = routers[key].getFirstHop()
                for route in routingTable:
                    '''Print distances and first hops'''
                    if isinstance(routingTable[route], int):
                        extraSpace = '  '
                    else:
                        extraSpace = ''
                    print '  ' + route  + '   ' + extraSpace + str(routingTable[route])  + '   ' + firstHop[route]
                    currentRouterState.append(routingTable[route])
                print
                print
                count = x + 1

                if all(x in previousRouterState for x in currentRouterState) and len(currentRouterState) == 16:
                    raise StopIteration

            previousRouterState = currentRouterState
            currentRouterState = []

    except:
        pass
            
    print 'Simulation has converged after ' + str(count) + ' iterations'
