from classes.data import Data


class Parameter(Data):
    def __init__(self, name, dataType, description):
        super().__init__(dataType, description)
        self.name = name

    def __str__(self):
        return f"@param {{{self.dataType}}} {self.name} - {self.description}"
