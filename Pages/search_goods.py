from PyQt5 import QtWidgets
from Database.db import Database
from Repositories.good_repository import GoodRepository


class Goods(QtWidgets.QDialog):
    def __init__(self, size):
        super().__init__()

        gr = GoodRepository()

        self.setWindowTitle("Поиск товаров")
        self.db = Database()
        self.db.connect()

        self.frameGeometry().moveCenter(size)
        gridLayout = QtWidgets.QGridLayout()

        self.typeBox = QtWidgets.QGroupBox(self)
        self.typeLayout = QtWidgets.QVBoxLayout()

        self.typeGoodLabel = QtWidgets.QLabel("Тип товара")

        self.typeComboBox = QtWidgets.QComboBox(self)
        self.typeComboBox.addItems(["Все товары", "Игрушка", "Одежда", "Обувь"])

        self.typeLayout.addWidget(self.typeGoodLabel)
        self.typeLayout.addWidget(self.typeComboBox)
        self.typeBox.setLayout(self.typeLayout)
        gridLayout.addWidget(self.typeBox, 0, 0)

        self.availabilityCheckBox = QtWidgets.QCheckBox("Только доступные для заказа товары")
        gridLayout.addWidget(self.availabilityCheckBox, 1, 0)

        self.searchBox = QtWidgets.QGroupBox(self)
        self.searchLayout = QtWidgets.QVBoxLayout()

        self.searchLabel = QtWidgets.QLabel("Поиск", self)
        self.searchLineEdit = QtWidgets.QLineEdit(self)
        self.searchButton = QtWidgets.QPushButton("Найти", self)
        self.searchButton.clicked.connect(self.find)

        self.searchLayout.addWidget(self.searchLabel)
        self.searchLayout.addWidget(self.searchLineEdit)
        self.searchLayout.addWidget(self.searchButton)
        self.searchBox.setLayout(self.searchLayout)
        gridLayout.addWidget(self.searchBox, 2, 0)

        self.resultBox = QtWidgets.QGroupBox(self)
        self.resultLayout = QtWidgets.QVBoxLayout()
        self.resultLabel = QtWidgets.QLabel("Результаты поиска", self)

        self.countResults = gr.get_goods_count(self.db)
        self.resultTable = QtWidgets.QTableWidget(self.countResults, 8)
        self.resultTable.setHorizontalHeaderLabels(["Доступен", "ID", "Название", "Количество", "Закупочная цена",
                                                    "Розничная цена", "Тип товара", "Пол"])
        self.selectResult = gr.get_all_goods(self.db)
        self.query_result_to_table_item(self.selectResult)

        self.resultTable.resizeColumnsToContents()
        self.resultLayout.addWidget(self.resultLabel)
        self.resultLayout.addWidget(self.resultTable)
        self.resultBox.setLayout(self.resultLayout)
        gridLayout.addWidget(self.resultBox, 3, 0)

        self.setLayout(gridLayout)
        self.setMinimumSize(800, 500)

    def query_result_to_table_item(self, query_result):
        i = 0
        for items in query_result:
            j = 0
            for item in items:
                if j == 0:
                    if item == 1:
                        item = "Да"
                    elif item == 0:
                        item = "Нет"
                elif j == 6:
                    if item == 0:
                        item = "Игрушка"
                    elif item == 1:
                        item = "Одежда"
                    elif item == 2:
                        item = "Обувь"
                elif j == 7:
                    if item == 0:
                        item = "Для девочек"
                    elif item == 1:
                        item = "Для мальчиков"
                    elif item == 2:
                        item = "Для мальчиков и для девочек"
                self.resultTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))
                j += 1
            i += 1
