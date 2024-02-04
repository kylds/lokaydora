from codigocarro import * 
import carros as carros
import alugueis as alugueis
import clientes as clientes 
import devolvercarro as devolver 
from colorama import Fore, Back, Style

carros.lerArquivo()
alugueis.lerArquivoC()
clientes.lerArquivoP()
devolver.lerArquivoUA()

while True:
    menu(['Carros disponíveis', 'Alugar Carro', 'Devolver carro','Carros alugados','Clientes','Últimos aluguéis realizados','Sair'])
    op = int(input(Fore.BLUE + Back.WHITE + 'Digite sua opção: '))
    try:
        if op == 1: 
            linha('CARROS DISPONÍVEIS')
            carros.listarTodosOsCarros()
            add = str(input('Gostaria de adicionar um carro? [S/N]:')).upper()
            if add == 'S':
                carros.adicionarNovoCarro()           
        elif op == 2:
            linha('AlUGAR CARRO')
            alugueis.listarAlugueis()
            add = str(input('Gostaria de alugar um carro? [S/N]:')).upper()
            if add == 'S':
                alugueis.adicionarArquivoC()
        elif op == 3: 
            linha('DEVOLUÇÃO DO CARRO')
            add = str(input('Deseja devolver o carro? [S/N]: ')).upper()
            if add == 'S':
                devolver.excluirArquivo()
        elif op == 4:
            linha('CARROS ALUGADOS')
            alugueis.listarAlugueis()
        elif op == 5:
            linha('CLIENTES')
            clientes.listarClientes()
            add = str(input('\n Gostaria de adicionar um novo cliente? [S/N]:')).upper()
            if add == 'S':
                clientes.adicionarArquivoP()
        elif op == 6:
            linha('ALUGADOS RECENTEMENTE')
            devolver.listarUltimosAlugados() 
    except ValueError:
        print('ERRO! tente novamente')
    else:
        if op == 7:
            print(Fore.BLUE + Back.WHITE + Style.DIM + 'LOKAYDORA FINALIZADA! Volte sempre')
            break

carros.salvarArquivo()
alugueis.salvarArquivo()
clientes.salvarArquivoP()
devolver.salvarArquivo()