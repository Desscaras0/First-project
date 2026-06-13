import random

class Human :
    def __init__(self, name, strength, speed):
        self.name =  name
        self.strength =  strength
        self.speed = speed
       
    def introduction(self): 
      Value = 0
      if self.name == "Karl" : 
        print("KARL IS PROHIBITED")
        return False
      else:
        print(f'{self.name} STATS: Strength "{self.strength}", Speed "{self.speed}".')
        Value = Value + 1
        return Value

#STATS    
Spd1 = random.randint(5,9)
Str1 = random.randint(4,6)
Spd2 = random.randint(5,9)
Str2 = random.randint(4,6)
#User input
Name1 = input("Name of the  1st Character: ")
Name2 = input("Name of the  2st Character: ")
#
person1 = Human(Name1 , Str1 , Spd1)
person2 = Human(Name2 , Str2 , Spd2)

#print
Valueprint1 = person1.introduction()
Valueprint2 = person2.introduction()
print(Valueprint1)
print(Valueprint2)
