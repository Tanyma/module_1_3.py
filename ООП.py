import time

class House():
    def __init__(self,name ,number_of_floors):
        self.name  = name 
        self.number_of_floors = int(number_of_floors )
    def display_info(self):
        print("Добро пожаловать в отель " + self.name + "\nВ нем "  + self.number_of_floors + " этажей")
    def go_to(self,new_floor):
        self.new_floor  = int(new_floor) 
        if self.new_floor <= self.number_of_floors and self.new_floor >= 1 :
            for i in range(self.new_floor):
                print(i+1)
                time.sleep(1) 
            print(f'Вы на {self.new_floor} этаже') 
        else :
            print('Такого этажа нет')


house1 = House("DOOSAN", "10")  
# house1.display_info() 
house1.go_to(0)