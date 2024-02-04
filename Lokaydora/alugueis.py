aluguel = []
ultimos_arq = 'Lokaydora/ultimosalugueis.txt'
alugados_ex = {'id': 1, 'nome': 'Carolina','idade': 24, 'modelos': 'fiat'}

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

# ---- #

def listarAlugueis():
    for alugueis in aluguel:
        print('Nome: {} |'.format(alugueis['nome']), end = ' ')
        print('Idade: {} |'.format(alugueis['idade']), end = ' ')
        print('Modelo: {}'.format(alugueis['modelo']))

contador_id = 0 
def lerArquivoC():
    if not arquivoExiste(ultimos_arq):
        criarArquivo(ultimos_arq)
    try: 
        a = open(ultimos_arq, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
        conteudo = a.read()
        if conteudo != "":
            for carro in conteudo.split('*'):
                if carro != "":
                    dados = carro.split(',')
                    aluguel.append({'id': dados[0], 'nome': dados[1],'idade': dados[2], 'modelo': dados[3]})
            global contador_id_c
            maior_id = 0 
            for alugados in aluguel:
                if alugados['id'] > maior_id:
                    maior_id = alugados['id']
            contador_id_c = maior_id + 1 

def adicionarArquivoC():
    modelo = str(input('Informe o modelo do carro: '))
    nome = str(input('Digite o nome do cliente: '))
    idade = int(input('Digite a idade do cliente: '))
    global contador_id 
    aluguel.append({'id':contador_id,'nome': nome, 'idade': idade, 'modelo': modelo})
    contador_id = contador_id + 1 

def salvarArquivo():
    try:
        a = open(ultimos_arq,'wt+')
        a.truncate()
    except:
        print('Não foi possível salvar o arquivo!')
    else:
        for i in aluguel:
          text = str(i["id"])+","+str(i["nome"])+","+str(i['idade'])+","+str(i["modelo"])+"*" 
          a.write(text)

#----#

