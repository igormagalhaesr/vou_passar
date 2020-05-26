from data import ufrj_majors

class Profile:
    def __init__(self, username, name):
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
    
import pickle

def not_yet():
    print("opa, ainda não está pronto")

def get_grades():
    ling = float(input("Nota Linguagens: "))
    hum = float(input("Nota Humanas: "))
    cn = float(input("Nota Ciências da Natureza: "))
    mat = float(input("Nota Matemática: "))
    red = float(input("Nota Redação: "))

    out = {
        "linguagens": ling,
        "humanas" : hum,
        "natureza" : cn,
        "matematica" : mat,
        "redacao" : red
        }
    
    return out

def create_profile():
    name = input("Entre seu nome: ")
    username = input("Entre um nome de usuário: ")
    grades = get_grades()

    user = Profile(username, name)
    user.set_grades(grades)

    file_user = open(username + ".txt", "xb")
    pickle.dump(user, file_user)

def select_profile():
    username = input("Entre o seu nome de usuário: ")
    obj = pickle.load(open(username + ".txt", "rb"))
    grades_list = obj.grades.items()

    print("Olá", obj.name)
    print()

    for grade_tuple in grades_list:
        print("Sua nota em", end=" ")
        print(grade_tuple[0], end = " ")
        print("é", grade_tuple[1])
    
    print()

    for major in ufrj_majors:
        user_average = obj.weighted_average(major)
        print("Sua média em", major["curso"], "é", user_average)
        print("A nota de corte é ", major["corte"])

        if user_average >= major["corte"]:
            print("Você passou!")
        else:
            print("Você não passou.")
        print()
        









