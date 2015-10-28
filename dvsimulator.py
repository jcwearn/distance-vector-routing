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
        parsedContent.append(line.split())

    for row in parsedContent:
        for col in row:
            if isNumber(col):
                col = float(col)

    return parsedContent, content

def importAndUpdateRouters(router, exportedTables):
    neighborTables = exportedTables.copy()
    del neighborTables[router.getRouterName()]
    router.importDistanceVectors(neighborTables)
    router.updateRoutingTable()

class DVSimulator:
    '''Creates a simulation of a network of routers using a distance vector algorithm to find the routes between nodes.'''
    def __init__(self, networkConfig):
        self.routers = self.buildNetwork(networkConfig)

    def dist(firstRouter, secondRouter):
        pass

    def buildNetwork(self, networkConfig):
        routers = {}
        for row in networkConfig:
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
        routers = self.getRouters()
        routerList = []
        for key in routers:
            routerList.append(routers[key])

        return routerList[0].formatNeighborTables(routerList)

    def getRouters(self):
        return self.routers
    
if __name__ == '__main__':
    args = parseArgs()
    networkConfig, rawText = parseFile(args.config_file)

    simulator = DVSimulator(networkConfig);
    routers = simulator.getRouters()

    print 'Simulator starting, network config file: ' + args.config_file
    print 'Network config file contents:'
    for row in rawText:
        print row.rstrip('\n')
    print '\nInitial tables before DV iterations:'
    for key in routers:
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

    export =  simulator.buildExport()
    for key in routers:
        importAndUpdateRouters(routers[key], export)

    for key in routers:
        print 'Routing table at ' + key
        print 'Dest dist firstHop'
        print '---- ---- --------'
        routingTable = routers[key].getRoutingTable()
        firstHop = routers[key].getFirstHop()
        
        for route in routingTable:
            if isinstance(routingTable[route], int):
                extraSpace = '  '
            else:
                extraSpace = ''
            print '  ' + route  + '   ' + extraSpace + str(routingTable[route])  + '   ' + route
        print
        print
