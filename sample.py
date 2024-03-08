class student:
    def __init__(self, name, age,address) -> None:
        self.name = name 
        self.age = age
        self.address = address

    def info(self):
        print(f"I am {self.name} and I am {self.age} years old and I live in {self.address}")


human = student('xyz', 55, 'yss')
human.info()