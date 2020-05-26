from menu import * 
from profile import *


def exit_main_menu():
    global main_menu_running
    main_menu_running = False

main_menu_running = True

main_menu = Menu(
    "Menu Principal - Selecione Uma Opção", [
    ('Criar Perfil', create_profile),
    ('Entrar em um Perfil', select_profile),
    ('Sair', exit_main_menu)])

print(main_menu.display())

while main_menu_running:
    option = int(input('>> '))
    main_menu.callback(option)()
 
