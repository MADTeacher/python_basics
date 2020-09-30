class Persone:
    def __init__(self, name="Ivan"):
        self.name = name

    def __call__(self, profession):
        print(f"{self.name} is a {profession}")

class ProfessionName:
    def __init__(self, persone, prof="unemployed"):
        self.persone = persone
        self.profession = prof

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if key == "profession":
            self.persone(self.__dict__[key])

if __name__ == "__main__":
    persone = Persone("Alex")
    prof = ProfessionName(persone)
    prof.profession = "doctor"
    prof.profession = "student"