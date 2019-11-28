import glob, os, codecs, sys, codecs

#####Funções das aulas para tokenização...######
def limpa_tela():
    os.system('cls') or None

def tokenizacao(documento):
    return documento.split(" ")

def remover_repetidas(lista_palavras):
    return sorted(filter(None,list(set(lista_palavras))))

def remover_stopwords(lista_palavras, stopwords):    
    nova_lista = []
    for p in lista_palavras:
        if p not in stopwords:
            nova_lista.append(p)

    return nova_lista

def normalizacao(lista_palavras):
    nova_lista = []
    simbolos = list('.,+/?:;!@#$%')
    for p in lista_palavras:
        p = p.lower()
        for s in simbolos:
            if s in p:
                p = p.replace(s,'')
        nova_lista.append(p)
    return nova_lista

def indexar(lista_palavras, arq, dic):
    for p in lista_palavras:
        if p in dic:
            docs = dic[p]
            docs.append(arq)
        else:
            dic[p] = [arq]
def merge(lista1, lista2):
    nova_lista = []
    lista1.sort()
    lista2.sort()

    p1 = 0
    p2 = 0
    while p1 < len(lista1) and p2 < len(lista2):
        if lista1[p1] == lista2[p2]:
            nova_lista.append(lista1[p1])
            p1 += 1
            p2 += 1
        else:
            if lista1[p1] < lista2[p2]:
                p1 += 1
            else:
                p2 += 1
    return nova_lista

######Funções para funcionamento do trabalho #####
def seleciona_stopwords():
    stopwords = []
    texto_sw = codecs.open('stopwords.txt', "r", "UTF-8")
    linhas = texto_sw.readlines()
    for linha in linhas:
        stopwords.append(linha.replace('\n', '').strip().lower())
    texto_sw.close()
    return stopwords


def criar_documento():
    print("---- Criador de documentos ----")
    nome = input("Digite o nome do arquivo:\n")
    arquivo = codecs.open('docs/' + nome + '.txt', 'w', 'UTF-8')
    texto = input("Digite o conteúdo do arquivo:\n")
    arquivo.write(texto)
    arquivo.close()

def indexador():
    for arquivo in glob.glob(pasta):
        documento = ''
        arquivo_lido = codecs.open(arquivo, "r", "UTF-8-sig")
        ler_linha = arquivo_lido.readlines()

        for linha in ler_linha:
            documento = documento + linha.replace("\r\n", " ")
        arquivo_lido.close
        ###processo de "limpeza" do arquivo
        arquivo_limpo = tokenizacao(documento)
        arquivo_limpo = normalizacao(arquivo_limpo)        
        arquivo_limpo = remover_repetidas(arquivo_limpo)
        stopwords = seleciona_stopwords()
        arquivo_limpo = remover_stopwords(arquivo_limpo, stopwords)
        indexar(arquivo_limpo, arquivo, dic)

def buscador(dic):
    buscador = input("Digite a(s) palavra(s) que deseja buscar:\n").lower().split(" ")
    lista = []
    for p in buscador:
        lista.append(dic[p])
    
    if (opcao == 1):
        buscador = list(set().union(*lista))
        print(buscador)

    elif opcao == 2:
        i = 0
        buscador = lista[0]
        while i < len(lista)-1:
            if len(lista) == 1:
                print(buscador)
                break
            else:
                buscador = merge(buscador, lista[i+1])
                i += 1
        print(buscador)
    elif opcao == 3:
        print("Opção atualmente não desenvolvida.")


###### Main #########
limpa_tela()
dic = dict()
while True:
    print("------- INDEXAÇÃO ------- \n\n")
    opcao = int(input('Selecione uma opção:\n\n1. Criar novo documento\n2. Indexar documentos\n3. Realizar consultas\n4. Mostrar indice invertido\n\n'))
            
    if opcao == 1:
        limpa_tela()
        criar_documento()
        limpa_tela()
        print("Documento criado com sucesso!")

    elif opcao == 2:
        limpa_tela()
        pasta = "docs/*txt"
        indexador()
        limpa_tela()
        print("Indexado com sucesso\n")
        

    elif opcao == 3:
            limpa_tela()
            opcao = int(input("Selecione uma opção para buscar:\n\n1. Usando operador OR\n2. Usando operador AND\n3. Usando expressões booleanas\n"))
            limpa_tela()
            buscador(dic)

    elif opcao == 4:
        limpa_tela
        for chave in dic.keys():
            print(str("A palavra {}' é encontrada no(s) documento(s) {}:".format(chave, dic[chave])))

