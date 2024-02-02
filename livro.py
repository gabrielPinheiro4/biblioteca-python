from csv import *
import datetime
import unicodedata
import operator

class Livro:

    #Método que retorna o arquivo csv
    @staticmethod
    def csv_aquivo():
        with open('livros.csv') as arq:
            csv = DictReader(arq)
            return [linha for linha in csv]

    #Método para instanciar o objeto com os dados do csv
    @staticmethod
    def csv_arquivo_header(header):
        with open('livros.csv') as arq:
            csv = DictReader(arq)
            return [livro[header] for livro in csv]
        

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


    #Cira um novo arquivo na ordem desejada.
    def ordernar(self, decisao):
        with open(f'{decisao}.csv', 'w') as arq:
            cabecalho = [
                'Título', 
                'Autor', 
                'Data de Lançamento',
                'Gênero', 
                'Quantidade'
                ]
            csv = DictWriter(arq, fieldnames=cabecalho)
            csv.writeheader()
            linha = sorted(Livro.csv_aquivo(), key=lambda livro: livro.get(decisao))
            for i in linha:
                csv.writerow(
                    {
                        'Título': i['Título'],
                        'Autor': i['Autor'],
                        'Data de Lançamento': i['Data de Lançamento'],
                        'Gênero': i['Gênero'],
                        'Quantidade': i['Quantidade']
                        
                    }
                )

    @staticmethod
    def listar(listar_por, procurar):

        #Cria uma nova lista de dicionarios com as chaves e valores em lowercase e sem acentuação
        nova_lista = []
        for livro in Livro.csv_aquivo():
            nova_lista.append(
                {unicodedata.normalize(
                    'NFD', chave.lower()).encode(
                        'ascii', 'ignore').decode(
                            'utf-8'): unicodedata.normalize(
                                'NFD', valor.lower()).encode(
                                    'ascii', 'ignore').decode(
                                        'utf-8') for chave, valor in livro.items()})
        

        #Cria uma lista filtrando os elementos de acordo com a pesquisa do usuario
        lista = list(
            filter(
                lambda x: unicodedata.normalize(
                    'NFD', procurar.lower()).encode(
                        'ascii', 'ignore').decode(
                            'utf-8') in x[unicodedata.normalize(
                                'NFD', listar_por.lower()).encode(
                                    'ascii', 'ignore').decode(
                                        'utf-8')], nova_lista))
        
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
        for livro in Livro.csv_aquivo():
            idade_livro = datetime.date.today().year - int(livro['Data de Lançamento'])
            livro.update({'idade_livro': idade_livro})
            nova_lista.append(livro)

        return list(filter(lambda x: operador_dict[operador](x['idade_livro'], idade), nova_lista))
        

a = Livro(
        Livro.csv_arquivo_header('Título'),
        Livro.csv_arquivo_header('Autor'), 
        Livro.csv_arquivo_header('Data de Lançamento'), 
        Livro.csv_arquivo_header('Gênero'), 
        Livro.csv_arquivo_header('Quantidade')
    )


# print(a.listar('título', 'hobbit'))
# print(a.listar_idade_livro('==', 180))

