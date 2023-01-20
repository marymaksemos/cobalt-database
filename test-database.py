import unittest
import os
import pickle
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_db.pkl'
        self.db = Database(self.file_path)

    def test_init_creates_file(self):
        self.assertTrue(os.path.exists(self.file_path))

    def test_init_loads_data(self):
        data = {'key': 'value'}
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)
        db = Database(self.file_path)
        self.assertEqual(db.data, data)
 
    def test_save_data(self):
        data = {'key': 'value'}
        self.db.save('key', data)
        with open(self.file_path, 'rb') as f:
            loaded_data = pickle.load(f)
        self.assertEqual(loaded_data, {'key': data})

    def tearDown(self):
        os.remove(self.file_path)
