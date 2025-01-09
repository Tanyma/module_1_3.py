import math

# Базовый класс Figure

class Figure:

    sides_count = 0 # Количество сторон (устанавливается в дочернем классе)

    def __init__(self, color, *sides):
        self.__color = None
        self.filled = False
        self.set_color(*color)
        self.set_sides(*sides)


# Метод для получения цвета

    def get_color(self):
        return self.__color


# Проверка корректности цвета

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
        0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255


# Установка цвета

    def set_color(self, r, g, b):

        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

        else:
            print(f"Invalid color: ({r}, {g}, {b}). Color remains the same.")

# Проверка корректности сторон

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)


# Установка сторон

    def set_sides(self, *new_sides):

        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print(f"Invalid sides. Sides remain the same.")


# Получение сторон

    def get_sides(self):
        return self.__sides


# Периметр (длина для фигур с замкнутыми сторонами)

    def __len__(self):
        return sum(self.__sides)


# Класс Circle (круг)

class Circle(Figure):

    sides_count = 1


    def __init__(self, color, *sides):

        super().__init__(color, *sides)
        self.__radius = self.__sides[0] / (2 * math.pi) # Радиус из длины окружности


    def get_square(self):

    # Площадь круга: π * r^2

        return math.pi * (self.__radius ** 2)


# Класс Triangle (треугольник)

class Triangle(Figure):

    sides_count = 3


    def __init__(self, color, *sides):
        super().__init__(color, *sides)


    def get_square(self):

        a, b, c = self.__sides

        p = (a + b + c) / 2

        return math.sqrt(p * (p - a) * (p - b) * (p - c))


# Класс Cube (куб)

class Cube(Figure):

    sides_count = 12


    def __init__(self, color, *sides):

        super().__init__(color, *sides)

        if len(self.__sides) == 1:

            self.__sides = [self.__sides[0]] * 12 # Если передано 1 значение, делаем 12 одинаковых сторон


    def get_volume(self):

# Объем куба: a^3

        return self.__sides[0] ** 3

