class Person(object):

    def __init__(self, name, age, weight):
        self._name = name
        self._weight = weight
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def play(self):
        if self.age >= 16:
            print("You are a child")

        elif 80 <= self.weight <= 110:
            print("You are a health man")

        else:
            print("You have some information but i don't know")


if __name__ == '__main__':
    person = Person("Hamzone", 12, 99)
    person.play()
    person.age = 22
    person.play()



"""
@property 
将类的属性进行保护的时候，注意方法的命名前面要加上“_”
"""