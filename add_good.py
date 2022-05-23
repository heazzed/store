from PyQt5 import QtWidgets


class AddGood(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавление товара")
        self.setGeometry(0, 0, 400, 600)
        formLayout = QtWidgets.QFormLayout()
        gridLayout = QtWidgets.QGridLayout()

        self.nameGoodLabel = QtWidgets.QLabel("Наименование", self)
        self.nameGoodLineEdit = QtWidgets.QLineEdit(self)

        self.quantityGoodLabel = QtWidgets.QLabel("Количество", self)
        self.quantityGoodLineEdit = QtWidgets.QLineEdit(self)

        formLayout.addRow(self.nameGoodLabel, self.nameGoodLineEdit)
        formLayout.addRow(self.quantityGoodLabel, self.quantityGoodLineEdit)
        gridLayout.addLayout(formLayout, 0, 0)

        self.ok_button = QtWidgets.QPushButton("Сохранить", self)
        self.ok_button.clicked.connect(self.save)

        gridLayout.addWidget(self.ok_button, 1, 0)
        gridLayout.setColumnMinimumWidth(0, 500)
        self.setLayout(gridLayout)

    def save(self):
        print(self.nameGoodLineEdit.text())
