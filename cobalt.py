import database


class Cobalt:
    """
    This is the main class for Cobalt Database.
    This class provides methods to retrieve and save data to-and-from database.
    """

    def __init__(self, db_path: str = 'db', db_name: str = 'cobalt'):
        """
        Creates a database db object & copies data to a new dict.
        """
        db = database.Database(f'{db_path}/{db_name}')
        self.data = db.data.copy()
        self.save = db.save

    def fetch(self, key, obj):
        data = self.data
        retrieved_data = data[key][obj]
        return retrieved_data
