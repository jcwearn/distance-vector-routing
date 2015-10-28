import unittest
import dvrouter

class TestDVRouter(unittest.TestCase):
    def test_constructor(self):
        '''Test that a newly created DVRouter has a link to itself but to no other node'''
        router1 = dvrouter.DVRouter('A')
        table1 = router1.getRoutingTable()
        self.assertEqual(len(table1), 1)
        self.assertEqual(table1['A'], 0)

        router2 = dvrouter.DVRouter('B')
        table2 = router2.getRoutingTable()
        self.assertEqual(len(table2), 1)
        self.assertEqual(table2['B'], 0)
        
    def test_addLink(self):
        '''Test adding a link to a neighbor'''
    def test_removeLink(self):
        '''Test removing a link from a neighbor'''
    def test_exportDistanceVector(self):
        '''Test exporting distance vectors to a neighbor. If split horizon is on, should not advertize a route whose first hop is some neighbor to that neighbor'''
    def test_importDistanceVectors(self):
        '''Test importing a list of distance vectors.  It should raise a KeyError if the vector does not come from a neighbor'''
    def test_updateRoutingTable(self):
        '''Test updating the routing table via the Bellman-Ford algorithm'''
if __name__ == '__main__':
    unittest.main()        
