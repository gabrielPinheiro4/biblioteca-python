from csv import DictReader, DictWriter
from unicodedata import normalize
from constants.livro_const import (
    ABRIR_ARQUIVO_LIVRO,
    CABECALHO
)
from constants.biblioteca_const import (
    ABRIR_ARQUIVO_BIBLIOTECA,
    CABECALHO_BIBLIOTECA
)


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


def faz_emprestimo_devolucao(eh_emprestimo=False, eh_devolucao=False, livro=False, biblioteca=False):
    novo_arq = []
    novo_arq_biblioteca = []

    for livros in ABRIR_ARQUIVO_LIVRO:
        for bibliotecas in ABRIR_ARQUIVO_BIBLIOTECA:
            if livro == {
                meu_normalize(chave.lower()):
                meu_normalize(valor.lower()) for chave, valor in livros.items()
            } and biblioteca in bibliotecas.get('Nome da Biblioteca'):
                
                if eh_emprestimo:
                    quantidade_nova = int(livros.get('Quantidade'))
                    quantidade_nova -= 1
                    livros.update({'Quantidade': quantidade_nova})

                    quantidade_nova_b = int(bibliotecas.get('Quantidade de Catálogos'))
                    quantidade_nova_b -= 1
                    bibliotecas.update({'Quantidade de Catálogos': quantidade_nova_b})

                if eh_devolucao:
                    quantidade_nova = int(livros.get('Quantidade'))
                    quantidade_nova += 1
                    livros.update({'Quantidade': quantidade_nova})

                    quantidade_nova_b = int(bibliotecas.get('Quantidade de Catálogos'))
                    quantidade_nova_b += 1
                    bibliotecas.update({'Quantidade de Catálogos': quantidade_nova_b})

                novo_arq.append(livros)
                novo_arq_biblioteca.append(bibliotecas)
            escrita_livro(novo_arq, CABECALHO)
            escrita_biblioteca(novo_arq_biblioteca, CABECALHO_BIBLIOTECA)
