from unittest.main import main


def check_valid_expression(exp):
    operands = exp.split()[::2]
    operators = exp.split()[1::2]

    # check for appropriate operators
    if not set(operators).issubset(set(["+", "-"])):
        return "Error: Operator must be '+' or '-'."

    # check for only digits in operands
    if not all([x.isdigit() for x in operands]):
        return "Error: Numbers must only contain digits."

    # check each operand has max four digits
    if not all([len(x) <= 4 for x in operands]):
        return "Error: Numbers cannot be more than four digits."

    return


def format_expression(exp, solve):
    operand1, operator, operand2 = exp.split()
    width = max(len(operand1), len(operand2)) + 2

    line1 = operand1.rjust(width)
    line2 = operator + operand2.rjust(width - 1)

    if solve == True:
        if operator == "+":
            ans = int(operand1) + int(operand2)
        else:
            ans = int(operand1) - int(operand2)
        return [line1, line2, width * "-", str(ans).rjust(width)]
    else:
        return [line1, line2, width * "-"]


def format_all_problems(formatted_problems):
    nrows = len(formatted_problems[0])
    result = ""

    for i in range(nrows):
        row = [exp[i] for exp in formatted_problems]
        row = "    ".join(row)
        result += row + "\n"

    return result[:-1]


def arithmetic_arranger(problems, solve=False):

    # check for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # other error checking (only addition/subtraction, only digits, operands 4 digits or less)
    for exp in problems:
        error = check_valid_expression(exp)

        if error is not None:
            return error

    result = [format_expression(exp, solve) for exp in problems]

    return format_all_problems(result)
