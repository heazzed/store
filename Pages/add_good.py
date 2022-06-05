from PyQt5 import QtWidgets
from Entities.good import Good
from Repositories.good_repository import GoodRepository


class AddGood(QtWidgets.QDialog):
    def __init__(self, size):
        super().__init__()

        self.setWindowTitle("Добавление товара")

        self.frameGeometry().moveCenter(size)

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

        self.genderBox = QtWidgets.QGroupBox("Пол")
        self.genderCheckBox0 = QtWidgets.QCheckBox("Для девочек")
        self.genderCheckBox1 = QtWidgets.QCheckBox("Для мальчиков")

        self.genderLayout = QtWidgets.QVBoxLayout()
        self.genderLayout.addWidget(self.genderCheckBox0)
        self.genderLayout.addWidget(self.genderCheckBox1)
        self.genderBox.setLayout(self.genderLayout)
        gridLayout.addWidget(self.genderBox, 3, 0)

        self.listTypeRadioButtons = [self.typeButton0, self.typeButton1, self.typeButton2]
        self.listGenderCheckBoxButtons = [self.genderCheckBox0, self.genderCheckBox1]
        self.listButtons = []
        for btn in self.listTypeRadioButtons:
            self.listButtons.append(btn)
        for btn in self.listGenderCheckBoxButtons:
            self.listButtons.append(btn)

        self.clearButton = QtWidgets.QPushButton("Очистить", self)
        self.clearButton.clicked.connect(self.clear)

        self.okButton = QtWidgets.QPushButton("Сохранить", self)
        self.okButton.clicked.connect(self.save)

        gridLayout.addWidget(self.clearButton, 4, 0)
        gridLayout.addWidget(self.okButton, 5, 0)
        self.setMinimumSize(400, 400)
        self.setLayout(gridLayout)

    def save(self):
        g = Good()
        g.name = self.nameGoodLineEdit.text()
        g.quantity = self.quantityGoodLineEdit.text()
        g.buyPrice = self.buyPriceGoodLineEdit.text()
        g.salePrice = self.salePriceGoodLineEdit.text()
        for btn in self.listTypeRadioButtons:
            if btn.isChecked():
                g.type = btn.text()
        gen = []

        for btn in self.listGenderCheckBoxButtons:
            if btn.isChecked():
                gen.append(btn.text())

        g.gender = gen

        if g.validate() is False:
            print("При сохранении товара возникла ошибка")
            return
        else:
            gr = GoodRepository()
            gr.save(g)

            print("Сохранен товар:")
            g.show()

            gr.show_current_saved_goods()

    def clear(self):
        self.nameGoodLineEdit.clear()
        self.quantityGoodLineEdit.clear()
        self.buyPriceGoodLineEdit.clear()
        self.salePriceGoodLineEdit.clear()
        for btn in self.listButtons:
            if btn.isChecked():
                if isinstance(btn, QtWidgets.QRadioButton):
                    btn.setAutoExclusive(False)
                    btn.setChecked(False)
                    btn.setAutoExclusive(True)
                elif isinstance(btn, QtWidgets.QCheckBox):
                    btn.setChecked(False)

