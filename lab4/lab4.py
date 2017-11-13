#class Animal(object):
#        def __init__(self,sound,name,age,favorite_color):                self.sound=sound
#                self.name=name
#                self.age=age
#                self.favorite_color=favorite_color
#        def eat(self,food):
#                print("yummy!"+self.name+" is eating"+food)
#        def description(self):
#                print(self.name+"is"+self.age+"years old and loves the color"+self.favorite_color)
#        def make_sound(self):
#                print(self.sound*3)
#elephant=Animal("tuuu","billy","20","blue")
#elephant.make_sound()
#elephant=Animal("tuuu","billy","20","blue")
#elephant.eat(" bananas")
#elephant.description()
       
class Person(object):
        def __init__(self,name,age,city,gender,favorite_food):
                self.name=name
                self.age=age
                self.city=city
                self.gender=gender
                self.favorite_food=favorite_food
        def eat(self):
                print("noa is eating her favorite food which is "+self.favorite_food)

noa=Person("noa","15","tivon","female","pizza")

noa.eat()

