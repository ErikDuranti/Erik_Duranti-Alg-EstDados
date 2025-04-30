from Produto import Produto

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempo_de_bateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempo_de_bateria = tempo_de_bateria

    def getInformacoes(self):
        informacoes = super().getInformacoes()
        informacoes["tempo_de_bateria"] = self.__tempo_de_bateria
        return informacoes

    def get_tempo_de_bateria(self):
        return self.__tempo_de_bateria

    def set_tempo_de_bateria(self, tempo_de_bateria):
        self.__tempo_de_bateria = tempo_de_bateria

    def cadastrar(self):
        pass