class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self):
        print(f'{self.name} attacks')

class Dragon(Monster):
    def __init__(self, name, health, element):
        super().__init__(name, health)
        self.element = element
    
    def attack(self):
        print(f'{self.name} breathes {self.element}')
    
class Goblin (Monster):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon
        
    def attack(self):
        print(f'{self.name} swings a {self.weapon}')
        
def attack(monster):
    monster.attack()
    
rat = Monster('rat', 10)
goblin = Goblin('goblin', 100, 'sword')
dragon = Dragon('dragon', 80, 'fire')
    
attack(rat)
attack(goblin)
attack(dragon)