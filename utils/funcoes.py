from csv import DictReader, DictWriter
from unicodedata import normalize



# Função para ler os arquivos livros.csv e bibliotecas.csv
def ler_arquivo(arquivo, header=False, aninhada=False):
    with open(arquivo) as arq:
        csv = DictReader(arq)

        # Se o header for verdadeiro retorne uma lista com os valores da chave
        # que o usuario passar 
        if header:
            return [linha.get(header) for linha in csv]

        # Se o parametro 'aninhada' for verdadeiro retorna uma lista com
        # os valores do dicionario
        elif aninhada:
            return [list(linha.values()) for linha in csv] 

        # Se nenhum dos parametros acima for verdadeiro retorne apenas uma lista
        # de dicionarios do arquivo
        return [linha for linha in csv]


# Função para remover acentuação de strings e deixá-las em lowercase
def meu_normalize(variavel):
    normaliza = normalize('NFD', variavel.lower()).encode('ascii', 'ignore')

    return normaliza.decode('utf-8')


# Escreve no arquivo livros.csv
def escrita_livro(nova_lista, cabecalho):
    with open('livros.csv', 'w') as arq:
        csv = DictWriter(arq, fieldnames=cabecalho)
        csv.writeheader()
        for n in nova_lista:
            csv.writerow(
                {'Título': n.get('Título'),
                'Autor': n.get('Autor'),
                'Data de Lançamento': n.get('Data de Lançamento'),
                'Gênero': n.get('Gênero'),
                'Quantidade': n.get('Quantidade')}
            )


# Escreve no arquivo bibliotecas.csv
def escrita_biblioteca(nova_lista, cabecalho_biblioteca):
    with open('bibliotecas.csv', 'w') as arq:
        csv = DictWriter(arq, fieldnames=cabecalho_biblioteca)
        csv.writeheader()
        for n in nova_lista:
            csv.writerow(
                {'Nome da Biblioteca': n.get('Nome da Biblioteca'),
                'Endereço': n.get('Endereço'),
                'Número': n.get('Número'),
                'Quantidade de Catálogos': n.get('Quantidade de Catálogos')}
            )
