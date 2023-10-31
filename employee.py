class Employee:
    raise_amount = 1.04
    
    def __init__(self, last: str, first: str, pay: int):
        self.last = last
        self.first = first
        self.pay = pay
    
    @property
    def email (self):
        return'{}.{}@gmail.com'.format(self.last, self.first)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay *= self.raise_amount
        return self.pay
    
    