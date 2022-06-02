from PyQt5 import QtWidgets
from Pages.add_good import AddGood
from Pages.goods import Goods


class MainWindow(QtWidgets.QDialog):
    def __init__(self, size):
        super().__init__()

        self.setWindowTitle("Главное окно")
        self.frameGeometry().moveCenter(size)

        self.selectActionLabel = QtWidgets.QLabel("Выберите действие", self)
        self.addGoodButton = QtWidgets.QPushButton("Добавить товар", self)
        self.goodsButton = QtWidgets.QPushButton("Товары", self)
        self.ordersButton = QtWidgets.QPushButton("Список заказов", self)

        self.add_good_window = AddGood(size)
        self.goods_window = Goods(size)

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(self.selectActionLabel, 0, 1)
        gridLayout.addWidget(self.addGoodButton, 1, 0)
        gridLayout.addWidget(self.goodsButton, 1, 1)
        gridLayout.addWidget(self.ordersButton, 1, 2)

        self.addGoodButton.clicked.connect(self.add_good_window.show)
        self.goodsButton.clicked.connect(self.goods_window.show)

        self.setMinimumSize(350, 125)
        self.setLayout(gridLayout)
