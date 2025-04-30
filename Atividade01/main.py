import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QMessageBox

from TelaCategoria import TelaCategoria
from TelaDesktop import TelaDesktop
from TelaNotebook import TelaNotebook

class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Principal")
        self.setGeometry(100, 100, 900, 200)

        self.categorias = []
        self.produtos = []

        layout = QVBoxLayout()

        self.btnCategoria = QPushButton("Cadastrar Categoria")
        self.btnCategoria.clicked.connect(self.abrirTelaCategoria)

        self.btnDesktop = QPushButton("Cadastrar Desktop")
        self.btnDesktop.clicked.connect(self.abrirTelaDesktop)

        self.btnNotebook = QPushButton("Cadastrar Notebook")
        self.btnNotebook.clicked.connect(self.abrirTelaNotebook)

        self.btnConsultar = QPushButton("Consultar Itens")
        self.btnConsultar.clicked.connect(self.consultarItens)

        self.btnAlterar = QPushButton("Alterar Item")
        self.btnAlterar.clicked.connect(self.alterarItem)

        self.btnDeletar = QPushButton("Deletar Item")
        self.btnDeletar.clicked.connect(self.deletarItem)

        self.btnEstoque = QPushButton("Consultar Estoque")
        self.btnEstoque.clicked.connect(self.consultarEstoque)

        layout.addWidget(self.btnCategoria)
        layout.addWidget(self.btnDesktop)
        layout.addWidget(self.btnNotebook)
        layout.addWidget(self.btnConsultar)
        layout.addWidget(self.btnAlterar)
        layout.addWidget(self.btnDeletar)
        layout.addWidget(self.btnEstoque)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrirTelaCategoria(self):
        telaCategoria = TelaCategoria("Cadastro de Categorias", self.categorias)
        telaCategoria.exec_()

    def abrirTelaDesktop(self):
        if not self.categorias:
            self.mostrarMensagemErro("Nenhuma categoria cadastrada. Cadastre uma categoria primeiro.")
            return
        telaDesktop = TelaDesktop("Cadastro de Desktop", self.categorias, self.produtos)
        telaDesktop.exec_()

    def abrirTelaNotebook(self):
        if not self.categorias:
            self.mostrarMensagemErro("Nenhuma categoria cadastrada. Cadastre uma categoria primeiro.")
            return
        telaNotebook = TelaNotebook("Cadastro de Notebook", self.categorias, self.produtos)
        telaNotebook.exec_()

    def consultarItens(self):
        if not self.produtos:
            self.mostrarMensagemErro("Nenhum item cadastrado.")
            return
        itens = "\n".join([str(produto.getInformacoes()) for produto in self.produtos])
        QMessageBox.information(self, "Itens Cadastrados", itens)

    def alterarItem(self):
        #AINDA NÃO FEITO, Falta implementar lógica para alterar um item cadastrado (Foi preguiça sor, vai ser implementado mais pra frente kkkkk)
        QMessageBox.information(self, "Alterar Item", "Funcionalidade de alteração ainda não implementada.")

    def deletarItem(self):
        #AINDA NÃO FEITO, Falta implementar lógica para deletar um item cadastrado (Foi preguiça sor, vai ser implementado mais pra frente kkkkk)
        QMessageBox.information(self, "Deletar Item", "Funcionalidade de exclusão ainda não implementada.")

    def consultarEstoque(self):
        #AINDA NÃO FEITO, Falta implementar lógica para deletar um item cadastrado (Foi preguiça sor, vai ser implementado mais pra frente kkkkk)
        QMessageBox.information(self, "Consultar Estoque", "Funcionalidade de consulta disponível em estoque ainda não implementada.")

    def mostrarMensagemErro(self, mensagem):
        QMessageBox.warning(self, "Erro", mensagem)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    telaPrincipal = TelaPrincipal()
    telaPrincipal.show()
    sys.exit(app.exec_())