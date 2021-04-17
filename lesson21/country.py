class Country:
    
    def __init__(self, name, capital, continent, population, cities_names):
        self.name = name
        self.capital = capital
        self.continent = continent
        self.population = population
        self.cities_names = cities_names

    def __str__(self):
        return f'country name : {self.name}\ncapital : {self.capital}\ncontinent : {self.continent}\npopulation : {self.population}\ncities_names : {self.cities_names}'


try:
    name = input("Enter country's name: ")
except ValueError:
        print("Enter valid type")       
try:
    capital = input("Enter capital's name: ")
except ValueError:
    print("Enter valid type")
    
try:
    continent = input("Enter continent's name: ")
except ValueError:
    print("Enter valid type")
    
try:
    population = float(input("Enter population amount: "))
except ValueError:
    print("Enter valid type")
    
try:
    cities_names = input("Enter cities' names: ")
except ValueError:
    print("Enter valid type")
         

if __name__ == '__main__':
    country = Country(name, capital, continent, population, cities_names)
    print(country)

        
