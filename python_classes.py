# class MyClass:
#     # Class variable
#     class_variable = 10

#     # Constructor or initializer method
#     def __init__(self, name):
#         self.name = name

#     # Instance method
#     def greet(self):
#         return f"Hello, {self.name}!"

# # Creating an instance of the class
# my_instance = MyClass("Alice")

# # Accessing attributes and calling methods
# print(my_instance.name)  # Output: Alice
# print(my_instance.greet())  # Output: Hello, Alice!
# print(MyClass.class_variable)  # Output: 10



# class Employee:
#     def __init__(self, first, last, pay: int):
#         self.fname = first
#         self.lname = last
#         self.pay = pay
#         self.email = first + '.' + last + '@example.com'
        
#     def fullname(self):
#         return('The full name is {} {}'.format(self.lname, self.fname))
# emp_1 = Employee('Shuab', 'Akintola', 70000)
# emp_2 = Employee('Brighto', 'Indiana', 56000)

# print(emp_1.email)
# print(emp_1.fullname())

# if __name__ == '__main__':
#     Employee

from class_variable import Pizza
#import class_variable
first_instance = Pizza('Large', 7, True)
first_instance.tax = 1.20
print(first_instance.price())