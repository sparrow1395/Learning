import datetime
from Person import Actions


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


def main():
    look = Actions()
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
            birth = correct_date(fake_birth)
            fake_death = input("Enter a date of death (dd.mm.YYYY): ")
            death = correct_date(fake_death)
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


def correct_date(date_str):
    for separator in [".", "-", "/", " "]:
        part = date_str.split(separator)
        if len(part) == 3:
            day, month, year = map(int, part)
            return datetime.date(year, month, day)


if __name__ == "__main__":
    main()
