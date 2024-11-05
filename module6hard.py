import math

class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.color = [r, g, b]
        else:
            print("Некорректный цвет!")

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_sides(self):
        return self.radius

    def set_sides(self, radius):
        if radius > 0:
            self.radius = radius
        else:
            print("Радиус должен быть положительным!")

    def len(self):
        return int(2 * math.pi * self.radius)

class Cube(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.__sides = [side] * 12

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if len(sides) == 12 and all(side > 0 for side in sides):
            self.__sides = list(sides)
        else:
            print("Некорректное количество или значения сторон!")

    def get_volume(self):
        return self.__sides[0] * self.__sides[1] * self.__sides[2]  # Исправлено: вычисляем объем

# Создание объектов
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# Проверка периметра (круга)
print(circle1.len())

# Проверка объема (куба)
print(cube1.get_volume())
