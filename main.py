class Rectangle:

    # Constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50: # Checking if height or width is greater than 50. If so, message is returned instead of picture
            picture = "Too big for picture."
        else:
            for i in range(self.height):
                picture += self.width * "*" + "\n"
        return picture

    def get_amount_inside(self, smallRect):
        if self.width / smallRect.width >= 1 and self.height / smallRect.height >= 1:
            w = int(self.width / smallRect.width)
            h = int(self.height / smallRect.height)
            return w * h
        else:
            return 0

class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height