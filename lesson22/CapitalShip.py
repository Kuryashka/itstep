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
        hp = 10000 - int(points)
        return hp
    
    
if __name__ == "__main__":
    ship = CapitalShip()
    print(ship.damage(513))
