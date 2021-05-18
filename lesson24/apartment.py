class Apartment:
    def __init__(self, apartment_number, amount_of_residents, floor, area):
        self.apartment_number = apartment_number
        self.amount_of_residents = amount_of_residents
        self.floor = floor
        self.area = area

    @property
    def apartment_number(self):
        return self._apartment_number
    
    @apartment_number.setter
    def apartment_number(self, number):
        if number <= 0:
            raise Exception('apartment number cannot be zero or below')
        self._apartment_number = number
    
    @property
    def amount_of_residents(self):
        return self._amount_of_residents

    @amount_of_residents.setter
    def amount_of_residents(self, amount):
        if amount <= 0:
            raise Exception('amount of residents cannot be zero or below')
        self._amount_of_residents = amount
    
    @property
    def floor(self):
        return self._floor
    
    @floor.setter
    def floor(self, f):
        if f <= -1:
            raise Exception('floor cannot be below zero')
        self._floor = f

    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, a):
        if a <= 0:
            raise Exception('area cannot be zero or below')
        self._area = a
    
    def __str__(self):
        return f'apartment number : {self._apartment_number}\namount of residents : {self._amount_of_residents}\nfloor : {self._floor}\narea : {self._area} meters squared'

if __name__ == '__main__':
    apartment = Apartment(256, 4, 19, 180)
    print(apartment)
