from csv import *
import datetime
import operator
from biblioteca_python.constants.livro_const import CABECALHO
from biblioteca_python.utils.funcoes import (
    meu_normalize,
    csv_arquivo_header,
    csv_aquivo
)
 

class Livro:

    def __init__(self, titulo, autor, data_lancamento,genero, quantidade):
        self.__titulo = titulo
        self.__autor = autor
        self.__data_lancamento = data_lancamento
        self.__genero = genero
        self.__quantidade = quantidade    

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor
    
    @property
    def data(self):
        return self.__data_lancamento

    @property
    def genero(self):
        return self.__genero

    @property
    def quantidade(self):
        return self.__quantidade


    # Cria um novo arquivo na ordem desejada.
    def ordernar(self, decisao):
        with open(f'{decisao}.csv', 'w') as arq:
            csv = DictWriter(arq, fieldnames=CABECALHO)
            csv.writeheader()

            # Cria uma nova lisata de dicionarios, poŕem ordenada com o valor que o usuario passar 
            linha = sorted(csv_aquivo(), key=lambda livro: livro.get(decisao))
            for i in linha:
                csv.writerow(
                    {
                        'Título': i.get('Título'),
                        'Autor': i.get('Autor'),
                        'Data de Lançamento': i.get('Data de Lançamento'),
                        'Gênero': i.get('Gênero'),
                        'Quantidade': i.get('Quantidade')
                        
                    }
                )

    
    def listar(self, listar_por, procurar):

        # Cria uma nova lista de dicionarios com as chaves e valores em lowercase e sem acentuação
        nova_lista = []
        for livro in csv_aquivo():
            nova_lista.append(
                {
                    meu_normalize(chave):
                    meu_normalize(valor) for chave, valor in livro.items()
                }
            )
        
        # Cria uma lista filtrando os elementos de acordo com a pesquisa do usuario
        lista = list(
            filter(
                lambda x: 
                meu_normalize(procurar.lower()) in x.get(meu_normalize(listar_por.lower())), nova_lista))
        
        return lista
    
    @staticmethod
    def listar_idade_livro(operador, idade):
        # Cria um dicionario contendo um operador em fortado string e como chave
        # sua funcionalidade como valor do dicionario 
        operador_dict = {
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '==': operator.eq,
        }

        nova_lista = []

        for livro in csv_aquivo():

            # Variável contendo o ano atual
            ano_atual = datetime.date.today().year

            # Variável contendo a idade de cada livro
            # Ano atual - ano do livro
            idade_livro = ano_atual - int(livro.get('Data de Lançamento'))

            # Adiciona uma chave 'idade_livro' para todos os dicionarios contendo
            # o valor a idade do livro
            livro.update({'idade_livro': idade_livro})
            nova_lista.append(livro)

        # Retorna uma lista com os livros selecionados de acordo com a operação
        # do usuário
        return list(filter(lambda x: operador_dict.get(operador)(x.get('idade_livro'), idade), nova_lista))
        

# Instanciando o objeto com os dados do arquivo livros.csv
livro = Livro(
        csv_arquivo_header('Título'),
        csv_arquivo_header('Autor'), 
        csv_arquivo_header('Data de Lançamento'), 
        csv_arquivo_header('Gênero'), 
        csv_arquivo_header('Quantidade')
    )
