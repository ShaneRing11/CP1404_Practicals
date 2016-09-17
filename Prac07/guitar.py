class Guitar:
    def __init__(self, name='', year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        vintage_string = self.is_vintage(self.year)
        return "Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".\
            format(i + 1, self.name, self.year, self.cost, vintage_string)

    def get_age(self, year):
        age = 2016 - year
        return age

    def is_vintage(self, year):
        age = self.get_age(year)
        if age >= 50:
            return "(Vintage)"
        else:
            return ""
