def calc_math_expression_from_str(str_input):
    list_string = str_input.split(',')
    num1 = float(list_string[0])
    num2 = float(list_string[1])
    operator = list_string[2]
    print(num1)
    print(num2)
    print(operator)

print(calc_math_expression_from_str('1,2,+'))
