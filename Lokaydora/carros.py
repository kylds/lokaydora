carros = []
contador_id = 0
arq_carros = "Lokaydora/carrosdisponiveis.txt"
carro_exemplo = {"id": 1,"ano": 2020,"modelo": "A3","marca":"Audi"} #todos os carros serão assim.

#----

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
#---

def lerArquivo():
    if not arquivoExiste(arq_carros):
        criarArquivo(arq_carros)
    try: 
        a = open(arq_carros, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
        conteudo = a.read()
        if conteudo != "":
            for carro in conteudo.split('*'):
                if carro != "":
                    dados = carro.split(',')
                    carros.append({'id': int(dados[0]), 'ano': int(dados[1]),'modelo': dados[2],'marca': dados[3]})
            global contador_id
            maior_id = 0 
            for carro in carros:
                if carro['id'] > maior_id:
                    maior_id = carro['id']
            contador_id = maior_id + 1 

def listarTodosOsCarros():
    for carro in carros:
        print("Modelo: {} ".format(carro["modelo"]))
        print("Ano: {} ".format(carro["ano"]))
        print("Marca: {} ".format(carro["marca"]))
        print("-------------")

def adicionarNovoCarro():
    ano = int(input('Informe o ano do carro: '))
    modelo = str(input('Informe o modelo do carro: '))
    marca = str(input('Informe a marca do carro: '))
    global contador_id 
    carros.append({'id': contador_id, 'ano': ano,'modelo': modelo,'marca': marca})
    contador_id = contador_id + 1 

def salvarArquivo():
    try:
        a = open(arq_carros,'wt+')
        a.truncate()
    except:
        print('Não foi possível salvar o arquivo!')
    else:
        for i in carros:
          text = str(i["id"])+","+str(i["ano"])+","+str(i["modelo"])+","+str(i["marca"])+"*" 
          a.write(text)

#-----



