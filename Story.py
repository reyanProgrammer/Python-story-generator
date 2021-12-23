class Story():

    def __init__(self, name, age, mother, happymother) -> None:
        self.name = name
        self.age = age
        self.mother = mother
        self.happymother = happymother

    def printstory(self):
        print(f"""
This is a chracter whose name is {self.name}
he is {self.age} years old
his mother's name is {self.mother}
and his mother's mood is {self.happymother}
        """)
