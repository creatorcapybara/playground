def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top = []
    bottom = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts
        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        width = max(len(num1), len(num2)) + 2
        top.append(num1.rjust(width))
        bottom.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)
            
        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else: 
                result = str(int(num1) - int(num2))
            answers.append(result.rjust(width))

    arranged = '    '.join(top) +  '\n' + \
               '    '.join(bottom) + '\n' + \
               '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(answers)
    return arranged
print(arithmetic_arranger(["3 / 855", "3801 - 2"]))