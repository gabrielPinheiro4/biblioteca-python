from biblioteca import Biblioteca 
from usuario import Usuario
from livro import Livro
from csv import *
from utils.funcoes import (
    csv_biblioteca,
    meu_normalize,
    csv_aquivo,
    )
 
from constants.biblioteca_const import CABECALHO_BIBLIOTECA
from constants.livro_const import CABECALHO

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


    #Realiza o cadastro do usuário    
    def cadastrar_usuario(self,nome_completo, cpf,endereco, data_nascimento, genero_preferido):
        super().__init__(nome_completo, cpf,endereco, data_nascimento, genero_preferido)
        
    #Retorna os dados do usuário
    def mostra_usuario(self):
        return (
            f'Nome: {self.nome}\n'
            f'Usuário: {self.usuario}\n'
            f'CPF: {self.cpf}\n'
            f'Endereço: {self.endereco}\n'
            f'Data de Nascimento: {self.data_nascimento}\n'
            f'Matricula: {self.matricula}, Data da Matricula: {self.data_matricula}\n'
            f'Gênero: {self.genero}'
        )
        
    
    #Retorna os dados da biblioteca selecionada
    def mostrar_biblioteca(self):
        #Cria uma nova lista de dicionarios em lowercase e sem acentuação do arquivo bibliotecas.csv
        nova_lista_biblioteca = []
        for biblioteca in csv_biblioteca():
            nova_lista_biblioteca.append(
                {meu_normalize(chave.lower()): 
                 meu_normalize(valor.lower()) for chave, valor in biblioteca.items()})
        
        ##Criar uma lista filtrando os elementos de acordo com a pesquisa do usuario
        biblioteca_selecionada = list(
            filter(
                lambda x: 
                meu_normalize(self.biblioteca.lower()) in x['nome da biblioteca'], nova_lista_biblioteca
            )
        )

        return biblioteca_selecionada


    #Retorna os dados do livro selecionado
    def mostrar_livro(self):
        return self.listar('titulo', self.livro)
    

    #Método para realizar emprestimo
    def emprestimo(self):
        #Faz um for para pegar o livro selecionado no arquivo csv, todos em lowercase e sem acento
        for x in csv_aquivo():
            for livro in self.mostrar_livro():

                if livro == {
                     meu_normalize(chave.lower()):
                     meu_normalize(valor.lower()) for chave, valor in x.items()}:
                                
                    #Cria uma nova lista de dicionarios com os dados alterados após o emprestimo
                    novo_arq = []
                    with open('livros.csv') as arq:
                        csv = DictReader(arq)
                        for linha in csv:
                            if linha == x:
                                quantidade_n = int(linha.get('Quantidade'))
                                quantidade_n -= 1
                                linha.update({'Quantidade': quantidade_n})
                            novo_arq.append(linha)
                    
                    #Sobreescreve o csv atual com a nova lista criada anteriormente
                    with open('livros.csv', 'w') as arq:
                        csv = DictWriter(arq, fieldnames=CABECALHO)
                        csv.writeheader()
                        for n in novo_arq:
                            csv.writerow(
                                {'Título': n.get('Título'),
                                'Autor': n.get('Autor'),
                                'Data de Lançamento': n.get('Data de Lançamento'),
                                'Gênero': n.get('Gênero'),
                                'Quantidade': n.get('Quantidade')}
                            )

        #Faz um for para pegar a biblioteca selecionada no arquivo csv, todos em lowercase e sem acento
        for x in csv_biblioteca():
            for livro in self.mostrar_biblioteca():
                if livro == {
                     meu_normalize(chave.lower()):
                     meu_normalize(valor.lower()) for chave, valor in x.items()}:

                    #Cria uma nova lista de dicionarios com os dados alterados após o emprestimo
                    novo_arq = []
                    with open('bibliotecas.csv') as arq:
                        csv = DictReader(arq)
                        for linha in csv:
                            if linha == x:
                                quantidade_n = int(linha.get('Quantidade de Catálogos'))
                                quantidade_n -= 1
                                linha.update({'Quantidade de Catálogos': quantidade_n})
                            novo_arq.append(linha)
                    
                    #Sobreescreve o csv atual com a nova lista criada anteriormente
                    with open('bibliotecas.csv', 'w') as arq:
                        csv = DictWriter(arq, fieldnames=CABECALHO_BIBLIOTECA)
                        csv.writeheader()
                        for n in novo_arq:
                            csv.writerow(
                                {'Nome da Biblioteca': n.get('Nome da Biblioteca'),
                                'Endereço': n.get('Endereço'),
                                'Número': n.get('Número'),
                                'Quantidade de Catálogos': n.get('Quantidade de Catálogos')}
                            )

        return 'Emprestimo feito com sucesso'
    

    #Faz a mesma coisa que o metodo 'emprestimo' mas adiciona 1 ao inves de remover
    def devolver_emprestimo(self):
        #Faz um for para pegar o livro selecionado no arquivo csv, todos em lowercase e sem acento
        for x in csv_aquivo():
            for livro in self.mostrar_livro():
                if livro == {
                     meu_normalize(chave.lower()):
                     meu_normalize(valor.lower()) for chave, valor in x.items()}:
                                
                    #Cria uma nova lista de dicionarios com os dados alterados após o emprestimo
                    novo_arq = []
                    with open('livros.csv') as arq:
                        csv = DictReader(arq)
                        for linha in csv:
                            if linha == x:
                                quantidade_n = int(linha.get('Quantidade'))
                                quantidade_n += 1
                                linha.update({'Quantidade': quantidade_n})
                            novo_arq.append(linha)
                    
                    #Sobreescreve o csv atual com a nova lista criada anteriormente
                    with open('livros.csv', 'w') as arq:
                        csv = DictWriter(arq, fieldnames=CABECALHO)
                        csv.writeheader()
                        for n in novo_arq:
                            csv.writerow(
                                {'Título': n.get('Título'),
                                'Autor': n.get('Autor'),
                                'Data de Lançamento': n.get('Data de Lançamento'),
                                'Gênero': n.get('Gênero'),
                                'Quantidade': n.get('Quantidade')}
                            )

        #Faz um for para pegar a biblioteca selecionada no arquivo csv, todos em lowercase e sem acento
        for x in csv_biblioteca():
            for livro in self.mostrar_biblioteca():
                if livro == {
                     meu_normalize(chave.lower()):
                     meu_normalize(valor.lower()) for chave, valor in x.items()}:

                    #Cria uma nova lista de dicionarios com os dados alterados após o emprestimo
                    novo_arq = []
                    with open('bibliotecas.csv') as arq:
                        csv = DictReader(arq)
                        for linha in csv:
                            if linha == x:
                                quantidade_n = int(linha.get('Quantidade de Catálogos'))
                                quantidade_n += 1
                                linha.update({'Quantidade de Catálogos': quantidade_n})
                            novo_arq.append(linha)
                    
                    #Sobreescreve o csv atual com a nova lista criada anteriormente
                    with open('bibliotecas.csv', 'w') as arq:
                        csv = DictWriter(arq, fieldnames=CABECALHO_BIBLIOTECA)
                        csv.writeheader()
                        for n in novo_arq:
                            csv.writerow(
                                {'Nome da Biblioteca': n.get('Nome da Biblioteca'),
                                'Endereço': n.get('Endereço'),
                                'Número': n.get('Número'),
                                'Quantidade de Catálogos': n.get('Quantidade de Catálogos')}
                            )

        return 'Emprestimo devolvido com sucesso'
        

eu = Emprestimo('Biblioteca Técnica de Iguatu', 'tico e teco', '1984')
eu.cadastrar_usuario('gabriel', '23.2333-09', 'rua 123', '08/092004', 'masculino')
print(eu.emprestimo())
