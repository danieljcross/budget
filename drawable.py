import constants
from color import Color
from point import Point

class Drawable:



    def __init__(self, name, value):

        self._name = name
        self._value = value
        self._font_size = 15
        self._color = Color(245,245,245)
        quarter_of_width = int(constants.MAX_X / 4)
        half_of_height = int(constants.MAX_Y / 2)
        self._position = Point(quarter_of_width, half_of_height)
        self._velocity = Point(0,0)
    
    def get_color(self):

        return self._color

    def get_font_size(self):

        return self._font_size

    def get_position(self):

        return self._position

    def get_velocity(self):

        return self._velocity

    def move_next(self):

        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)
        
    def set_color(self,color):

        self._color = color

    def set_position(self, position):
        self._position = position

    def set_font_size(self,font_size):

        self._font_size = font_size

    def set_velocity(self, velocity):

        self._velocity = velocity

    def set_text(self, text):

        self._text = text

    def get_text(self):
        return self._text

    def has_actors(self):
        return False

    def get_actors(self):
        return None
    
firstExpense = Drawable("Fast food spending", 25)

expense_value = firstExpense._value

expense_name = firstExpense._name

expenses = []

expenses.append(firstExpense)

print(expenses[0]._value)
