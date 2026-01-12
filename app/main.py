class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    people_obj_list = []

    {person["name"]: Person(person["name"], person["age"])
     for person in people}

    for person in people:
        person_objt = Person.people[person["name"]]

        if person.get("wife") and person.get("wife") is not None:
            person_objt.wife = Person.people[person["wife"]]
        elif person.get("husband") and person.get("husband") is not None:
            person_objt.husband = Person.people[person["husband"]]
        people_obj_list.append(person_objt)

    return people_obj_list
