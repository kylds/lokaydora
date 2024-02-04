import alugueis as aluguel  

alugados_ult = []
alugados_arq = 'Lokaydora/carrosalugados.txt'
alugados_ex = {'id': 5, 'ano': 2023, 'modelo': 'Porsche', 'nome': 'Gabriel', 'idade': 26}

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

#----#

def listarUltimosAlugados():
    if not arquivoExiste(alugados_arq):
        criarArquivo(alugados_arq)
    try:
        a = open(alugados_arq, 'rt')
    except:
        print('Erro ao abrir arquivo')
    else:
        aluguel.listarAlugueis()

contador_id_ua = 0

def lerArquivoUA():
    try: 
        a = open(alugados_arq, 'rt')
    except: 
        print('Erro ao ler o arquivo')
    else:
        conteudo = a.read()
        if conteudo != "":
            for carro in conteudo.split('*'):
                if carro != "":
                    dados = carro.split(',')
                    alugados_ult.append({'id': dados[0], 'ano': dados[1], 'modelo': dados[2], 'nome': dados[3], 'idade': dados[4]})
            global contador_id_ua
            maior_id = 0 
            for id in alugados_ult:
                if id['id'] > maior_id:
                    maior_id = id['id']
            contador_id_ua = maior_id + 1 

def salvarArquivo():
    try:
        a = open(alugados_arq,'wt+')
        a.truncate()
    except:
        print('Não foi possível salvar o arquivo!')
    else:
        for i in alugados_ult:
          text = str(i["id"])+","+str(i['ano'])+","+str(i['modelo'])+","+str(i["nome"])+","+str(i['idade'])+","+str(i["modelo"])+"*" 
          a.write(text)

#-----# 
