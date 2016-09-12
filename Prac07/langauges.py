from Prac07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    programming_languages = [ruby, python, vb]
    for item in programming_languages:
        if item.is_dynamic(item.dynamic):
            print(item.name)


main()
