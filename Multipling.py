def multiply_tuple_elements(tuple):
    result = 1
    for item in tuple:
        result *= item
    return result

my_tuple = (2, 3, 4, 5)
print(multiply_tuple_elements(my_tuple))