class FunctionSpecification():
    functionName = ''
    description = ''
    examples = []
    parameters = []
    preconditions = []
    returnValue = None

    def __init__(self, functionName):
        self.functionName = functionName

    def addExample(self, example):
        self.examples.append(example)

    def setDescription(self, description):
        self.description = description

    def addParameter(self, newParameter):
        self.parameters.append(newParameter)

    def addPrecondition(self, precondition):
        self.preconditions.append(precondition)

    def setReturnValue(self, returnValue):
        self.returnValue = returnValue
    """
    /**
    * Drops a number of items from the front of a list.
    * @example
    * // results in list(3, 4, 5)
    * drop(2, list(1, 2, 3, 4, 5));
    * @param {number} count - number of items to drop
    * @param {list} xs - input list
    * @precondition count is not negative.
    * @returns {list} Returns the input list xs without its first count elements.
    */
    """

    def formatSpecification(self):
        string = "/**\n"
        string += f"* {self.description}\n"

        for example in self.examples:
            string += f"* {str(example)}\n"

        for param in self.parameters:
            string += f"* {str(param)}\n"

        for precondition in self.preconditions:
            string += f"* @precondition {precondition}\n"

        if self.returnValue != None:
            string += f"* {str(self.returnValue)}\n"
        string += "*/"

        return string
