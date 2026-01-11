class returnn:
    name = "monika"
    age =22
    profession = "whatever"
    def info(self):
      print(f"{self.name} is a {self.profession}")

a = returnn()
a.name = "gita"
a.profession = "pop star"
a.info()

m = returnn()
m.name ="sina"
m.profession ="dancer"
m.info()

