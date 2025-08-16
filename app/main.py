class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return f"Person({self.__dict__})"


def create_person_list(people: list) -> list:
    people_list = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        person = Person.people[human["name"]]
        for key, value in human.items():
            if key not in ("name", "age") and value is not None:
                setattr(person, key, value)

    for person in people_list:
        if hasattr(person, "wife"):
            for next_person in people_list:
                if next_person.name == person.wife:
                    person.wife = next_person
                    next_person.husband = person

    return people_list
