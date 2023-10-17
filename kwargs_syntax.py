# EXAMPLE 1
# def print_details(**kwargs):
#     print(f"kwargs:{kwargs}")
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
        
# print_details(name = "Jill", age = 30, city = "Lagos")

# EXAMPLE 2
# def describe_fish(fish_name, **kwargs):
#     color = kwargs.get("color", "unknown color")  # if we dont provide color it will use unknown
#     habitat = kwargs.get("habitat", "unknown habitat") # if we dont provide habitat it will use unknown
#     fins = kwargs.get("fins", 0)        # if we dont provide fins it will use 0
#     description = f"A {fish_name} is an {color} fish that inhabits in {habitat} habitat. " \
#                     f"It has {fins} fins" # the backslash means it is continuation. Escape character
#     return description
# #result = describe_fish(fish_name= "Goldfish", color = "blue coloured", habitat = "Acquarium", fins = 4)
# #result = describe_fish("Goldfish", habitat = "Acquarium", fins = 4)
# #result = describe_fish(fish_name= "Goldfish", fins = 4)
# result = describe_fish(fish_name= "Goldfish", color ="red coloured")
#print(result)

# EXAMPLE 3
# def list_numbers(first, second, third):
#     print("First number is:", first)
#     print("Second number is:",second)
#     print("Third number is:", third)
    
# #list_numbers("One", "Two", "Three")
# numbers = {"first": 1, "second":2, "third":3}
# #list_numbers(**numbers)
# list_numbers(*numbers.values())

#EXAMPLE 4
def process_data(name: str, *args, age = 0, **kwargs): #combine positional arg, arg syntax, keyword and kwargs
    print(f"process data: {name}")
    print(f"process args: {args}")
    print(f"Age: {age}")
    print(f"process Kwargs: {kwargs}")
    
process_data("Torres", 1,2,4,"basketball", age=46, Country= "Spain", Language = "Spanish")