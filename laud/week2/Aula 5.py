# Construtor

class EstudanteInf:
  def __init__(self, N, T1, T2):
    self.__nome=N
    self.__teste1=T1
    self.__teste2=T2
  
  def get_nome(self):  
    return self.__nome

  def set_nome(self, N): #new_name)
    self.__nome = N #new_name

if __name__ == "__main__":
  E =  EstudanteInf("", 0, 0)
  E.nome = input("Digite o nome correto: ")
  print(E.nome)
