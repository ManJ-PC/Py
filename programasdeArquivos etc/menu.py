# -*- coding: utf-8 -*-


# cardinal = 30 no módulo seguindo a nomenclatura
from lib.interface import *


  
while True:
    header()
    #try:
    option = int(input('Sua opção: ')) # str
    line(CARD)
    if option > 3 or option < 0: #or option < 0: #except(ValueError, TypeError)
        print('Option there is not exist!')
# except(ValueError, TypeError):
#     print('This did not matter\n')
#         # for i in 
    advance = str(input('\nDid you want to continue: ...')).strip().upper()[0]
    if advance == 'N':
        break #return
