def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    result = a / b
    return round(result, 2)

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    reversed_s = s[::-1]
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case

def get_list_element(lst, index):
    return lst[index] 
