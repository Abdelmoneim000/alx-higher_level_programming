#!/usr/bin/python3
"""
A package for a square object
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class that inherits from
    the Rectangle class to update the
    id and attributes
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the square to inherit from
        the super class Rectangle.
        """
        super().__init__(size, x, y, id)

    @property
    def size(self):
        """
        get the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        set the size attribute to
        the assigned value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the attributes of the square
        according to the number of parameters
        given.

        if args exists, ignore kwargs.
        """
        if args:
            attributes = ["id", "_Rectangle__width",
                          "_Rectangle__height", "_Rectangle__x", "_Rectangle__y"]
            for i in range(min(len(args), len(attributes))):
                setattr(self, attributes[i], args[i])
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """return the represented string format of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
