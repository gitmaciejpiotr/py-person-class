class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    {person["name"]: Person(person["name"], person["age"])
     for person in people}

    return [
        add_spouse(person) for person in people
    ]

def add_spouse(person) -> object:
    person_obj = Person.people[person["name"]]
    if person.get("wife") and person.get("wife") is not None:
        person_obj.wife = Person.people[person["wife"]]
    elif person.get("husband") and person.get("husband") is not None:
        person_obj.husband = Person.people[person["husband"]]
    return person_obj
