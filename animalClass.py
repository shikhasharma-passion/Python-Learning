class animal:
   name = "lion"
   name2 = "wolf"
   name3 = "tiger"
   name4 = "crocodile"
   habit = "eat flesh"
   typeOfAnimal = "carnivour"

   def info(self):
    # {a}, {b}, {c}" normal string formatting
    print(f"{self.name}, {self.name2}, {self.name3}, {self.name4} {self.habit} so, they are called {self.typeOfAnimal} animals")
    # "{a, b, c}"  become tuple
    print(f"{self.name, self.name2, self.name3, self.name4 } {self.habit} so, they are called {self.typeOfAnimal} animals")
   

obj1 = animal()
# print(obj1.name)
# print(obj1.habit)
# print(obj1.typeOfAnimal)
obj1.info()