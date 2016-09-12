class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".\
            format(self.name, self.year, self.cost)

    def get_age(self, year):
        age = 2016 - year
        return age

    def is_vintage(self, year):
        age = self.get_age(year)
        print(age)
        if age >= 50:
            return True
        else:
            return False
