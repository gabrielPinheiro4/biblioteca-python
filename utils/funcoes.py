from csv import DictReader
from unicodedata import normalize


#Função que retorna uma lista de dicionarios do arquivo livros.csv
def csv_aquivo():
    with open('livros.csv') as arq:
        csv = DictReader(arq)

        return [linha for linha in csv]


#Função para instanciar o objeto com os dados do arquivo livros.csv
def csv_arquivo_header(header):
    with open('livros.csv') as arq:
        csv = DictReader(arq)

        return [livro[header] for livro in csv]
    

#Retorna uma lista de dicionarios com as linhas do arquivo bibliotecas.csv
def csv_biblioteca():
    with open('bibliotecas.csv') as arq:
        csv = DictReader(arq)

        return [linha for linha in csv]


#Funcão para instanciar o objeto com so dados do arquivo biblioteca.csv
def csv_arquivo_biblioteca(header):
    with open('bibliotecas.csv') as arq:
        csv = DictReader(arq)

        return [x[header] for x in csv]


#Função para remover acentuação de strings
def meu_normalize(variavel):
    normaliza = normalize('NFD', variavel.lower()).encode('ascii', 'ignore')

    return normaliza.decode('utf-8')
