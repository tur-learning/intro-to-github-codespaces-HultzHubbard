from classes import person

person1 = person("Hultz", 18, 6)
person1.info()

person2 = person("Elsie", 16, 4)
person2.info()

person3 = person("Caroline", 14, 5)
person3.info()

print("\n\n")

person1.info()
person1.change_age(19)
person1.info()