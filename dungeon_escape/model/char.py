
class Character:
    def __init__(self,specie,hp,speed):

        self.name = input("Que nombre quieres darle a tu personaje? ")
        self.specie = specie
        self.hp = hp
        self.speed = speed
        self.inventory=[]
        
        '''match stats:
            case 1:
                self.specie=Character.specie_list[1]
            case 2:
                self.specie=Character.specie_list[2]
            case 3:
                self.specie=Character.specie_list[3]
        self.create_char()'''

        
    def create_char(self):
        # Falta elección de personaje

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
