class Rectangle:
  width = 0
  height = 0
  
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self): 
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self): 
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self): 
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    line = "*" * self.width
    pic = [line for _ in range(self.height)]
    return "\n".join(pic)+"\n"
    
  def get_amount_inside(self,rectangle): 
    return (self.width//rectangle.width) * (self.height//rectangle.height)

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    
class Square(Rectangle):
  
  def set_side(self,side):
    self.width = side
    self.height = side

  def __init__(self,side):
    self.set_side(side)

  def set_width(self,width):
    self.set_side(width)

  def set_height(self,height):
    self.set_side(height)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
