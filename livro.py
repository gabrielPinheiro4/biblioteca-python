from csv import *

class Livro:

    @staticmethod
    def csv_aquivo():
        with open('livros.csv') as arq:
            csv = DictReader(arq)
            return [linha for linha in csv]


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
            

a = Livro(
        Livro.csv_arquivo_header('Título'), 
        Livro.csv_arquivo_header('Autor'), 
        Livro.csv_arquivo_header('Data de Lançamento'), 
        Livro.csv_arquivo_header('Gênero'), 
        Livro.csv_arquivo_header('Quantidade')
    )


print(a.ordernar('Título'))
a.ordernar('Autor')
a.ordernar('Data de Lançamento')