from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf = None):
        self.nome = nome
        self._cpf = cpf

    @abstractmethod
    def marcarPresenca(self):
        pass

    def imprimir(self):
        print(self)

    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + str(self._cpf)