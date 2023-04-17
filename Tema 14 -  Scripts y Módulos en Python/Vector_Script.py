import math
 
class Vector2D():

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @property
  def module(self):
    return math.sqrt(self.x**2 + self.y**2)

  def scalar_prod(self, n = 1):
    self.n = n
    self.x = n * self.x
    self.y = n * self.y

  def __str__(self): 
    return (f"({self.x},{self.y})") 

  @classmethod
  def sum(cls, i , j):
    return cls(i.x + j.x, i.y + j.y)

  @classmethod
  def substract(cls, i , j):
    return cls(i.x - j.x, i.y - j.y)

  @staticmethod
  def dot_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

  @classmethod
  def distance(cls, u , v): 
    return cls.substract(u, v).module    

  def extend_to_3D(self, z = 0):
    return Vector3D(self.x , self.y, z)


class Vector3D(Vector2D):

    def __init__(self, x, y, z):
      super().__init__(x, y)
      self.z = z

    def __str__(self):
      return (f"({self.x},{self.y},{self.z})") 
     
    @property
    def module(self):
      return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def scalar_prod(self, n = 1):
      super().scalar_prod(n)
      self.z = n * self.z
    
    @classmethod
    def sum(cls, i , j):
      return cls(i.x + j.x, i.y + j.y, i.z + j.z)

    @classmethod
    def substract(cls, i , j):
      return cls(i.x - j.x, i.y - j.y, i.z - j.z)

    @staticmethod
    def dot_product(v1, v2):
      return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @classmethod
    def distance(cls, u , v): 
      return cls.substract(u, v).module  
    
    @classmethod
    def zero(cls):
      return cls(0,0,0)

    @classmethod
    def horizontal(cls):
      return cls(1,0,0)

    @classmethod
    def vertical(cls):
      return cls(0,1,0)
    
    @classmethod
    def forward(cls):
      return cls(0,0,1)
    