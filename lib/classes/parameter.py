from data import Data

class Parameter(Data):
    def __init__(self, name, dataType, description, id):
        super().__init__(dataType, description)
        self.name = name
        self.id = id

    def __str__(self):
        return ""