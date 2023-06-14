"""Nome   alfanumerica
       Teste1 real
       Teste2 real
       
       Criar um construtor que receba três parametros
       Método ClassFinal calcular a média aritmética das notas obtidas pelo aluno
       
       João Silva 14  16
       Paulo Santos 13  15
       Ana Pereira  18  17
"""
import math
#Construtor da classe EstudanteInf()
class EstudanteInf():
    def __init__(self, N, T1, T2):
        self.Nome=N
        self.Teste1=T1
        self.Teste2=T2

#Método de classificação final da classe EstudanteInf
    def ClassificacaoFinal(self):
        return math.floor(((self.Teste1+self.Teste2)/2))

#Programa principal
if __name__=="__main__":
    E=EstudanteInf("João Silva",14,16)
    F=EstudanteInf("Paulo Santos",13,15)
    G=EstudanteInf("Ana Pereira",18,17)
    print(f"{E.Nome} teve a classificação final de {E.ClassificacaoFinal()} valores")
    print(f"{F.Nome} teve a classificação final de {F.ClassificacaoFinal()} valores")
    print(f"{G.Nome} teve a classificação final de {G.ClassificacaoFinal()} valores")
