# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. 
# You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.




class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def special_skill(self):
        print(f"{self.name} has a special skill: {self.hunting_skill}")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def display_strength(self):
        print(f"{self.name}'s strength is {self.strength}.")


dog1 = Dog("Buddy", 3, "Golden")
dog1.description()
dog1.get_info()
dog2 = JackRussellTerrier("Max", 2, "White and Brown", "excellent digging")
dog2.description()
dog2.get_info()
dog2.special_skill()
dog3 = Bulldog("Rocky", 4, "Brown", "impressive")
dog3.description()
dog3.get_info()
dog3.display_strength()
"""
expected output
Buddy is 3 years old.
Buddy's coat color is Golden.
Max is 2 years old.
Max's coat color is White and Brown.
Max has a special skill: excellent digging
Rocky is 4 years old.
Rocky's coat color is Brown.
Rocky's strength is impressive.
"""