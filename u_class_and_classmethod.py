class Date:
    ''' This class return integer of date 
    
    '''
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string, diff = '-'):
        ''' This take any input of date format and return normal date 
    '''
        year, month, day = map(int, date_string.split(diff))
        return cls(year, month, day)
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def multiply(a,b):
        return a*b
    
    @staticmethod
    def power(a,b):
        return a**b
    

#inst_1 = Date(2023, 12, 35)
inst_1 = Date.from_string('2018$08$01', '$')
print(inst_1.year)
inst_2 = Date.power(2,3)
print(inst_2)