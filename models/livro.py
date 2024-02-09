import datetime
import operator
from biblioteca_python.utils.funcoes import (
    meu_normalize,
    ler_arquivo
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
    
    def listar(self, listar_por, procurar):

        # Cria uma lista vazia
        nova_lista = []

        # Adiciona na lista os dicionarios de livros.csv porém com as chaves e
        # valores em lowercase e sem acentuação
        for livro in ler_arquivo('livros.csv'):
            nova_lista.append({
                meu_normalize(chave):
                meu_normalize(valor) for chave, valor in livro.items()
            })

        # Cria uma lista contendo os livros que o usuario passou na pesquisa
        lista = list(
            filter(
                lambda x: 
                meu_normalize(procurar.lower()) in x.get(meu_normalize(listar_por.lower())), nova_lista))

        return lista

    @staticmethod
    def listar_idade_livro(operador, idade):
        # Cria um dicionario contendo um operador em fortado string como chave e
        # sua funcionalidade como valor
        operador_dict = {
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '==': operator.eq,
        }

        nova_lista = []

        for livro in ler_arquivo('livros.csv'):

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
        ler_arquivo('livros.csv', 'Título'),
        ler_arquivo('livros.csv', 'Autor'), 
        ler_arquivo('livros.csv', 'Data de Lançamento'), 
        ler_arquivo('livros.csv', 'Gênero'), 
        ler_arquivo('livros.csv', 'Quantidade')
    )
