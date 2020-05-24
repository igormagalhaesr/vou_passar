#profile

class Profile:
    

    def __init__(self, username, name, grades):
        self.username = username
        self.name = name
        self.grades = {
            "linguagens" : 0,
            "humanas" : 0,
            "natureza" : 0,
            "matematica" : 0,
            "redacao" : 0
            }

    def get_grades(self):
        return self.grades

    def set_grades(self, grades):
        self.grades = grades

    def weighted_average(self, major):
        grades = self.grades
        
        numerator = grades["linguagens"] * major["linguagens"] + grades["humanas"] * major["humanas"] + \
        grades["natureza"] * major["natureza"] + grades["matematica"] * major["matematica"] + \
        grades["redacao"] * major["redacao"]

        denominator = major["linguagens"] + major["humanas"] + major["natureza"] + major["matematica"] + \
        major["redacao"]

        out = numerator / denominator

        return out

#data

matematica_aplicada = {
        "curso" : "Matemática Aplicada",
        "corte" : "720.96",
        "linguagens" : 3,
        "humanas" : 1,
        "natureza" : 4,
        "matematica" : 5,
        "redacao" : 1
        }

estatistica = {
        "cursoi" : "Estatística",
        "corte" : 742.91,
        "linguagens" : 2,
        "humanas" : 1,
        "natureza" : 3,
        "matematica" : 5,
        "redacao" : 3
        }

ufrj_majors = [matematica_aplicada, estatistica]

#menu
from collections import namedtuple
Option = namedtuple('Option', ['label', 'callback'])

class Menu:

    SEPARATOR = '-'

    _title = ''
    _options = []

    def __init__(self, title, options):
        self._title = title

        for option in options:
            self._options.append(Option(option[0], option[1]))

    def header(self, text):
        line = self.SEPARATOR * (len(text) + 2)
        return f"{line}\n {text}\n{line}\n"

    def display(self):
        string = self.header(self._title)

        for i, option in enumerate(self._options):
            string += f"{i + 1} {option.label}\n"

        return string

    def callback(self, i):
        if i <= len(self._options):
            return self._options[i - 1].callback

def not_yet():
    print("opa, ainda não está pronto")

def exit_main():
    global main_menu_running
    main_menu_running = False

main_menu_running = True

main_menu = Menu(
    "Menu Principal - Selecione Uma Opção", [
    ('Criar Perfil', not_yet),
    ('Entrar em um Perfil', not_yet),
    ('Sair', exit_main)])

print(main_menu.display())

while main_menu_running:
    option = int(input('>> '))
    main_menu.callback(option)()
        













