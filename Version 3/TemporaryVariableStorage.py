import os
import pickle

class TemporaryVariable:
    _path = "tempvarstore/"

    def __init__(self, variable_name):
        self.variable_name = variable_name

        if not os.path.exists(self._path):
            os.makedirs(self._path)

    def set_value(self, value):
        try:
            with open(f'{self._path}{self.variable_name}.pickle', 'wb') as f:
                pickle.dump(value, f)
        except Exception as e:
            print(f"An error occurred while storing {self.variable_name}: {e}")

    def get_value(self):
        try:
            with open(f'{self._path}{self.variable_name}.pickle', 'rb') as f:
                value = pickle.load(f)
            return value
        except FileNotFoundError:
            print(f"File '{self.variable_name}.pickle' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while retrieving {self.variable_name}: {e}")
            return None
