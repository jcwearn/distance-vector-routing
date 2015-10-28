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

    return parsedContent

class DVSimulator:
    '''Creates a simulation of a network of routers using a distance vector algorithm to find the routes between nodes.'''
    def __init__(self, networkConfig):
        pass

    def dist(firstRouter, secondRouter):
        pass
    
if __name__ == '__main__':
    args = parseArgs()
    networkConfig = parseFile(args.config_file)
    simulator = DVSimulator(networkConfig);    
