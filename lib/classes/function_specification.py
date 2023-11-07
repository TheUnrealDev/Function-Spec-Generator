class FunctionSpecification():
    functionName = ''
    description = ''
    parameters = []
    returnValue = None
    def __init__(self, functionName):
        self.functionName = functionName

    def addDescription(self, description):
        self.description = description

    def addParameter(self, newParameter):
        self.parameters.append(newParameter)
    
    def addReturnValue(self, returnValue):
        self.returnValue = returnValue