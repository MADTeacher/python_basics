class Persone:
    def __init__(self, name="Alex", age=22):
        self.__persone_name = name
        self.__persone_age = age

    @property
    def name(self):
        print("get name", end=' ')
        return self.__persone_name

    @property
    def age(self):
        print("get age", end=' ')
        return self.__persone_age

    @name.setter
    def name(self, new_name):
        print(f"set new name - {new_name}")
        self.__persone_name = new_name

    # @age.setter
    # def age(self, new_age):
    #     print(f"set new age - {new_age}")
    #     self.__persone_age = new_age

if __name__ == "__main__":
    my_persone = Persone()
    print(my_persone.name)
    print(my_persone.age)
    my_persone.name = "Maxim"
    my_persone.age = 10
    my_persone.name = 20