class mostra_ipmon:
    def __init__(self,ipmon):
        self.ipmon=ipmon
    def dados(self,ipmon):    
        print("Inspermon : {0}".format(self.ipmon["Nome"]))
        print("Ataque = {0}".format(self.ipmon["Ataque"]))
        print("Vida = {0}".format(self.ipmon["Vida"]))
        print("Nome Ataque = {0}".format(self.ipmon["Nome Ataque"]))
        print("Defesa = {0}".format(self.ipmon["Defesa"]))
        print("Experiência = {0}".format(self.ipmon["Experiência"]))
        return ("")
