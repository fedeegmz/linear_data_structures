from array import Array

class Cube():
    def __init__(self, x, y, z, fill_values=None):
        self.data = Array(x)
        for row in range(x):
            self.data[row] = Array(y)
            for col in range(y):
                self.data[row][col] = Array(z, fill_values)