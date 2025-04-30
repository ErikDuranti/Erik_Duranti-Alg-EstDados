from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from Notebook import Notebook

class TelaNotebook(QDialog):
    def __init__(self, titulo, categorias, produtos):
        super().__init__()
        self.setWindowTitle(titulo)
        self.categorias = categorias
        self.produtos = produtos

        layout = QVBoxLayout()

        self.labelModelo = QLabel("Modelo:")
        self.inputModelo = QLineEdit()

        self.labelCor = QLabel("Cor:")
        self.inputCor = QLineEdit()

        self.labelPreco = QLabel("Preço:")
        self.inputPreco = QLineEdit()

        self.labelCategoria = QLabel("Categoria:")
        self.comboCategoria = QComboBox()
        self.comboCategoria.addItems([categoria.nome for categoria in categorias])

        self.labelBateria = QLabel("Tempo de Bateria (horas):")
        self.inputBateria = QLineEdit()

        self.btnSalvar = QPushButton("Salvar")
        self.btnSalvar.clicked.connect(self.salvarNotebook)

        layout.addWidget(self.labelModelo)
        layout.addWidget(self.inputModelo)
        layout.addWidget(self.labelCor)
        layout.addWidget(self.inputCor)
        layout.addWidget(self.labelPreco)
        layout.addWidget(self.inputPreco)
        layout.addWidget(self.labelCategoria)
        layout.addWidget(self.comboCategoria)
        layout.addWidget(self.labelBateria)
        layout.addWidget(self.inputBateria)
        layout.addWidget(self.btnSalvar)

        self.setLayout(layout)

    def salvarNotebook(self):
        modelo = self.inputModelo.text()
        cor = self.inputCor.text()
        preco = self.inputPreco.text()
        categoria_nome = self.comboCategoria.currentText()
        bateria = self.inputBateria.text()

        if modelo and cor and preco and categoria_nome and bateria:
            # Busca a categoria pelo nome
            categoria = next((cat for cat in self.categorias if cat.nome == categoria_nome), None)
            if categoria:
                notebook = Notebook(modelo, cor, float(preco), categoria, bateria)
                self.produtos.append(notebook)
                QMessageBox.information(self, "Sucesso", f"Notebook '{modelo}' cadastrado com sucesso!")
                self.close()
            else:
                QMessageBox.warning(self, "Erro", "Categoria inválida!")
        else:
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos!")