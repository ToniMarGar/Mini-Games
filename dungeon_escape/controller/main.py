import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from dungeon_escape.model.Char import Character
new_player = ""

def create_player():
    name = input("\n Dale nombre a tu personaje: ")
    new_player = ""
    while new_player == "":
        print("\033[1m""1 - Humano, 2 - Enano, 3 - Elfo""\033[0m")
        option = input("\n Con que especie quieres jugar? ")
        if option == "1":
            new_player = Character(name,int(option)) 
        elif option == "2":
            new_player = Character(name,int(option)) 
        elif option == "3":
            new_player = Character(name,int(option)) 
        else:
            print("Eso no es un personaje disponible..")
        
    print(f"Nombre: {new_player.name} Hp: {new_player.hp} Specie: {new_player.specie}")
    return new_player

def start_game(player):
    print("\n La partida está empezando.. ")
    print("En una de tus exploraciones, entras en una mazmorra. ")
    print("Ves que hay diferentes caminos. ")
    while player.speed != 0 and player.hp >= 0:    
        
            player.action()
            print(f"Vida: {player.hp}")
            #print(f"{player.speed}")
            print(f"Inventario: {player.inventory}")
            print("--------------------------------------------------")

    if player.hp <= 0:
        print("\033[1m""Has perdido""\033[0m")
    else:
        print("\033[1m""Has conseguido salir de la mazmorra! ""\033[0m")

def main():
    print("Empieza la partida")
    player = create_player()
    start_game(player)

main()