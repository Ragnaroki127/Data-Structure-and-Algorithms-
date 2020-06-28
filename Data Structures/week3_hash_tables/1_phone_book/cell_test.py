#%%
class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s: Age under 16' % self._name)
        else:
            print('%s: Age above 16' % self._name)

# %%
person = Person('Jack', 12)
person.play()
person.age = 22
person.play()