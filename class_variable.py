# class MyClass:
#     class_variable = 10  # This is a class variable

#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable

# # Accessing the class variable
# print(MyClass.class_variable)  # Outputs: 10

# # Creating instances and accessing instance variables
# obj1 = MyClass(20)
# obj2 = MyClass(30)

# print(obj1.instance_variable)  # Outputs: 20
# print(obj2.instance_variable)  # Outputs: 30

# # Even though we access the class variable using an instance, it's the same for all instances
# print(obj1.class_variable)  # Outputs: 10
# print(obj2.class_variable)  # Outputs: 10
# print(obj1.__class__)


# class Employee:
#     number_of_emp = 0
#     raise_amount = 1.04
#     def __init__(self, last, first, pay):
#         self.last = last
#         self.first = first
#         self.pay = pay
#         self.email = last + '.' + first + '@example.com'
#         Employee.number_of_emp +=1
        
#     def fullname(self):
#         return ('{} {}').format(self.last, self.first)
    
#     def apply_raise(self):
#         self.pay = self.pay* self.raise_amount
        
    
# emp1 = Employee('Ademola', 'Lukman', 80000)
# emp2 = Employee('Adekola', 'Baliqis', 60000)
# print(Employee.number_of_emp)

# # print(emp1.pay)
# # emp1.apply_raise()
# # print(emp1.pay)

# print(emp1.raise_amount)
# print(Employee.raise_amount)
# print(emp2.raise_amount)
    

# class Pizza:
#     """A Class to initialize instance variables"""
#     tax: float = 1.06
#     def __init__(self, size: str, toppings: int, extra_cheese: bool):
#         self.size = size
#         self.toppings = toppings
#         self.extra_cheese = extra_cheese
        
#     def price(self)-> float:
#         """A classmethod to calculate Price of a Pizza"""
#         total = 0.0
#         if self.size == 'Large':
#             total += 10.00
#         else:
#             total += 8.00
        
#         if self.extra_cheese:
#             total += 1
#         if self.toppings >= 4:
#             total += 5.00
#         else:
#             total += 1
            
#         total*= self.tax
#         return total
        
# first_pizza = Pizza('Large', 6, True)
# print(first_pizza.tax)
# Pizza.tax = 1.20
# print(first_pizza.price())
# # if __name__ == '__main__':
# #     price


class Employee:
    number_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, last: str, first: str, pay: int):
        self.last = last
        self.first = first
        self.pay = pay
        self.email = last + '.' + first + '@sample.com'
        
        Employee.number_of_emps +=1
        
    def fullname(self):
        return '{} {}'.format(self.last, self.first)
    
    def apply_raise(self)-> float:
        self.pay = self.pay*self.raise_amount
print(Employee.number_of_emps)
emp_1 = Employee('Akintola', 'Shuab', 50000)
emp_2 = Employee('Ademola', 'Isiaq', 74000)
print(emp_1.fullname())
print(emp_1.apply_raise())
print(emp_1.pay)
print(emp_2.fullname())
print(emp_2.apply_raise())
print(emp_2.pay)
#print(Employee.number_of_emps)
print(emp_2.number_of_emps)
