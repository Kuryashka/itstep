class Cars:
    def __init__(self, name, year, manufacturer, engine_capacity, color, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = float(engine_capacity)
        self.color = color
        self.price = int(price)
        self.result = []
    
    def __str__(self):
        return f'name : {self.name}\nyear : {self.year}\nmanufacturer : {self.manufacturer}\nengine_capacity : {self.engine_capacity}\ncolor : {self.color}\nprice : {self.price}'
    
    def return_name(self):
        return self.name
    def return_year(self):
        return self.year
    def return_manufacturer(self):
        return self.manufacturer
    def return_EngineCapacity(self):
        return self.manufacturer
    def return_color(self):
        return self.color
    def return_price(self):
        return self.price

car1 = Cars("year", "name", "manufacturer", 1.45, 'red', 55)
print(car1)
print(car1.return_price())