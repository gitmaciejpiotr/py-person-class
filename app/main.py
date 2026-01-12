class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    people_obj_list = []

    {person["name"]: Person(person["name"], person["age"]) for person in people}

    for person in people:
        person_obj = Person.people[person["name"]]

        if person.get("wife") and person.get("wife") is not None:
            person_obj.wife = Person.people[person["wife"]]
        elif person.get("husband") and person.get("husband") is not None:
            person_obj.husband = Person.people[person["husband"]]
        people_obj_list.append(person_obj)

    return people_obj_list

people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

print(create_person_list(people))
