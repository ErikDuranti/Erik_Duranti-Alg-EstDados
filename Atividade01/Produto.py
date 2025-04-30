from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacoes(self):
        return {
            "Modelo": self.modelo,
            "\nCor": self.cor,
            "\nPreço": self.preco,
            "\nCategoria": self.categoria
        }

    @abstractmethod
    def cadastrar(self):
        pass