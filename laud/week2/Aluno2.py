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

def imprime_aluno(E):
  print(f'{E.Nome:^10s} teve a classificação final de {E.ClassificacaoFinal():<.2f} valores')

#Programa principal
if __name__=="__main__":
    turma=[]
    n_alunos=int(input("Introduza o número de alunos:"))
    for i in range(n_alunos):
        turma.append(EstudanteInf(input("Qual o nome:"),int(input("Nota Teste 1:")),int(input("Nota Teste 2:"))))
    for i in range(n_alunos):
        print(imprime_aluno(turma[i]))
        #print(f"{turma[i].Nome} teve a classificação final de {turma[i].ClassificacaoFinal()} valores")