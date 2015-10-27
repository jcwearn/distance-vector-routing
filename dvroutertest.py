import unittest
import dvrouter

class TestDVRouter(unittest.TestCase):
    def test_constructor(self):
        '''Test that a newly created DVRouter has a link to itself byt to no other node'''
    def test_addLink(self):
        '''Test adding a link to a neighbor'''
    def test_removeLink(self):
        '''Test removing a link from a neighbor'''
    def test_exportDistanceVector(self):
        '''Test exporting distance vectors to a neighbor. If split horizon is on, should not advertize a route whose first hop is some neighbor to that neighbor'''
    def test_importDistanceVectors(self):
        '''Test importing a list of distance vectors.  It should raise a KeyError if the vector does not come from a neighbor'''
    def test_recomputeTable(self):
        '''Test recomputing the routing table via the Bellman-Ford algorithm'''
if __name__ == '__main__':
    unittest.main()        
