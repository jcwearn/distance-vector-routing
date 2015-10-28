import dvrouter, argparse

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="A configuration file that contains a list of routers and how they are linked together.")
    args = parser.parse_args()
    return args

class DVSimulator:
    '''Creates a simulation of a network of routers using a distance vector algorithm to find the routes between nodes.'''

    
if __name__ == '__main__':
    print parseArgs()
