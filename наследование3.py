import random


class Animal:

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0] # координаты X, Y, Z
    speed = 1 # начальная скорость



    def __init__(self, speed):
        self.speed = speed



    def move(self, dx, dy, dz):

    # Изменяем координаты с учетом скорости

        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed

    # Если попытка изменить координату Z на отрицательное значение

        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")

        else:
            self._cords[2] += dz * self.speed


    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")



    def attack(self):

        if self._DEGREE_OF_DANGER < 5:

            print("Sorry, i'm peaceful :)")

        else:

            print("Be careful, i'm attacking you 0_0")



    def speak(self):

        print(self.sound)


# Класс для птиц, наследуется от Animal

class Bird(Animal):

    beak = True



def lay_eggs(self):
    eggs = random.randint(1, 4)
    print(f"Here are(is) {eggs} eggs for you")


# Класс для плавающих животных, наследуется от Animal

class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3


    def dive_in(self, dz):
        dz = abs(dz) # Чтобы всегда делать отрицательное изменение
        self.speed /= 2 # Скорость при нырянии уменьшается в 2 раза
        self.move(0, 0, -dz) # Ныряем, изменяя только координату Z


# Класс для ядовитых животных, наследуется от Animal

class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8



# Класс для утконоса, наследует от Bird, AquaticAnimal, PoisonousAnimal

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    sound = "Click-click-click" # Уникальный звук утконоса



    def __init__(self, speed):

        super().__init__(speed) # Инициализация через родительский класс Bird

 