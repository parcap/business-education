class Dog:
    species = "mammal"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def decription(self):
        return "{} is {} and is a {}".format(self.name, self.age, self.species)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
    def birthday(self):
        self.age += 1

class Person:
    description = "general person"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("My name is {} and I am {} years old".format(self.name, self.age))
        
    def eat(self, food):
        print("{} eats {}".format(self.name, food))
              
    def action(self):
        print("{} jumps.".format(self.name))
        
class Baby(Person):
    description = "baby"
    
    def speak(self):
        print("ba ba ba ba ba ba")
        
    def nap(self):
        print("{} taks a nap".format(self.name))

person = Person("Steve", 20)

person.speak()
person.eat("pasta")
person.action()

baby = Baby("Ian", 1)
baby.speak()
baby.eat("baby food")
baby.action()

print(person.description)
print(baby.description)

print(isinstance(person, Person))
print(isinstance(person, Baby))
print(isinstance(baby, Person))
print(isinstance(baby, Baby))
print(isinstance(person, object))
print(isinstance(baby, object))
    

'''
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 8)

print(mikey.decription())
print(philo.decription())

philo.age = 10
mikey.species = "reptile"

print(mikey.decription())
print(philo.decription())

print(philo.speak("Gruff gruff!"))
print(mikey.speak("Bow wow!"))

mikey.birthday()

print(mikey.decription())
'''