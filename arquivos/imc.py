
from time import sleep

def linha(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))

def calculo(peso,altura):
    sleep(0.5)
    result = altura * altura 
    imc = peso/ result 
    linha('IMC')
    print('Seu IMC é {:.2f}'.format(imc))
    return imc 