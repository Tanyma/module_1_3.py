class House():
    def __init__(self,name ,number_of_floors):
        self.name  = name
        self.number_of_floors = int(number_of_floors )
    def display_info(self):
        print("Добро пожаловать в отель " + self.name + "\nВ нем "  + self.number_of_floors + " этажей")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return "Название: " + self.name +  " кол-во этажей " + str(self.number_of_floors)
h1 = House("Ameli", "10")
h2 = House("Antares", "15")
print(len(h1))
print(str(h2))