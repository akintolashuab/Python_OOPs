# class Employee:
#     number_of_emps = 0
#     raise_amount = 1.04
    
#     def __init__(self, last: str, first: str, pay: int):
#         self.last = last
#         self.first = first
#         self.pay = pay
#         self.email = last + '.' + first + '@sample.com'
        
#         Employee.number_of_emps +=1
        
#     def fullname(self):
#         return '{} {}'.format(self.last, self.first)
    
#     def apply_raise(self)-> float:
#         self.pay = self.pay*self.raise_amount

# import random
# def random_power():
#     def f(x):
#         return x**2
#     def g(x):
#         return x**3
#     def h(x):
#         return x**4
    
#     functions = [f,g,h]
#     return random.choice(functions)
# for i in range(10):
#     p = random_power()
#     print(p(i))
    
# print(8**4)
    
    
# class Employee:
#     number_of_emps = 0
#     raise_amount = 1.04
    
#     def __init__(self, last: str, first: str, pay: int):
#         self.last = last
#         self.first = first
#         self.pay = pay
#         self.email = last + '.' + first + '@sample.com'
        
#         Employee.number_of_emps +=1
        
#     def fullname(self):
#         return '{} {}'.format(self.last, self.first)
    
#     def apply_raise(self)-> float:
#         self.pay = self.pay*self.raise_amount
    
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount        

#     @classmethod #alternative constructor
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, int(pay))
        
# #emp_1 = Employee('Akintola', 'Shuab', 50000)
# # emp_2 = Employee('Ademola', 'Isiaq', 74000)

# # Employee.upward_amount(1.10)
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)


# employee_1 = 'Akintola-Shuab-50000'
# employee_2 = 'Ademola-Isiaq-74000'

# result = Employee.from_string(employee_1)
# print(result.pay)
# print(result.apply_raise())

class Employee:
    number_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, last: str, first: str, pay: int):
        self.last = last
        self.first = first
        self.pay = pay
        self.email = last + '.' + first + '@sample.com'
        
        Employee.number_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay *= self.raise_amount
        return self.pay
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    #Alternative constructor.   
    @classmethod
    def from_string(cls, emp_str):  
        first, last, pay = emp_str.split('-')
        return cls(last, first, int(pay))  # Use cls instead of Employee to create an instance
    
    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5)| (day.weekday() == 6):
            return f'It is a Weekend'
        else:
            return f'It is a Weekday'
        
    @staticmethod
    def from_timestamp(tim):
        y,m,d,h,mm,s, weekday, jday, jst = time.localtime(tim)
        return (y,m,d,h,mm,s, weekday, jday, jst)
    

# Example usage
employee_1 = 'Akintola-Shuab-50000'
employee_2 = 'Ademola-Isiaq-74000'

result1 = Employee.from_string(employee_1)
result2 = Employee.from_string(employee_2)

#print(result1.fullname())
print(result1.apply_raise())  # Print the updated pay after applying raise

#print(result2.fullname())
print(result2.apply_raise())  # Print the updated pay after applying raise

# result = Employee.from_string(employee_1)
# print(result.pay)
# print(result.apply_raise())
import datetime
my_date = datetime.date(2023, 10, 16)
print(Employee.is_workday(my_date))

import time

# Get the current timestamp (seconds since the epoch)
current_timestamp = time.time()
print(Employee.from_timestamp(1697108661.969087))

print(time.time())