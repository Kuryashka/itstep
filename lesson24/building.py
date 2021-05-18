class Building:
    def __init__(self, levels, height, area, place):
        self.levels = levels
        self.height = height
        self.area = area
        self.place = place
    
    @property
    def levels(self):
        return self._levels

    @levels.setter
    def levels(self, s):
        if not s:
            raise Exception("Set level")
        self._levels = s
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        if  h <= 0:
            raise Exception("Height cannot be zero or below it")
        self._height = h
    
    @property
    def area(self):
        return self._area 

    @area.setter
    def area(self, a):
        if a <= 0:
            raise Exception("Area cannot be zero or below it")
        self._area = a

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, p):
        if not p:
            raise Exception("Place has to be string")
        self._place = p
    
    def __str__(self):
        return f'levels : {self._levels}\nheight : {self._height} cm\narea : {self._area} meters squared\nplace : {self._place}'


if __name__ == '__main__':
    building = Building(4, 255, 5, 'place')
    print(building)
