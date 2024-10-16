import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import random

class Character:
    def __init__(self,name,specie):

        self.name = name
        self.specie = specie
        self.inventory=[]
        self.hp = 0
        self.speed = 0
        self.create_char()
        
    def create_char(self):
        match self.specie:
            case 1:
                self.human_char()
            case 2:
                self.dwarf_char()
            case 3:
                self.elf_char()

        print("Character created")
        
    def human_char(self):
        self.hp = 100
        self.specie = "Humano"
        self.speed = 10
    
    def dwarf_char(self):
        self.hp = 120
        self.specie = "Enano"
        self.speed = 12
    
    def elf_char(self):
        self.hp = 80
        self.specie = "Elfo"
        self.speed = 8
    
    def trap(self):
    
        prob = random.random()

        if prob < 0.4:
            print("\033[1m""Has caido en una trampa!""\033[0m")
            self.hp -= 30
        else:
            print("\033[1m""Un monstruo te ha encontrado!""\033[0m")
            print("w - atacar, d - huir")
            choice = input("Que quieres hacer? ")
            if choice == "w":
                attack = random.random()
                if attack < 0.3:
                    print("Has derrotado al monstruo")
                elif 0.3 <= attack and attack < 0.7:
                    print("Combates con el monstruo")
                    self.hp -= 20
                else:
                    print("El monstruo te derrota claramente")
                    self.hp -= 50
            if choice == "d":
                flee = random.random()
                if flee < 0.4:
                    print("Has escapado del monstruo")
                elif 0.4 <= flee and flee < 0.9:
                    print("Intentas escapar pero tropiezas") 
                    self.hp -= 20
                else:
                    print("No hay salida y el monstruo te ataca por la espalda")
                    self.hp -= 50

    def advance(self):

        prob = random.random()

        if prob < 0.8:
            print("\033[1m""Avanzas a la siguiente sala.""\033[0m")
        else:
            obj = random.random()
            if obj < 0.7:
                self.inventory.append("Potion")
                print("\b Has encontrado una poción!")
            else:
                self.inventory.append("Sword")
                print("\b Has encontrado una espada!")
    
    def action(self):
        print("\033[1m""\n d - derecha, w- recto, a - izquierda, p - poción""\033[0m")
        direction = input("Hacia donde quieres ir? ")
        while direction != "":
            if direction == "p":
                if "Potion" in self.inventory:
                    self.hp += 50
                    self.inventory.remove("Potion")
                    print("\b Te has curado")
                    direction = ""
                else:
                    print("No tienes pociones. ")
                    direction = input("\033[1m""Hacia donde quieres ir? ""\033[0m")
            elif direction == "w" or direction == "a" or direction == "d" and direction != "p":
                prob = random.random()
                if prob < 0.7:
                    self.advance()
                else:
                    self.trap()
        
                self.speed -= 1
                direction = ""
            else:
                print("Te has chocado contra una pared, eso no era una dirección..")
                self.hp -= 10
                direction = ""