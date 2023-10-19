class Date:
    ''' This class return integer of date 
    
    '''
    def __init__(self, year:int, month:int, day:int) -> int:
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def from_string(cls, date_string, sep = '-'):
        ''' This take any input of date format and return normal date 
    '''
        year, month, day = map(int, date_string.split(sep))
        return cls(year, month, day)

inst_1 = Date(2023, 12, 35)
print(inst_1.day)