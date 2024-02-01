from pessoa import Pessoa
import uuid
import datetime

class Usuario(Pessoa):
    def __init__(self, 
                 nome_completo, 
                 cpf, 
                 endereco, 
                 data_nascimento,
                 genero_preferido
                 ):
        super().__init__(nome_completo, cpf, endereco, data_nascimento)
        self.__matricula = str(uuid.uuid4()).split('-')[0]
        self.__data_matriula = datetime.date.today()
        self.__genero_preferido = genero_preferido

    
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def data_matricula(self):
        return self.__data_matriula
    
    @property
    def genero(self):
        return self.__genero_preferido
    

    def mostra_usuario(self):
        return (
            f'Nome: {self.nome}\n'
            f'CPF: {self.cpf}\n'
            f'Endereço: {self.endereco}\n'
            f'Data de Nascimento: {self.data_nascimento}\n'
            f'Matricula: {self.matricula}, Data da Matricula: {self.data_matricula}\n'
            f'Gênero: {self.genero}'
        )


        