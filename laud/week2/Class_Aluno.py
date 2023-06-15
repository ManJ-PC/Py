import math
class EstudanteInf:
    
    def __init__(self,N,T1,T2):
        self.nome=N
        self.teste1=T1
        self.teste2=T2
    
    def getnome(self):
        return self.nome
    
    def setnome(self,N):
        self.nome=N
    
    def getteste1(self):
        return self.teste1
    
    def setteste1(self,T1):
        self.teste1=T1
        
    def getteste2(self):
        return self.teste2
    
    def setteste2(self,T2):
        self.teste2=T2
        
    def ClassFinal(self):
        return math.floor((self.teste1+self.teste2)/2)
    
    def Apresentação(self):
        print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Class. Final':^15}")
        print(f"{self.nome:^15}{self.teste1:^10}{self.teste2:^10}{self.ClassFinal():^16}")
    
    def Introdução_dados(self):
        self.nome=input("Digite o nome: ")
        self.teste1=(int(input("Qual a nota1: ")))
        self.teste2=(int(input("Qual a nota2: ")))