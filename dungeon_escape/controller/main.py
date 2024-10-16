import random

def main():
    print("Empieza la partida")
    create_player()

    def create_player():
        
        print("1 - Humano, 2 - Enano, 3 - Elfo")
        option = input("Con que especie quieres jugar? ")
        match option:
            case 1:
                player = Character(1)    
            case 2:
                player = Character(2)        
            case 3:
                player = Character(3)  

        name = input("Dale nombre a tu personaje")

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


