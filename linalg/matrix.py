from linalg.vector import Vector2
import numpy as np
from typing import Iterable, Self

class Matrix2D:
    def __init__(self, vector1: Vector2 = None, vector2: Vector2 = None, data:Iterable=None) -> None: # так в python можно типизовать перменные и функции
        if data is not None:
            self.data = np.array(data)
        else:
            self.data = np.array([[vector1.x, vector2.x], [vector1.y, vector2.y]])

         # тебе надо релизовать через чтение data. Посмотреть что такое Iterable, и как задаются списки в numpy


    def __str__(self) -> str:
        res = ''
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                res += self.data[i][j] + " "
            res += '\n'

        return res

    def __matmul__(self, other) -> Self:
        if isinstance(other, Matrix2D):
            return Matrix2D(data=self.data @ other.data)
        elif isinstance(other, Vector2):
            x = self.data[0][0] * other.x + self.data[0][1] * other.y
            y = self.data[1][0] * other.x + self.data[1][1] * other.y
            return Vector2(x, y)
        else:
            return None

    @classmethod
    def rotate_matrix(cls, alpha: float) -> Self:
        return Matrix2D(data=[[np.cos(alpha), -np.sin(alpha)], [np.sin(alpha), np.cos(alpha)]])

    @classmethod
    def scale_matrix(cls, scale: float) -> Self:
        return Matrix2D(data=[[scale, 0], [0, scale]])











