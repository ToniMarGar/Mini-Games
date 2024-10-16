import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from dungeon_escape.model.Char import Character

def main():
    print("Empieza la partida")
    create_player()

def create_player():
    new_player = ""    
    name = input("Dale nombre a tu personaje: ")
    print("1 - Humano, 2 - Enano, 3 - Elfo")
    while new_player == "":
        option = input("Con que especie quieres jugar? ")
        if option == "1":
            new_player = Character(name,int(option)) 
        elif option == "2":
            new_player = Character(name,int(option)) 
        elif option == "3":
            new_player = Character(name,int(option)) 
        else:
            print("This is not a character, please choose one from the list.")
 
         
    print(f"Name: {new_player.name} Stats: {new_player.hp} Specie: {new_player.specie}")
    # crear personaje alomejor si da tiempo y si nos apetece y si se alinean los astros.
    # empieza partida
    # inventario a 0, vida a 100
    # empieza partida en base dando las opciones: avanzar, derecha, izquierda
    # random entre: avanzar, trampa
        # si avanzar, 80 - avanzar, 20 - objeto
            # si objeto, 80 - poción, 20 - espada
                # poción + 50 hp, espada = salvar monstruo
        # si trampa, 60 - trampa, 40 - monstruo
            # si trampa, 60 - daño, 40 - esquivar
                # trampa - 20 hp,
            # si monstruo, daño a no ser que espada

main()