class CapitalShip:
    name = 'Imperial Star Destroyer'
    capacity = {
    'Officers' : 9235,            
    'Enlisted' : 27850,
    'Stormtroopers' : 9700,
    'TIE/ln space superiority starfighters' : 48,
    'TIE/sa bombers' : 12,
    'TIE/IN interceptors' : 12,
    'AT-AT walkers' : 20,
    'AT-ST or AT-DP walkers' : 30,
    'K79-S80 Imperial Troop Transports' : 15,
    'Lambda-class T-4a shuttles' : 8
    }
    max_speed = '7 main engines each speeding up to 975 kilometers per hour'
    length = '1600 meters'
    hp = 10000
    power = 513

    def damage(self, points):
        self.hp = self.hp - int(points)
        cur_hp = self.hp
        if cur_hp < 0:
            print("You destroyed the ship")
            return False
        else:
            print(f"the current amount of hp is : {self.hp}")
            return True
            
    def show_capacity(self):
        for i, j in self.capacity.items():
            print(i, ':', j)
        return
    
    def show_max_speed(self):
        return self.max_speed

    def show_length(self):
        return self.length
    
    
if __name__ == "__main__":
    ship = CapitalShip()
    print(ship.damage(513))
    print(ship.damage(10000))
    ship.show_capacity()
    print(ship.show_max_speed())
    print(ship.show_length())
