class Actions:
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

