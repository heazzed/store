from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from Pages.add_good import AddGood
from Pages.search_goods import Goods
from Tools.menu import MenuBar


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, size):
        super().__init__()

        self.title = "Главное окно"
        self.setWindowTitle(self.title)
        # self.frameGeometry().moveCenter(size)

        # self.selectActionLabel = QtWidgets.QLabel("Выберите действие", self)
        # self.addGoodButton = QtWidgets.QPushButton("Добавить товар", self)
        # self.goodsButton = QtWidgets.QPushButton("Поиск товаров", self)
        # self.ordersButton = QtWidgets.QPushButton("Список заказов", self)
        # self.selectActionLabel.setAlignment(QtCore.Qt.AlignCenter)

        # self.add_good_window = AddGood(size)
        # self.goods_window = Goods(size)

        # self.menuBar()
        mb = self.menuBar()
        mb.setNativeMenuBar(False)
        fileMenu = mb.addMenu("File")
        fileMenu.addAction("tr")
        self.setMenuBar(mb)

        # self.statusBar()

        # mainLayout = self.layout()
        #
        # mainLayout.addWidget(self.selectActionLabel)
        # mainLayout.addWidget(self.addGoodButton)
        # mainLayout.addWidget(self.goodsButton)
        # mainLayout.addWidget(self.ordersButton)
        #
        # self.addGoodButton.clicked.connect(self.add_good_window.show)
        # self.goodsButton.clicked.connect(self.goods_window.show)

        # w = QtWidgets.QWidget()
        # w.setLayout(mainLayout)
        # self.create_menu_bar()

        self.setMinimumSize(350, 125)
        #self.init_window()

    def init_window(self):
        mainMenu = self.menuBar()
        mainMenu.addMenu("File")
        mainMenu.addMenu("File")
        mainMenu.addMenu("File")
        mainMenu.addMenu("File")
        mainMenu.addMenu("File")
        self.setMenuBar(mainMenu)
        self.setWindowTitle(self.title)
        self.setGeometry(500, 500, 500, 500)
        self.show()