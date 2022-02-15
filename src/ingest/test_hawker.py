from hawker import HawkerCentre
from datetime import datetime

class TestHawkerObject:
    def test_hawker_object(self):
        test_date = datetime.now()
        expected = {
            "creation_timestamp":test_date,
            "name":"Test hawker",
            "photourl":"http://example.com",
            "loc":{ "type": "Point", "coordinates": [ 103.938732580554003, 1.33198706861747] }}
        actual = HawkerCentre(
            creation_timestamp=test_date,
            name="Test hawker",
            photourl="http://example.com",
            loc={ "type": "Point", "coordinates": [ 103.938732580554003, 1.33198706861747] }
            )
        assert expected == actual.dict()
        