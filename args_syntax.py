# def animal_names(species, *names):
#     name_str = ', '.join(names)
#     message = f"{species} names: {name_str}"
#     return message

# result = animal_names("Dog", "Jack", "James", "Johnbull")
# print(result)

def add(*args):
    total = 0
    for i in args:
        total += i
        if total >= 10:
                break
    return total
print(add(2,9,4,5,6))
        
        
