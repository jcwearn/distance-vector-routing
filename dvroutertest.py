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
        router1 = dvrouter.DVRouter('A')
        router1.addLink('B', 1.5)
        table1 = router1.getRoutingTable()
        self.assertEqual(table1['B'], 1.5)

        router2 = dvrouter.DVRouter('B')
        router2.addLink('C', 2.5)
        table2 = router2.getRoutingTable()
        self.assertEqual(table2['C'], 2.5)
        
    def test_removeLink(self):
        '''Test removing a link from a neighbor'''
        router1 = dvrouter.DVRouter('A')
        router1.addLink('B', 1.5)
        table1 = router1.getRoutingTable()
        self.assertIn('B', table1)
        router1.removeLink('B')
        self.assertNotIn('B', table1)
        
    def test_exportDistanceVector(self):
        '''Test exporting distance vectors to a neighbor. If split horizon is on, should not advertize a route whose first hop is some neighbor to that neighbor'''
        router1 = dvrouter.DVRouter('A')
        router1.addLink('B', 1.5)
        router1.addLink('C', 2)
        expectedTable = {'B': 1.5, 'C': 2}
        self.assertEqual(router1.exportDistanceVector('B'), expectedTable)
        
    def test_importDistanceVectors(self):
        '''Test importing a list of distance vectors.  It should raise a KeyError if the vector does not come from a neighbor'''
        router1 = dvrouter.DVRouter('A')
        router1.addLink('B', 1.5)
        router1.addLink('C', 2)

        router2 = dvrouter.DVRouter('B')
        router2.addLink('A', 1.5)
        router2.addLink('C', 4)
        neighborTable1 = router2.getRoutingTableExclusive()

        router3 = dvrouter.DVRouter('C')
        router3.addLink('A', 2)
        router3.addLink('B', 4)
        router3.addLink('D', 1)
        neighborTable2 = router3.getRoutingTableExclusive()        
        
        expectedTable = {'A': {'C': 2, 'B': 1.5}, 'C': {'A': 2, 'B': 4, 'D': 1}, 'B': {'A': 1.5, 'C': 4}}
        router1.importDistanceVectors({'B':neighborTable1, 'C':neighborTable2})
        self.assertEqual(router1.getImportedTables(), expectedTable)

    def test_updateRoutingTable(self):
        '''Test updating the routing table via the Bellman-Ford algorithm'''
        router1 = dvrouter.DVRouter('A')
        router1.addLink('B', 1.5)
        router1.addLink('C', 2)

        router2 = dvrouter.DVRouter('B')
        router2.addLink('A', 1.5)
        router2.addLink('C', 4)
        neighborTable1 = router2.getRoutingTableExclusive()

        router3 = dvrouter.DVRouter('C')
        router3.addLink('A', 2)
        router3.addLink('B', 4)
        neighborTable2 = router3.getRoutingTableExclusive()

        neighborTables = router1.formatNeighborTables([router2, router3])
        
        router1.importDistanceVectors(neighborTables)
        router1.updateRoutingTable()
        
if __name__ == '__main__':
    unittest.main()        
