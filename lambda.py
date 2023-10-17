#syntax for a lambda
#lambda arguments: expression on a single line use for simple function
# Example
# square = lambda x: x**2
# print(square(2))

# y = list((1,2,3,4,5))
# print(y)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# square_numbers = list(map(lambda x: x**2, numbers))
# print(square_numbers)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# square_numbers = list(filter(lambda x: x%2 ==0, numbers))
# print(square_numbers)

def apply_operation(x,y, operation = lambda a,b: a+b):
    return operation(x,y)
multiply = lambda a,b: a*b

add = apply_operation(5,8)
multi = apply_operation(7,8,multiply)
print(add)
print(multi)

