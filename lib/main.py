from create_function_spec import create_function_specification
from user_interface import (
    getValidatedStringInput,
    validateYesAndNoResponse,
    previewFunctionSpec
)

import pyperclip


def onFunctionSpecCreated(funcSpecification):
    previewFunctionSpec(funcSpecification)

    shouldCopy = getValidatedStringInput(
        "Do you want to copy this to your clipboard? [y/n]: ",
        validateYesAndNoResponse)
    if shouldCopy:
        pyperclip.copy(funcSpecification.formatSpecification())
        print("Success!")


def createFunctionSpec():
    funcSpecification = create_function_specification()
    onFunctionSpecCreated(funcSpecification)


if __name__ == '__main__':
    createFunctionSpec()
