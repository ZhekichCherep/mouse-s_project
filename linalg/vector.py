import math


class Vector2:
    def __init__(self, x, y): # этот метод перегружает инициализацию вектора, то есть вызвается при строке
                        # v = Vector(2)
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def __rmul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def __truediv__(self, other):
        if other!=0:
            return Vector2(self.x / other, self.y / other)
        else:
            print("Вы не знаете законов математики")
    def normalize(self):
        l=(self.x **2 + self.y**2)**0.5
        return Vector2(self.x / l, self.y / l)

    def get_coordinates(self):
        return self.x, self.y

    def __str__(self):
        return f"[{self.x},{self.y}]"




'''
И добавить способ на экране менять скорость (как добавить поле для ввода на экран можно у нейронки спрашивать)'''

