import unittest
import dvector

class TestDVRouter(unittest.TestCase):
    def test_destinations(self):
        '''test destination method which returns a list of all destinations to which we have a distance'''

    def test_distance(self, destinations):
        '''test distance method that returns the distance from nodeName to 'destination from our distance dictorary, or infinity if there is no entry for 'destination' in our distance dictorart'''

    def test_loadRoute(self, destination, dist):
        '''test load route method which adds a route to 'destination' with the distance 'dist''''
