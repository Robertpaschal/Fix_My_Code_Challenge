#!/usr/bin/python3
"""
A square challange
"""


class Square():
    """
    defines the width and height of a sqaure
    """
    def __init__(self, width=0, height=0):
        """
        Sets the inital values of how the square is defined
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """
        Perimiter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String return format"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
