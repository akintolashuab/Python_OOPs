def total(xs: list[float]) -> float:
    '''addition of numbers'''
    result = 0
    for x in xs:
        result+=x
    return result

print(total([1,3,4,5,6]))

def join(xs: list[int], delimiter: str) -> str:
    '''Takes list of integers as input and return the list as string'''
    generated_string = ''
    for x in xs:
        if generated_string == '':
            generated_string = str(x)
        else:
            generated_string += delimiter + str(x)    
    return generated_string

