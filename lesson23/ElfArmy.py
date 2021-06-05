class ElfArmy:
    def __init__(self, warrior_amount, damage_per_elf, elf_health, elf_shield):
        self.warrior_amount = warrior_amount
        self.damage_per_elf = damage_per_elf
        self.elf_health = elf_health
        self.elf_shield = elf_shield
    
    def __add__(self, other):
        self.warrior_amount_add = self.warrior_amount + other.warrior_amount
        self.damage_per_elf_mean = (self.damage_per_elf + other.damage_per_elf) // 2
        self.warrior_health_mean = (self.elf_health + other.elf_health) // 2
        k = ElfArmy(self.warrior_amount_add, self.damage_per_elf_mean, self.warrior_health_mean, self.elf_shield)
        return k
    
    def recieve_damage(self, damage : int):
        dead_warriors = (damage - self.elf_shield) // self.elf_health
        self.warrior_amount = self.warrior_amount - dead_warriors
        if self.warrior_amount < 0:
            print('You destroyed the army')
        return self.warrior_amount

    def __sub__(self, other):
        self.warrior_amount_add = self.warrior_amount - other.warrior_amount

        self.damage_per_orc_mean = (self.damage_per_orc - other.damage_per_orc) // 2

        self.warrior_health_mean = (self.warrior_health - other.warrior_health) // 2
        
        if self.warrior_amount < 0 and self.damage_per_elf < 0 and self.warrior_health_mean < 0:
            print("you destroyed the army")
            m = ElfArmy(0, 0, 0, 0)
            return m
        else:
            k = ElfArmy(self.warrior_amount_add, self.damage_per_orc_mean, self.warrior_health_mean, self.elf_shield)
            return k
    
    def __str__(self):
        return f'amount of warriors : {self.warrior_amount}\ndamage per elf is : {self.damage_per_elf}\nwarrior health : {self.elf_health}\nthis army\'s shield is : {self.elf_shield}'

if __name__ == "__main__":
    army = ElfArmy(5, 5, 5, 6)
    army2 = ElfArmy(10, 10, 10, 12)
    army3 = army.__add__(army2)
    print(army3)
    army3.recieve_damage(10)
    print(army3)
