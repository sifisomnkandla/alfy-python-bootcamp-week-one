
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    if (num1 >= num2) and (num1 >= num3):
        max_num = num1
    elif (num2 >= num1) and (num2 >= num3):
        max_num = num2
    else:
        max_num = num3
    return max_num


find_largest_and_smallest_numbers()
