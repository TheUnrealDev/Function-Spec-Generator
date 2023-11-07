from classes.function_specification import FunctionSpecification
from classes.function_example import Example
from classes.parameter import Parameter
from classes.return_value import ReturnValue
from user_interface import (
    getValidatedStringInput,
    validateYesAndNoResponse,
    clearScreen,
    previewFunctionSpec
)


def createExample(funcName):
    clearScreen()
    arguments = []
    while True:
        newArgument = input(f"Please enter argument {len(arguments) + 1} " +
                            "passed to the function\n" + "(or leave this empty to not add any more):\n")

        newArgument.strip()
        if newArgument != "":
            arguments.append(newArgument)
        else:
            break

    result = input("Please enter the result of the above example: ")
    return Example(funcName, arguments, result)


def getExamples(funcSpecification):
    while True:
        clearScreen()
        previewFunctionSpec(funcSpecification)
        shouldCreateExample = getValidatedStringInput(
            "Do you want to add an example usage? [y/n]: ",
            validateYesAndNoResponse)
        if shouldCreateExample == 'y':
            example = createExample(funcSpecification.functionName)
            funcSpecification.addExample(example)
        else:
            break


def createParam():
    name = input("Please enter the name of the parameter: ")
    dataType = input("Please enter the data type of the parameter: ")
    description = input("Please enter a description for the parameter: ")

    return Parameter(name, dataType, description)


def getParams(funcSpecification):
    while True:
        clearScreen()
        previewFunctionSpec(funcSpecification)
        shouldAdd = getValidatedStringInput(
            "Do you want to add a parameter? [y/n]: ",
            validateYesAndNoResponse)
        if shouldAdd == 'y':
            previewFunctionSpec(funcSpecification)
            param = createParam()
            funcSpecification.addParameter(param)
        else:
            break


def createPrecondition():
    precondition = input("Please enter your precondition: ")
    return precondition


def getPreconditions(funcSpecification):
    while True:
        clearScreen()
        previewFunctionSpec(funcSpecification)
        shouldAdd = getValidatedStringInput(
            "Do you want to add a precondition? [y/n]: ",
            validateYesAndNoResponse)
        if shouldAdd == 'y':
            precondition = createPrecondition()
            funcSpecification.addPrecondition(precondition)
        else:
            break


def createReturnValue():
    dataType = input("Please enter the data type of the return value: ")
    description = input("Please enter a description for return value: ")
    return ReturnValue(dataType, description)


def addReturnValue(funcSpecification):
    clearScreen()
    previewFunctionSpec(funcSpecification)
    shouldAdd = getValidatedStringInput(
        "Do you want to add a return value? [y/n]: ",
        validateYesAndNoResponse)
    if shouldAdd == 'y':
        returnValue = createReturnValue()
        if returnValue != None:
            funcSpecification.setReturnValue(returnValue)


def addDescription(funcSpecification):
    description = input("Please enter a description for your function: ")
    funcSpecification.setDescription(description)


def create_function_specification():
    funcName = getValidatedStringInput("Function Name: ")
    funcSpecification = FunctionSpecification(funcName)

    addDescription(funcSpecification)
    getExamples(funcSpecification)
    getParams(funcSpecification)
    getPreconditions(funcSpecification)
    addReturnValue(funcSpecification)

    return funcSpecification
