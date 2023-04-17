class Tree():

  

  def __init__(self, name, height, diameter, talkative = False):
    self.name = name
    self.height = height
    self.diameter = diameter
    self.talkative = talkative
  
  def talk(self, message):
    self.message = message
    if self.talkative == True:
      return self.message
    elif self.talkative == False:
      return "El albol no es partante"

  def grow(self, add_height = 0, add_diameter = 0):
    self.height += add_height
    self.diameter += add_diameter 


  def __str__(self): 
    if self.talkative == True:
      return f"{self.name} es un árbol parlante que mide {self.height} cm de altura y {self.diameter} cm de diametro"
    elif self.talkative == False:
      return f"{self.name} es un árbol no parlante que mide {self.height} cm de altura y {self.diameter} cm de diametro"

trees = []

def born_tree(tree_object):
  trees.append(tree_object)
  print(f"{tree_object.name} acaba de nacer")
  print(tree_object)

def dead_tree(tree_object):
  if tree_object in trees:
    trees.remove(tree_object)
    print(f"{tree_object.name}, descansa en paz")
  else:
    print("El arbol no esta en la lista")