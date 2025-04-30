from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from Categoria import Categoria  # Importação da classe Categoria

class TelaCategoria(QDialog):
    def __init__(self, titulo, categorias):
        super().__init__()
        self.setWindowTitle(titulo)
        self.categorias = categorias

        layout = QVBoxLayout()

        self.labelNome = QLabel("Nome da Categoria:")
        self.inputNome = QLineEdit()
        self.btnSalvar = QPushButton("Salvar")
        self.btnSalvar.clicked.connect(self.salvarCategoria)

        layout.addWidget(self.labelNome)
        layout.addWidget(self.inputNome)
        layout.addWidget(self.btnSalvar)

        self.setLayout(layout)

    def salvarCategoria(self):
        nome = self.inputNome.text()
        if nome:
            nova_categoria = Categoria(len(self.categorias) + 1, nome)
            self.categorias.append(nova_categoria)
            QMessageBox.information(self, "Sucesso", f"Categoria '{nome}' adicionada!")
            self.inputNome.clear()
        else:
            QMessageBox.warning(self, "Erro", "O nome da categoria não pode estar vazio!")