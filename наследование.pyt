
class Animal:

  def __init__(self, name):
    self.alive = True # Живое животное
    self.fed = False  # Не накормлено
    self.name = name  # Имя животного

class Plant:

  def __init__(self, name):
    self.edible = False # По умолчанию растение несъедобное
    self.name = name   # Имя растения

class Mammal(Animal):

  def eat(self, food):
    if food.edible:
      print(f"{self.name} съел {food.name}")
      self.fed = True
    else:
      print(f"{self.name} не стал есть {food.name}")
      self.alive = False


class Predator(Animal):
  
  def eat(self, food):
    if food.edible:
      print(f"{self.name} съел {food.name}")
      self.fed = True

    else:
      print(f"{self.name} не стал есть {food.name}")
      self.alive = False


class Flower(Plant):
  def __init__(self, name):
    super().__init__(name) # Вызов конструктора базового класса
    self.edible = False   # Цветы несъедобные


class Fruit(Plant):

  def __init__(self, name):
    super().__init__(name) # Вызов конструктора базового класса
    self.edible = True   # Фрукты съедобные


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим имена

print(a1.name)
print(p1.name)

# Проверка начальных состояний

print(a1.alive) # True
print(a2.fed)  # False

a1.eat(p1) # Хищник не стал есть несъедобный цветок
a2.eat(p2) # Млекопитающее съело съедобный фрукт

print(a1.alive) # False (погиб)
print(a2.fed)  # True (насытился)

 