class PrivateExc(Exception): pass

class PrivatAttribute:
    def __setattr__(self, key, value):
        print(f"check key = {key}, value = {value}")
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value

class FirstTestAttribute(PrivatAttribute):
    privates = ["name", "city"]

class SecondTestAttribute(PrivatAttribute):
    privates = ["age"]

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    first_test = FirstTestAttribute()
    second_test = SecondTestAttribute("Alex")
    second_test.city = "SPb"
    first_test.country = "Germany"
    #first_test.name = "Jon"
    second_test.age = 20