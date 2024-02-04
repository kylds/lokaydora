import matplotlib.pyplot
from arquivos.imc import *

valor_imc = ['18,5','18,5-24,9','25-29,99','20-24,99','35-39,99','40']
clas = ['Abaixo do peso normal','Peso normal','Excesso de peso','Obesidade tipo I','Obesidade tipo II', 'Obesidade tipo III']

matplotlib.pyplot.plot(valor_imc, clas)
linha('MENU')

while True:
    try:
        peso = float(input('Digite o peso [KG]: '))
        altura = float(input('Digite a altura [M]: '))
        calculo(peso,altura)
    except ValueError:
        print('Erro! digite novamente')
    else:
        print('Seu peso: {} \n Sua altura: {}'.format(peso,altura))
        print('Analise na tabela seu IMC!')
        matplotlib.pyplot.show()
        break 