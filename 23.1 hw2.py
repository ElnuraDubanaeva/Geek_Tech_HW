class Figure:
    unit = 'cm'

    def __init__(self):
        self.__perimeter = 0

    def get__perimetr(self):
        return self.__perimeter

    def set__perimetr(self, perimeter):
        self.__perimeter = perimeter

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, __sideLength, __perimeter=0):
        super().__init__()
        self.__sideLength = __sideLength

    def calculate_area(self):
        return (self.__sideLength ** 2)

    def calculate_perimeter(self):
        return (4 * self.__sideLength)

    def info(self):
        return (f'Figure: Square'
                f' Side length: {self.__sideLength}{Figure.unit}'
                f' Perimeter: {self.calculate_perimeter()}{Figure.unit}'
                f' Area: {self.calculate_area()}{Figure.unit}')


class Rectangle(Figure):
    def __init__(self, __length, __width, __perimeter=0):
        super().__init__()
        self.__length = __length
        self.__width = __width

    def calculate_area(self):
        return (self.__width * self.__length)

    def calculate_perimeter(self):
        perimeter = 2 * (self.__width + self.__length)
        self.__perimeter = perimeter
        return self.__perimeter

    def info(self):
        return (f'Figure: Rectangle'
                f' Length: {self.__length}{Figure.unit}'
                f' Width: {self.__width}'
                f' Perimeter: {self.calculate_perimeter()}{Figure.unit}'
                f' Area: {self.calculate_area()}{Figure.unit}')


def figure():
    square1 = Square(5)
    square2 = Square(3)
    rectangle1 = Rectangle(2, 3)
    rectangle2 = Rectangle(3, 4)
    rectangle3 = Rectangle(4, 5)
    figures = [square1, square2, rectangle1, rectangle2, rectangle3]
    for elem in figures:
        print(f'{elem.info()}')


figure()
