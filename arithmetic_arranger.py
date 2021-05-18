from unittest.main import main


def check_valid_expression(exp):
    operators = exp.split()[1::2]
    operands = exp.split()[::2]

    # check for appropriate operators
    if not set(operators).issubset(set(["+", "-"])):
        return "Error: Operator must be '+' or '-'."

    # check for only digits in operands
    if not all([x.isdigit() for x in operands]):
        return "Error: must only contain digits."

    # check each operand has max four digits
    if not all([len(x) > 4 for x in operands]):
        return "Error: Numbers cannot be more than four digits."

    return


def arithmetic_arranger(problems, solve=False):

    # check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    for exp in problems:
        error = check_valid_expression(exp)

        if error is not None:
            return error

    arranged_problems = []

    return arranged_problems
