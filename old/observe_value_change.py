class Observe_value_change():

   def __init__(self):
      print("init sets _initial=1")
      self._initial = 1

   @property
   def position(self):
      print(f"p.position() is @property and returns self._initial: {self._initial} ")
      return self._initial

   @position.setter
   def position(self, new_value):
      print(f"@position.setter takes new/passed value (({new_value})) and saves as self._initial")
      self._initial = new_value
      print(f"self._initial: {self._initial}")


if __name__ == "__main__":

   print("create new instance of Observe_value_change class")
   p = Observe_value_change()
   print(f"getter for p.position: {p.position}")
   print(f"setter for p.position:")
   p.position = 4