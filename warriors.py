class Warrior:
    def __init__(self, resource, health, damage, horizontalMove, verticalMove, crossMove):
        self.resource = resource
        self.health = health
        self.damage = damage
        self.horizontalMove = horizontalMove
        self.verticalMove = verticalMove
        self.crossMove = crossMove
        

class Guard(Warrior):
    def __init__(self):
        super().__init__(resource = 10, heath = 80, damage = 20, horizontalMove = 1, verticalMove = 1, crossMove = 1)


class Archer(Warrior): 
    def __init__(self): # Damage = Hp %60
        super().__init__(resource = 20, heath = 30, damage = 60, horizontalMove = 2, verticalMove = 2, crossMove = 2)

class Artilleryman(Warrior):
    def __init__(self): # Damage = Hp %100
        super().__init__(resource = 50, heath = 30, damage = 100, horizontalMove = 2, verticalMove = 2, crossMove = 0)

class Horseman(Warrior):
    def __init__(self):
        super().__init__(resource = 30, heath = 40, damage = 30, horizontalMove = 0, verticalMove = 0, crossMove = 3)

class Healer(Warrior):
    def __init__(self):# Damage = Heals %50 Hp
        super().__init__(resource = 10, heath = 100, damage = 50, horizontalMove = 2, verticalMove = 2, crossMove = 2)