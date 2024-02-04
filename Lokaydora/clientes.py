
clientes = 'clientes.txt'
pessoa = []
pessoa_ex = {'id': 4, 'nome': 'Maria Clara', 'idade': 18}
contador_id_p = 0

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

def listarClientes():
    for consumidores in pessoa:
        print('\n Id: {} |'.format(consumidores['id']), end = ' ')
        print('Nome: {} |'.format(consumidores['nome']), end = '')
        print('Idade: {}'.format(consumidores['idade']), end = ' ')

def lerArquivoP():
    if not arquivoExiste(clientes):
        criarArquivo(clientes)
    try: 
        a = open(clientes, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
        conteudo = a.read()
        if conteudo != "":
            for carro in conteudo.split('*'):
                if carro != "":
                    dados = carro.split(',')
                    pessoa.append({'id': dados[0],'nome': dados[1], 'idade': dados[2],})
            global contador_id_p
            maior_id = 0 
            for p in pessoa:
                if p['id'] in dados:
                    p_int = int(p['id'])
                    if p_int > maior_id:
                        maior_id = p_int

def adicionarArquivoP():
    nome = str(input('Digite o nome do cliente: '))
    idade = int(input('Digite a idade do cliente: '))
    global contador_id_p 
    pessoa.append({'id': contador_id_p, 'nome': nome, 'idade': idade})
    contador_id_p = contador_id_p + 1 

def salvarArquivoP():
    try:
        a = open(clientes,'wt+')
        a.truncate()
    except:
        print('Não foi possível salvar o arquivo!')
    else:
        for p in pessoa:
            text = str(p["id"])+","+str(p["nome"])+","+str(p["idade"])+"*" 
            a.write(text)


    