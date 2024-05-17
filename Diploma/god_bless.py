import datetime


class Person:

    def __init__(self, first_name, last_name=None, patronymic=None, birth=None, death=None, gender=None):
        self.first_name = first_name
        self.birth = birth
        self.death = death
        self.gender = gender
        self.last_name = last_name
        self.patronymic = patronymic

    def age(self, current_age=None):
        if current_age is None:
            current_age = datetime.date.today()
        if self.death:
            return (self.death - self.birth).days // 365
        else:
            return (current_age - self.birth).days // 365

    def __str__(self):
        info = f"{self.first_name}"
        if self.last_name:
            info += f" {self.last_name}"
        if self.patronymic:
            info += f" {self.patronymic}"
        if self.birth:
            info += f", {self.age()} years old"
        if self.gender:
            info += f", {self.gender}"
        if self.birth:
            info += f". Born on {self.birth.strftime('%d.%m.%Y')}"
        if self.death:
            info += f". Died on {self.death.strftime('%d.%m.%Y')}"
        return info


class Savedata:
    def __init__(self):
        self.person = []

    def add_people(self, human):
        self.person.append(human)

    def search(self, word):
        search = []
        for human in self.person:
            if word.lower() in str(human).lower():
                search.append(human)
        return search

    def save(self, filename):
        with open(filename, 'w') as file:
            for person in self.person:
                file.write(str(person) + '\n')

    def load(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.person.append(self.parse(line))

    @staticmethod
    def parse(line):
        data = line.strip().split(', ')
        first_name = data[0]
        last_name = patronymic = birth = death = gender = None
        for item in data[1:]:
            if 'years old' in item:
                birth = datetime.datetime.strptime(item.split('. ')[1], '%d.%m.%Y').date()
            elif 'Born on' in item:
                birth = datetime.datetime.strptime(item.split(': ')[1], '%d.%m.%Y').date()
            elif 'Died on' in item:
                death = datetime.datetime.strptime(item.split(': ')[1], '%d.%m.%Y').date()
            else:
                gender = item
        return Person(first_name, last_name, patronymic, birth, death, gender)


def main():
    look = Savedata()
    try:
        look.load('people.txt')
    except FileNotFoundError:
        pass

    while True:
        print("\n Main Menu")
        print("1. Add new person")
        print("2. Search for a person")
        print("3. Save data to file")
        print("4. Load data from file")
        print("5. Exit")

        choice = input("What do you want?: ")

        if choice == "1":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name (if it's possible): ")
            patronymic = input("Enter Patronymic (if it's possible): ")
            fake_birth = input("Enter a date of birth (dd.mm.YYYY): ")
            birth = datetime.datetime.strptime(fake_birth, "%d.%m.%Y").date()
            fake_death = input("Enter a date of death (dd.mm.YYYY): ")
            death = datetime.datetime.strptime(fake_death, "%d.%m.%Y").date()
            gender = input("Enter a gender: ")
            human = Person(first_name, last_name, patronymic, birth, death, gender)
            look.add_people(human)

        elif choice == "2":
            word = input("Enter the name for search: ")
            search = look.search(word)
            if search:
                print("Here what I have found")
                for res in search:
                    print(res)
            else:
                print("Nothing has found")
        elif choice == "3":
            look.save("people_base.txt")
            print("Complete")
        elif choice == "4":
            try:
                file = input("Enter name of file: ")
                look.load(file)
                print("Load is successful")
            except FileNotFoundError:
                print("There is no file with this name, try again")
        elif choice == "5":
            break
        else:
            print("Incorrect input, try again")


if __name__ == "__main__":
    main()
