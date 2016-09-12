class ProgrammingLanguage:
    def __init__(self, name='', dynamic='', reflection=False, year=0):
        self.name = name
        self.dynamic = dynamic
        self.reflection = reflection
        self.year = year

    def is_dynamic(self, dynamic):
        if dynamic == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".\
            format(self.name, self.dynamic, self.reflection, self.year)