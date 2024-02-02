from biblioteca import Biblioteca
from usuario import Usuario
from livro import Livro
import unicodedata
from csv import *


class Emprestimo(Usuario, Livro, Biblioteca):
    def __init__(self, biblioteca, usuario, livro):
        self.__biblioteca = biblioteca
        self.__usuario = usuario
        self.__livro = livro

    @property
    def biblioteca(self):
        return self.__biblioteca
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def livro(self):
        return self.__livro

    @property
    def quantidade_livro(self):
        for livro in self.mostrar_livro():
            return int(livro['quantidade'])
        
    @property
    def quantidade_livro_biblioteca(self):
        for livro_biblioteca in self.mostrar_biblioteca():
            return int(livro_biblioteca['quantidade de catalogos'])

    
    def cadastrar_usuario(self,  
                cpf, 
                endereco, 
                data_nascimento,
                genero_preferido):
        super().__init__(
            self.usuario,
            cpf, 
            endereco, 
            data_nascimento,
            genero_preferido
            )
        

    def mostrar_biblioteca(self):
        #Cria uma nova lista de dicionarios em lowercase e sem acentuação do arquivo bibliotecas.csv
        nova_lista_biblioteca = []
        for biblioteca in self.csv_biblioteca():
            nova_lista_biblioteca.append(
                {unicodedata.normalize(
                    'NFD', chave.lower()).encode(
                        'ascii', 'ignore').decode(
                            'utf-8'): unicodedata.normalize(
                                'NFD', valor.lower()).encode(
                                    'ascii', 'ignore').decode(
                                        'utf-8') for chave, valor in biblioteca.items()})
        
        ##Criar uma lista filtrando os elementos de acordo com a pesquisa do usuario
        biblioteca_selecionada = list(
            filter(
                lambda x: unicodedata.normalize(
                    'NFD', self.biblioteca.lower()).encode(
                        'ascii', 'ignore').decode(
                            'utf-8') in x['nome da biblioteca'], nova_lista_biblioteca
            )
        )

        return biblioteca_selecionada


    def mostrar_livro(self):
        return self.listar('titulo', self.livro)
    

    def emprestimo(self):
        #Faz um for para pegar o livro selecionado no arquivo csv, todos em lowercase e sem acento
        for x in self.csv_aquivo():
            for livro in self.mostrar_livro():
                if livro == {unicodedata.normalize(
                'NFD', chave.lower()).encode(
                    'ascii', 'ignore').decode('utf-8'):unicodedata.normalize(
                        'NFD', valor.lower()).encode(
                            'ascii', 'ignore').decode(
                                'utf-8') for chave, valor in x.items()}:
                                
                                #Cria uma nova lista de dicionarios com os dados alterados após o emprestimo
                                novo_arq = []
                                with open('livros.csv') as arq:
                                    csv = DictReader(arq)
                                    for linha in csv:
                                        if linha == x:
                                            quantidade_n = int(linha['Quantidade'])
                                            quantidade_n -= 1
                                            linha.update({'Quantidade': quantidade_n})
                                        novo_arq.append(linha)
                                
                                #Sobreescreve o csv atual com a nova lista criada anteriormente
                                with open('livros.csv', 'w') as arq:
                                    header = [
                                        'Título',
                                        'Autor',
                                        'Data de Lançamento',
                                        'Gênero',
                                        'Quantidade'
                                        ]
                                    csv = DictWriter(arq, fieldnames=header)
                                    csv.writeheader()
                                    for n in novo_arq:
                                        csv.writerow(
                                            {'Título': n['Título'],
                                            'Autor': n['Autor'],
                                            'Data de Lançamento': n['Data de Lançamento'],
                                            'Gênero': n['Gênero'],
                                            'Quantidade': n['Quantidade']}
                                        )

        #Faz um for para pegar a biblioteca selecionada no arquivo csv, todos em lowercase e sem acento
        for x in self.csv_biblioteca():
            for livro in self.mostrar_biblioteca():
                if livro == {unicodedata.normalize(
                'NFD', chave.lower()).encode(
                    'ascii', 'ignore').decode('utf-8'):unicodedata.normalize(
                        'NFD', valor.lower()).encode(
                            'ascii', 'ignore').decode(
                                'utf-8') for chave, valor in x.items()}:

                                #Cria uma nova lista de dicionarios com os dados alterados após o emprestimo
                                novo_arq = []
                                with open('bibliotecas.csv') as arq:
                                    csv = DictReader(arq)
                                    for linha in csv:
                                        if linha == x:
                                            quantidade_n = int(linha['Quantidade de Catálogos'])
                                            quantidade_n -= 1
                                            linha.update({'Quantidade de Catálogos': quantidade_n})
                                        novo_arq.append(linha)
                                
                                #Sobreescreve o csv atual com a nova lista criada anteriormente
                                with open('bibliotecas.csv', 'w') as arq:
                                    header = [
                                        'Nome da Biblioteca',
                                        'Endereço',
                                        'Número',
                                        'Quantidade de Catálogos'
                                        ]
                                    csv = DictWriter(arq, fieldnames=header)
                                    csv.writeheader()
                                    for n in novo_arq:
                                        csv.writerow(
                                            {'Nome da Biblioteca': n['Nome da Biblioteca'],
                                            'Endereço': n['Endereço'],
                                            'Número': n['Número'],
                                            'Quantidade de Catálogos': n['Quantidade de Catálogos']}
                                        )

        return 'Emprestimo feito com sucesso'
        

eu = Emprestimo('Biblioteca Técnica de Iguatu', 'gabriel', '1984')
eu.cadastrar_usuario('23.2333-09', 'rua 123', '08/092004', 'masculino')
print(eu.emprestimo())

