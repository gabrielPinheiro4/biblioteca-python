class Pessoa:
    def __init__(self, nome_completo, cpf, endereco, data_nascimento):
        self.__nome_completo = nome_completo
        self.__cpf = cpf
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        

    @property
    def nome(self):
        return self.__nome_completo
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento