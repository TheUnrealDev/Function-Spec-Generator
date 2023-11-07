from data import Data

class ReturnValue(Data):
    def __init__(self, dataType, description):
        super().__init__(dataType, description)

    def __str__(self):
        return ""