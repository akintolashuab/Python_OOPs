class Employee:
    num_of_emp = 0
    raise_amount = 1.05
    def __init__(self, last, first, pay):
        self.last = last
        self.first = first
        self.pay = pay
        self.email = last + '.' + first +'@mail.com'
        
        Employee.num_of_emp += 1
    def fullname(self):
        return '{} {}'.format(self.last, self.first)
    
    def apply_raise_amount(self):
        self.pay *= self.raise_amount
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, string):
        last, first, pay = string.split('-')
        return cls(last, first, int(pay))
    
# INHERITANCE and SUBCLASS

class Developer(Employee):
    ''' A demo of inheritance and subclass'''
    raise_amount = 1.15
    def __init__(self, last, first, pay, prog_lang):
        super().__init__(last, first, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    '''A subclass'''
    raise_amount = 1.30
    def __init__(self, last, first, pay, employees = None):
        super().__init__(last, first, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            #print(len(self.employees))
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('---->', emp.fullname())
        
mgr_1 = Manager('Sue', 'Smith', 87500, None)
dev_1 = Developer('Akinmorin', 'George', 88000, 'java')
dev_2 = Developer('John', 'Stone', 76000, 'Python')
mgr_1.add_employee(dev_1)
mgr_1.add_employee(dev_2)
print(mgr_1.email)
#mgr_2.apply_raise_amount()
#print(mgr_2.pay)
print(mgr_1.pay)
print(Manager.num_of_emp)
print(mgr_1.employees)
mgr_1.remove_employee(dev_1)
# mgr_1.add_employee('Camil')
# mgr_1.add_employee('Stones')
# mgr_1.add_employee('Brooklyn')
#print(mgr_1.employees)
mgr_1.print_emps()
# dev_1 = Developer('Akinmorin', 'George', 88000, 'java')
# dev_2 = Developer('John', 'Stone', 76000, 'Python')
# print(dev_1.email)
# dev_2.apply_raise_amount()
# print(dev_2.pay)
# print(dev_1.pay)
# print(Developer.num_of_emp)

#print(help(Developer)) to check for the ranking of the inheritance
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Employee.set_raise_amount(1.10)
# emp_1 = Employee('Akinmorin', 'George', 88000)
# emp_2 = Employee('John', 'Stone', 76000)
# emp_2.apply_raise_amount()
# print(emp_2.pay)
# # print(Employee.num_of_emp)
# print(76000*1.10)
# emp_3 = Employee.from_string('John-Stone-76000')
# emp_3.apply_raise_amount()
# emp_3.set_raise_amount(1.10)
# print(emp_3.pay)