# class define
class animal:

   # constractor (parameterized)
   def __init__(self, imgOfAnimal, habit, animalType):
     self.imgOfAnimal = imgOfAnimal
     self.habit = habit
     self.animalType = animalType
   
   def info(self):
    print(f"Hye I am {self.imgOfAnimal}. I {self.habit} so, i called as {self.animalType}")
print("---------WELCOME TO KNOW US--------")

# object define lon, elephant, wolf, tiger, goat, cat they are obj of class "animal" 
lion = animal("🦁", "eat flesh", "carnivours")
elephant = animal("🐘", "eat plants", "herbivours")
wolf = animal("🐺", "eat flesh", "carnivours")
tiger = animal("🐯", "eat fleshh", "carnivours")
goat = animal("🐐", "eat grass", "herbivours")
cat = animal("🙀", "eat both", "omnivours")

# method call
lion.info()
elephant.info()
wolf.info()
cat.info()
tiger.info()
goat.info()





 
