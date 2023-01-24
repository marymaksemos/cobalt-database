import unittest
from cobalt import Cobalt


sample_dict = {
    '0': {'name': 'Simon', 'age': 20, 'role': 'Developer'},
    '1': {'name': 'Saeed', 'age': None, 'role': 'Scrum master'},
    '2': {'name': 'Mary', 'age': None, 'role': 'Developer'},
    '3': {'name': 'Jannat', 'age': None, 'role': 'Developer'},
}


class TestDatabase(unittest.TestCase):

    def test_fetch(self):
        cbd = Cobalt()
        
        [cbd.save(key, obj) for key, obj in sample_dict.items()]

        for key, obj in sample_dict.items():
            for item in obj:
                self.assertEqual(cbd.fetch(key, item), sample_dict[key][item])
