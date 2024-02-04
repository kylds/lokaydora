from carro import * 
from colorama import Fore, Back, Style 


while True:
    menu(['Carros disponíveis','Aluguel de carros','Devolução de carros','Carros alugados','Clientes','Aluguéis realizados','Sair \n'])
    op = int(input(Fore.BLACK + Back.WHITE + 'Digite sua opção: '))
    try:
        if op == 1:
            linha(Fore.BLACK + Back.WHITE + 'CARROS')
            lerArq(carros)
            add = str(input('Deseja adicionar algum carro? [S/N]: ')).upper()
            if add == 'S':
                 ano = int(input('Digite o ano do carro: '))
                 modelo = str(input('Digite o modelo do carro: '))
                 marca = str(input('Digite a marca do carro: ')) 
                 adicionarArq(carros,ano,modelo,marca)
        elif op == 2: 
            linha(Fore.BLACK + Back.WHITE +'ALUGUEL')
            lerArq(aluguel)
            aluga = str(input('Deseja alugar algum carro? [S/N]')).upper()
            if aluga == 'S':
                ano = int(input('Digite o ano do carro: '))
                modelo = str(input('Digite o nome do modelo: '))
                nome = str(input('Digite o nome da pessoa que vai alugar: '))
                idade = int(input('Digite a idade da pessoa que vai alugar: '))
                carrosADD(aluguel,ano,modelo,nome,idade)
                carrosADD(alugueis,ano,modelo,nome,idade)
                carrosADD(alugados,ano,modelo,nome,idade)
        elif op == 3:
            linha(Fore.BLACK + Back.WHITE +'DEVOLUÇÃO')
            pedido = str(input('Deseja devolver o carro? [S/N]: ')).upper()
            if pedido == 'S':
                ano = int(input('Digite o ano do carro: '))
                modelo = str(input('Digite o modelo do carro: '))
                marca = str(input('Digite a marca do carro: ')) 
                adicionarArq(carros,ano,modelo,marca)
        elif op == 4:
            linha(Fore.BLACK + Back.WHITE +'ALUGADOS') 
            lerArq(alugados)
        elif op == 5:
            linha(Fore.BLACK + Back.WHITE +'CLIENTES')
            lerArq(clientes)
            c = str(input('Deseja adicionar um novo cliente? [S/N]: ')).upper()
            if c == 'S':
                nome = str(input('Digite o nome do cliente: '))
                idade = int(input('Digite a idade do cliente: '))
                clientesArq(clientes,nome,idade)
        elif op == 6:
            linha(Fore.BLACK + Back.WHITE +'ALUGUÉIS REALIZADOS')
            lerArq(alugueis)
    except ValueError:
        print('Erro! digite novamente')
    else:
          if op == 7:
            print(Fore.BLUE + 'Programa finalizado! Volte sempre a locadora')
            break 
