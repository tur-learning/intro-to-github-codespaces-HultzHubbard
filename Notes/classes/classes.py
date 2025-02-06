# Empty Class:
class myObject:
    # minimal class
    # without attributes
    pass

# Components of class (working function)
class person:
    #Class attribute
    # shared by all instances
    species = "Homo Sapiens"

    def __init__(self, name, age, height):
        # Instance attributes
        # specific to each instance
        self.name = name
        self.age = age
        self.height = height
    
    def info(self):
        #method (function) to print
        # infor related to our object
        print(f"{self.name} is {self.age} years old and {self.height} feet tall")

    def change_age(self, new_age):
        self.age = new_age

