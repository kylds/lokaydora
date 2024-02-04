from colorama import Fore, Back, Style 

def menu(lista):
    linha(Fore.RED + Back.WHITE + 'MENU')
    for c, i in enumerate(lista):
        print('{} - {}'.format(c+1,i))

def linha(msg):
    print('-'* len(msg))
    print(msg)
    print('-'* len(msg))

def arquivoExiste(arq):
    try:
        a = open(arq,'rt')
        a.close()
    except FileNotFoundError:
        return False 
    else:
        return True

def criarArq(arq):
    try:
        a = open(arq,'wt+')
        a.close()
    except:
        print('Erro! tente novamente')
    else:
        print('Arquivo {} criado!'.format(arq))

def lerArq(arq):
    try:
        a = open(arq,'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        print('--------------------------------')
        for linha in a: 
            print('{}'.format(linha))
        print(a.read())
        print('--------------------------------')

def adicionarArq(arq, ano = '0', modelo = 'desconhecido',marca = 'desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Ocorreu um erro ao abrir o arquivo')
    else: 
        try:
            print('Ano - Modelo - Marca')
            a.write('{} - {} - {}'.format(ano,modelo,marca))
        except: 
            print('Houve um erro no cadastro!')
        else:
            print('Novo registro do modelo {}'.format(modelo))
            a.close()

def carrosADD(arq,ano = '0', modelo = 'desconhecido', nome = 'desconhecido', idade = '0'):
    try:
        a = open(arq, 'at')
    except:
        print('Ocorreu um erro ao abrir o arquivo')
    else:
        try:
            a.write('{} - {} - {} - {}'.format(ano,modelo,nome,idade))
        except:
            print('Ocorreu um erro')
        else:
            a.close()

def clientesArq(arq, pessoa = 'desconhecida', idade = '0'):
    try:
        a = open(arq,'at')
    except:
        print('Ocorreu um erro ao abrir o arquivo')
    else:
        try: 
            a.write('{} - {}'.format(pessoa,idade))
        except:
            print('Ocorreu um erro')
        else: 
            print('Novo registro de {}'.format(pessoa))
            a.close()  

carros = 'carrosdisponíveis.txt'
aluguel = 'aluguelcarros.txt'
alugados = 'totalalugados.txt'
clientes = 'clientes.txt'
alugueis = 'totalalugueis.txt'

if not arquivoExiste(carros):
    criarArq(carros)

if not arquivoExiste(aluguel):
    criarArq(aluguel)

if not arquivoExiste(alugados):
    criarArq(alugados)

if not arquivoExiste(clientes):
    criarArq(clientes)

if not arquivoExiste(alugueis):
    criarArq(alugueis)