import unittest
import dvector

class TestDVector(unittest.TestCase):
    def test_constructor(self):
        '''test that a newly created DVector has a route to inself but to no other node'''
        dv = dvector.DVector('A')
        self.assertEqual(len(dv.destinations()), 1)
        self.assertEqual(dv.distance('A'),0)
    
    def test_destinations(self):
        '''test destination method which returns a list of all destinations to which we have a distance'''
        dv = dvector.DVector('A')
        
        dv.loadRoute('B', 4.5)
        self.assertEqual(len(dv.destinations()), 2)
        self.assertIn('B', dv.destinations())

        dv.loadRoute('C', 4.5)
        self.assertIn('B', dv.destinations())
        self.assertIn('C', dv.destinations())
        self.assertEqual(len(dv.destinations()),3)

        dv.loadRoute('D', 6.5)
        self.assertIn('B', dv.destinations())
        self.assertIn('C', dv.destinations())
        self.assertIn('D', dv.destinations())
        self.assertEqual(len(dv.destinations()), 4)
        

    def test_distance(self):
        '''test distance method that returns the distance from nodeName to 'destination from our distance dictorary, or infinity if there is no entry for 'destination' in our distance dictorart'''
        dv = dvector.DVector('A')
        self.assertEqual(dv.distance('A'), 0)
        
        dv.loadRoute('B', 4.5)
        self.assertEqual(dv.distance('B'), 4.5)

        dv.loadRoute('C', 5)
        self.assertEqual(dv.distance('C'), 5)

        dv.loadRoute('D', 7)
        self.assertEqual(dv.distance('D'), 7)

        self.assertEqual(dv.distance('E'), 16)

    def test_loadRoute(self):
        '''test load route method which adds a route to 'destination' with the distance 'dist' '''
        dv = dvector.DVector('A')

        dv.loadRoute('B', 4.5)
        self.assertIn('B', dv.destinations())
        self.assertEqual(dv.distance('B'), 4.5)

        dv.loadRoute('C', 5.5)
        self.assertIn('C', dv.destinations())
        self.assertEqual(dv.distance('C'), 5.5)

        dv.loadRoute('D', 2)
        self.assertIn('D', dv.destinations())
        self.assertEqual(dv.distance('D'), 2)

    def test_removeRoute(self):
        '''test removeRoute method which removes a route 'destination' from a routing table '''
        dv = dvector.DVector('A')
        dv.loadRoute('B', 4.5)
        self.assertIn('B', dv.destinations())
        dv.removeRoute('B')
        self.assertNotIn('B', dv.destinations())

        dv = dvector.DVector('B')
        dv.loadRoute('C', 4)
        self.assertIn('C', dv.destinations())
        dv.removeRoute('C')
        self.assertNotIn('C', dv.destinations())

if __name__ == '__main__':
    unittest.main()
