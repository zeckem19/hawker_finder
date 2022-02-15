from helper import find_distance

class TestHelper:
    def test_find_distance(self):
        '''assert that function has less than 0.1% error'''
        assert 1359000 < find_distance([40.0,40.0], [50.0,50.0]) < 1360000