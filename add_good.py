from PyQt5 import QtWidgets


class AddGood(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавление товара")
        self.setGeometry(0, 0, 400, 400)
        formLayout = QtWidgets.QFormLayout()
        gridLayout = QtWidgets.QGridLayout()

        self.nameGoodLabel = QtWidgets.QLabel("Наименование", self)
        self.nameGoodLineEdit = QtWidgets.QLineEdit(self)

        self.quantityGoodLabel = QtWidgets.QLabel("Количество", self)
        self.quantityGoodLineEdit = QtWidgets.QLineEdit(self)

        formLayout.addRow(self.nameGoodLabel, self.nameGoodLineEdit)
        formLayout.addRow(self.quantityGoodLabel, self.quantityGoodLineEdit)
        gridLayout.addLayout(formLayout, 0, 0)

        self.priceBox = QtWidgets.QGroupBox("Цены", self)

        self.buyPriceGoodLabel = QtWidgets.QLabel("Закупочная цена", self)
        self.buyPriceGoodLineEdit = QtWidgets.QLineEdit(self)

        self.salePriceGoodLabel = QtWidgets.QLabel("Розничная цена", self)
        self.salePriceGoodLineEdit = QtWidgets.QLineEdit(self)

        self.priceLayout = QtWidgets.QVBoxLayout()
        self.priceLayout.addWidget(self.buyPriceGoodLabel)
        self.priceLayout.addWidget(self.buyPriceGoodLineEdit)
        self.priceLayout.addWidget(self.salePriceGoodLabel)
        self.priceLayout.addWidget(self.salePriceGoodLineEdit)
        self.priceBox.setLayout(self.priceLayout)
        gridLayout.addWidget(self.priceBox, 1, 0)

        self.typeBox = QtWidgets.QGroupBox("Тип товара")
        self.typeButton0 = QtWidgets.QRadioButton("Игрушка")
        self.typeButton1 = QtWidgets.QRadioButton("Одежда")
        self.typeButton2 = QtWidgets.QRadioButton("Обувь")

        self.typeLayout = QtWidgets.QVBoxLayout()
        self.typeLayout.addWidget(self.typeButton0)
        self.typeLayout.addWidget(self.typeButton1)
        self.typeLayout.addWidget(self.typeButton2)
        self.typeBox.setLayout(self.typeLayout)
        gridLayout.addWidget(self.typeBox, 2, 0)

        self.modificationBox = QtWidgets.QGroupBox("Модификация")
        self.modificationButton0 = QtWidgets.QRadioButton("Обычный товар")
        self.modificationButton1 = QtWidgets.QRadioButton("Комплект")
        self.modificationButton2 = QtWidgets.QRadioButton("Набор")

        self.modificationLayout = QtWidgets.QVBoxLayout()
        self.modificationLayout.addWidget(self.modificationButton0)
        self.modificationLayout.addWidget(self.modificationButton1)
        self.modificationLayout.addWidget(self.modificationButton2)
        self.modificationBox.setLayout(self.modificationLayout)
        gridLayout.addWidget(self.modificationBox, 3, 0)

        # button clear

        self.okButton = QtWidgets.QPushButton("Сохранить", self)
        self.okButton.clicked.connect(self.save)

        gridLayout.addWidget(self.okButton, 4, 0)
        gridLayout.setColumnMinimumWidth(0, 200)
        self.setLayout(gridLayout)

    def save(self):
        print(self.nameGoodLineEdit.text())
