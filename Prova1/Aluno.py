from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf = None, matricula = None):
        super().__init__(nome, cpf)
        self.__matricula = 0
        
    def set_matricula(self, valor):
        if self.__matricula == 0:
            self.__matricula = valor
        else:
            return f"Matricula já cadastrada"

    def get_matricula(self):
        return print ("\nMatricula: " + str(self.__matricula))
        
    def __str__(self):
        return super().__str__() + "\nMatricula: " + str(self.__matricula)
    
    def marcarPresenca(self):
        return super().marcarPresenca()