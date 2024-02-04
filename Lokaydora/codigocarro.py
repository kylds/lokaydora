from colorama import Fore, Back, Style



aluguel = []

def menu(lista):
    linha(Fore.RED + Back.WHITE + 'LOKAYDORA')
    for i, elementos in enumerate(lista):
        print(Fore.BLACK + Back.WHITE +'{} - {}'.format(i+1,elementos))

def linha(msg):
    print(Fore.RED + Back.WHITE +'-'*len(msg))
    print(msg)
    print(Fore.RED + Back.WHITE +'-'*len(msg))

def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False 
    else:
        return True 

def criarArquivo(arq):
    try: 
        a = open(arq, 'wt+')
    except: 
        print('Erro ao criar arquivo!')
    else:
        print('Arquivo {} criado!'.format(a))
        a.close()

contador_id = 0
contador_id_c = 0


def lerArquivoC(arq):
    try: 
        a = open(arq, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
        conteudo = a.read()
        if conteudo != "":
            for carro in conteudo.split('*'):
                if carro != "":
                    dados = carro.split(',')
                    aluguel.append({'Id': dados[0], 'Nome': dados[1], 'Modelo': dados[2]})
            global contador_id_c
            maior_id = 0 
            for alugados in aluguel:
                if alugados['Id'] > maior_id:
                    maior_id = alugados['Id']
            contador_id_c = maior_id + 1 



def adicionarArquivoC(arq):
    ano = int(input('Informe o ano do carro: '))
    modelo = str(input('Informe o modelo do carro: '))
    marca = str(input('Informe a marca do carro: '))
    nome = str(input('Digite o nome do cliente: '))
    idade = int(input('Digite a idade do cliente: '))
    global contador_id 
    aluguel.append({'Id': contador_id, 'Ano': ano,'Modelo': modelo,'Marca': marca, 'Nome': nome, 'Idade': idade})
    contador_id = contador_id + 1 


def excluirArquivo(arq):
    idx = int(input('Digite o índice do carro: '))
    remover = 0
    for id in range(0,len(info_carro)):
        if info_carro[id]['Id'] == idx:
            remover = id 
        info_carro.pop(remover)
    for p in range(0,len(pessoa)):
        if pessoa[id]['Id'] == idx:
            remover = id 
        pessoa.pop(remover)

def salvarArquivo(arq):
    try:
        a = open(arq,'wt+')
        a.truncate()
    except:
        print('Não foi possível salvar o arquivo!')
    else:
        for i in info_carro:
          text = str(i["Id"])+","+str(i["Ano"])+","+str(i["Modelo"])+","+str(i["Marca"])+"*" 
          a.write(text)





alugados = 'carrosalugados.txt'

ultimos_alugados = 'ultimosalugueis.txt'







if not arquivoExiste(ultimos_alugados):
    criarArquivo(ultimos_alugados)