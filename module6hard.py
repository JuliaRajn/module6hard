import math

class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [r, g, b]
        else:
            print("Некорректный цвет!")

    def _is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

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

    def __len__(self):
        return int(2 * math.pi * self.radius)

class Cube(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.__sides = [side] * 12

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self._is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            print("Некорректное количество или значения сторон!")

    def get_volume(self):
        return self.__sides[0] ** 3

    def _is_valid_sides(self, *sides):
        return len(sides) == 12 and all(side > 0 for side in sides)

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
print(circle1.__len__()) # Используем метод __len__ для получения периметра

# Проверка объема (куба)
print(cube1.get_volume())
