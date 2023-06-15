
from Class_Aluno import*

if __name__=="__main__":
    Inf=[["Cárine Gonçalves", 11, 13],["José Cruz", 14, 16],["Paulo Sousa", 18,20],["Gilberto Moreira", 18,16]]
    
    Pauta={}
    for a in Inf:
        E=EstudanteInf(a[0],a[1],a[2])
        Pauta[E.nome]=E.ClassFinal()
    print(Pauta)
    #E.Introdução_dados()
    #E.Apresentação()