from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, 
                 nome_completo, 
                 cpf, 
                 endereco, 
                 data_nascimento,
                 matricula,
                 data_matricula,
                 genero_preferido
                 ):
        super().__init__(nome_completo, cpf, endereco, data_nascimento)
        self.__matricula = matricula
        self.__data_matriula = data_matricula
        self.__genero_preferido = genero_preferido


        