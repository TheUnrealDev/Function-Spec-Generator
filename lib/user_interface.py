from os import system


def clearScreen():
    system("cls")


def previewFunctionSpec(funcSpecification):
    clearScreen()
    print("PREVIEW\n")
    print(funcSpecification.formatSpecification())
    print(f"\n{'-' * 20}\n")


def getValidatedStringInput(prompt, validationFunc=None):
    while True:
        string = input(prompt)

        invalidInputMessage = None
        if validationFunc != None:
            invalidInputMessage = validationFunc(string)

        if invalidInputMessage == None:
            return str.strip(string)
        else:
            print(invalidInputMessage)


def validateYesAndNoResponse(string):
    if not string.strip().lower() in ["y", "n"]:
        return "Your answer needs to be 'y' or 'n'!"
