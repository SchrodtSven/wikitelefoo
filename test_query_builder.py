import unittest
import string
from wtf_base import WTFQueryBuilder

class TestQueryBuilder(unittest.TestCase):

    def test_basix(self):
        qb = WTFQueryBuilder()
        self.assertEqual(qb.search_entities('Orthopädie'), 'https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=de&search=Orthop%C3%A4die')

if __name__ =='__main__':
    unittest.main()
    
    
    
    