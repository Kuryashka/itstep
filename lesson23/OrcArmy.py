class OrcArmy:
    
    def __init__(self, warrior_amount : int, damage_per_orc : float, warrior_health : float):
        self.warrior_amount = warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health


    def __add__(self, other):
        self.warrior_amount_add = self.warrior_amount + other.warrior_amount
        self.damage_per_orc_mean = (self.damage_per_orc + other.damage_per_orc) // 2
        self.warrior_health_mean = (self.warrior_health + other.warrior_health) // 2
        k = OrcArmy(self.warrior_amount_add, self.damage_per_orc_mean, self.warrior_health_mean)
        return k

    def __sub__(self, other):
        self.warrior_amount_add = self.warrior_amount - other.warrior_amount

        self.damage_per_orc_mean = (self.damage_per_orc - other.damage_per_orc) // 2

        self.warrior_health_mean = (self.warrior_health - other.warrior_health) // 2
        
        if self.warrior_amount < 0 and self.damage_per_orc < 0 and self.warrior_health_mean < 0:
            print("you destroyed the army")
            m = OrcArmy(0, 0, 0)
            return m
        else:
            k = OrcArmy(self.warrior_amount_add, self.damage_per_orc_mean, self.warrior_health_mean)
            return k


    def __str__(self):
        return f'amount of warriors : {self.warrior_amount}\ndamage per orc is : {self.damage_per_orc}\nwarrior health : {self.warrior_health}'
    


if __name__ == '__main__':
    army = OrcArmy(5, 5, 5)
    army2 = OrcArmy(2, 2, 2)
    army3 = army.__add__(army2)
    print(army3)
    army4 = army.__sub__(army2)
    print(army4)
