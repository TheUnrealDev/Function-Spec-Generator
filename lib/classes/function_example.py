class Example():
    def __init__(self, funcName, arguments, result):
        self.funcName = funcName
        self.arguments = arguments
        self.result = result

    def __str__(self):
        formattedString = "@example\n"
        formattedString += f"* // results in {self.result}\n"
        argumentString = ""
        for i, argument in enumerate(self.arguments):
            if i == 0:
                argumentString += argument
            else:
                argumentString += f", {argument}"
        formattedString += f"* {self.funcName}({argumentString});"
        return formattedString
