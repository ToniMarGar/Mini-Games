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
        self.hp = 150
        self.specie = "Enano"
        self.speed = 12
    
    def elf_char(self):
        self.hp = 80
        self.specie = "Elfo"
        self.speed = 8
    

    def trap(self):
    
        prob = random.random()

        if prob < 0.6:
            print("Has caido en una trampa!")
            self.hp -= 30
        else:
            print("Un monstruo te ha encontrado!")
            choice = input("Que quieres hacer? ")
            #obj = random.random()
            if choice == "Atacar":
                attack = random.random()
                if attack < 0.3:
                    print("Has derrotado al monstruo")
                elif 0.3 <= attack and attack < 0.7:
                    print("Combates con el monstruo")
            if choice == "Huir":
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
            print("Avanzas a la siguiente sala.")
        else:
            print("Has encontrado un objeto!")
            obj = random.random()
            if obj < 0.8:
                self.inventory.append("Potion")
            else:
                self.inventory.append("Sword")
    
    def action(self):
        direction = input("Hacia donde quieres ir? ")
        if direction != "":
            prob = random.random()
            if prob < 0.5:
                self.advance()
            else:
                self.trap()
