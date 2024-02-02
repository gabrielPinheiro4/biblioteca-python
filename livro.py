from csv import *
import datetime
import operator
from utils import meu_normalize
from utils import csv_aquivo
from utils import cabecalho
from utils import csv_arquivo_header

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


    #Cria um novo arquivo na ordem desejada.
    def ordernar(self, decisao):
        with open(f'{decisao}.csv', 'w') as arq:
            csv = DictWriter(arq, fieldnames=cabecalho)
            csv.writeheader()

            linha = sorted(Livro.csv_aquivo(), key=lambda livro: livro.get(decisao))
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

        #Cria uma nova lista de dicionarios com as chaves e valores em lowercase e sem acentuação
        nova_lista = []
        for livro in csv_aquivo():
            nova_lista.append(
                {
                    meu_normalize(chave):
                    meu_normalize(valor) for chave, valor in livro.items()
                }
            )
        
        #Cria uma lista filtrando os elementos de acordo com a pesquisa do usuario
        lista = list(
            filter(
                lambda x: 
                meu_normalize(procurar.lower()) in x.get(meu_normalize(listar_por.lower())), nova_lista))
        
        return lista
    
    @staticmethod
    def listar_idade_livro(operador, idade):
        operador_dict = {
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '==': operator.eq,
        }

        nova_lista = []
        for livro in csv_aquivo():
            idade_livro = datetime.date.today().year - int(livro.get('Data de Lançamento'))

            livro.update({'idade_livro': idade_livro})
            nova_lista.append(livro)

        return list(filter(lambda x: operador_dict.get(operador)(x.get('idade_livro'), idade), nova_lista))
        

livro = Livro(
        csv_arquivo_header('Título'),
        csv_arquivo_header('Autor'), 
        csv_arquivo_header('Data de Lançamento'), 
        csv_arquivo_header('Gênero'), 
        csv_arquivo_header('Quantidade')
    )

# print(livro.listar('titulo', 'o hobbit'))
print(livro.listar_idade_livro('==', 180))