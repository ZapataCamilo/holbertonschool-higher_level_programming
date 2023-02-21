from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    @property
    def public_set(self):
        return (self.__width, self.__height, self.__x, self.__y)
    @public_set.setter
    def public_set(self):
        return (self.width, self.height, self.x, self.y)
