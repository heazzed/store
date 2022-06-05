from PyQt5 import QtWidgets
from Pages.add_good import AddGood
from Pages.search_goods import SearchGoods
from Tools.menu import MenuBar
from Database.db import Database


class MainWindow(QtWidgets.QDialog):
    def __init__(self, size):
        super().__init__()

        self.db = Database()
        self.db.connect()

        self.title = "Главное окно"
        self.setWindowTitle(self.title)
        self.frameGeometry().moveCenter(size)
        self.setMinimumSize(350, 125)

        self.selectActionLabel = QtWidgets.QLabel("Выберите действие:", self)
        self.addGoodButton = QtWidgets.QPushButton("Добавить товар", self)
        self.goodsButton = QtWidgets.QPushButton("Поиск товаров", self)
        self.ordersButton = QtWidgets.QPushButton("Список заказов", self)

        self.add_good_window = AddGood(size, self.db)
        self.search_goods_window = SearchGoods(size, self.db)

        self.menuBar = MenuBar(size, self.db)
        mb = self.menuBar.get_menu_bar()

        mainLayout = QtWidgets.QGridLayout()

        mainLayout.addWidget(self.selectActionLabel, 0, 1)
        mainLayout.addWidget(self.addGoodButton, 1, 0)
        mainLayout.addWidget(self.goodsButton, 1, 1)
        mainLayout.addWidget(self.ordersButton, 1, 2)

        mainLayout.setMenuBar(mb)

        self.addGoodButton.clicked.connect(self.add_good_window.show)
        self.goodsButton.clicked.connect(self.search_goods_window.show)

        self.setLayout(mainLayout)

