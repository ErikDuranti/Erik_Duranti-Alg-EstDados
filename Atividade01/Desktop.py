from Produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potencia_da_fonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potencia_da_fonte

    def getInformacoes(self):
        return {
            "Modelo": self.modelo,
            "\nCor": self.cor,
            "\nPreço": self.preco,
            "\nCategoria": self.categoria.nome,
            "\nPotência da Fonte": self._potenciaDaFonte
        }

    def get_potencia_da_fonte(self):
        return self._potenciaDaFonte

    def set_potencia_da_fonte(self, potencia_da_fonte):
        self._potenciaDaFonte = potencia_da_fonte

    def cadastrar(self):
        pass