def add(a:int,b:int)-> int:
    '''Returns the sum of two number
    '''
    return a+b 

def multiply(a:int,b:int)-> int:
    '''Returns the sum of two number
    '''
    return a*b 

def subtract(a:int,b:int)-> int:
    '''Returns the sum of two number
    '''
    return a-b 

def add(a:int,b:int)-> int:
    '''Returns the sum of two number
    '''
    return a+b 

def division(a:int,b:int)-> int:
    '''Returns the sum of two number
    '''
    if b == 0:
        return ValueError ('Cannot divide by Zero')
    else:
        return int(a/b)


print(division(4,2))