class Car:
    def __init__(self, color, make, model, year, amount:float):
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.amount = amount
    
    def __str__(self) -> str:
        return f'A {self.color} {self.make} {self.model} made in {self.year} cost {self.amount}'
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Car):
            return (
            self.make == other.make
            and self.model == other.model
            and self.year == other.year
            )
        else:
            return False
        
    def __add__(self, other)->float:
        if isinstance(other, Car):
            total_cost = self.amount + other.amount
            return f'The addition of cost of {self.make} car and {other.make} car is: \n{total_cost}'
        else:
            return NotImplemented
        
    def __sub__ (self, other)->float:
        if isinstance(other, Car):
            cost = self.amount - other.amount
            return f'The difference in the cost of {self.make} car and {other.make} car is: \n{round(cost,2)}'
        else:
            return NotImplemented
car1 = Car('Red', 'Chevrolet', 'Camaro', 2023, 75800.50)
car2 = Car('Black', 'Bugatti', 'Cheyron', 2023, 88580.95)
car3 = Car('Black', 'Chevrolet', 'Camaro', 2023, 77900.88)
print(car1)
print(car2)
print(car1==car2)
print(car1==car3)
print(car2==car3)
print(car1 + car2)
print(car3-car1)
