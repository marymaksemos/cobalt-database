import pickle


class Database:
     """
    A class for saving  python objects to and from a file on disk.
    The objects are saved and accessed via a key (of type str).
    """
    def __init__(self, file_path):
        """
        Initialize the database by loading the data from the file if it exists.
        If the file does not exist, create an empty file.
        :paramter file_path: the path to the file where the data will be stored.
        """
        self.data = {}
        self.file_path = f'{file_path}_db.pkl'
        try:
            with open(self.file_path, "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            with open(self.file_path, "wb") as f:
                pickle.dump(self.data, f)

    def save(self, key, obj):
        """
        Save an object to the database with the given key.
        :param key: a string representing the key of the object.
        :param obj: the object to be saved.
        """
        self.data[key] = obj
        with open(self.file_path, "wb") as f:
            pickle.dump(self.data, f)
