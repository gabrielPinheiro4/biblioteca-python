from biblioteca import (
    Biblioteca, 
    biblioteca1,
    biblioteca2,
    biblioteca3,
    biblioteca4
    )

from usuario import Usuario
from livro import Livro
from csv import *
from utils.funcoes import (
    meu_normalize,
    escrita_livro,
    escrita_biblioteca,
    ler_arquivo
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
    
    # Realiza o cadastro do usuário    
    def cadastrar_usuario(self,nome_completo, cpf,endereco, data_nascimento, genero_preferido):
        super().__init__(nome_completo, cpf,endereco, data_nascimento, genero_preferido)
        
    # Retorna os dados do livro selecionado
    def mostrar_livro(self):
        return self.listar('titulo', self.livro)
    
    # Método para realizar emprestimo
    def emprestimo(self):

        # Faz um for para pegar o livro selecionado no arquivo livros.csv
        for x in ler_arquivo('livros.csv'):
            for livro in self.mostrar_livro():

                # Se o livro selecionado for igual ao livro em livro.csv
                if livro == {
                     meu_normalize(chave.lower()):
                     meu_normalize(valor.lower()) for chave, valor in x.items()}:
                                
                    # Cria uma nova lista
                    novo_arq = []

                    with open('livros.csv') as arq:
                        csv = DictReader(arq)
                        for linha in csv:

                            # Diminui a quantidade de livro
                            if linha == x:
                                quantidade_n = int(linha.get('Quantidade'))
                                quantidade_n -= 1
                                linha.update({'Quantidade': quantidade_n})

                            # Adiciona os dados alterados na lista criada anteriormente
                            novo_arq.append(linha)
                    
                    # Escreve os dados da lista no arquivo csv
                    escrita_livro(novo_arq, CABECALHO)
        
        for x in ler_arquivo('bibliotecas.csv'):
            if self.biblioteca.nome in x.get('Nome da Biblioteca'):

                novo_arq = []

                with open('bibliotecas.csv') as arq:
                    csv = DictReader(arq)

                    for linha in csv:
                        if linha == x:
                            quantidade_n = int(linha.get('Quantidade de Catálogos'))
                            quantidade_n -= 1
                            linha.update({'Quantidade de Catálogos': quantidade_n})
                        novo_arq.append(linha)
                escrita_biblioteca(novo_arq, CABECALHO_BIBLIOTECA)

        return 'Emprestimo feito com sucesso'
    
    def devolver_emprestimo(self):
        for x in ler_arquivo('livros.csv'):
            for livro in self.mostrar_livro():
                if livro == {
                     meu_normalize(chave.lower()):
                     meu_normalize(valor.lower()) for chave, valor in x.items()}:
                    novo_arq = []
                    with open('livros.csv') as arq:
                        csv = DictReader(arq)
                        for linha in csv:
                            if linha == x:
                                quantidade_n = int(linha.get('Quantidade'))
                                quantidade_n += 1
                                linha.update({'Quantidade': quantidade_n})
                            novo_arq.append(linha)
                    
                    escrita_livro(novo_arq, CABECALHO)

        for x in ler_arquivo('bibliotecas.csv'):
            if self.biblioteca.nome in x.get('Nome da Biblioteca'):
                novo_arq = []

                with open('bibliotecas.csv') as arq:
                    csv = DictReader(arq)
                    for linha in csv:
                        if linha == x:
                            quantidade_n = int(linha.get('Quantidade de Catálogos'))
                            quantidade_n += 1
                            linha.update({'Quantidade de Catálogos': quantidade_n})
                        novo_arq.append(linha)
                
                escrita_biblioteca(novo_arq, CABECALHO_BIBLIOTECA)

        return 'Emprestimo devolvido com sucesso'
    
    
eu = Emprestimo(biblioteca1, 'gPinheiro', '1984')
eu.cadastrar_usuario('gabriel', '23.2333-09', 'rua 123', '08/092004', 'masculino')
print(eu.emprestimo())
