from PyQt5 import QtWidgets
from Pages.info import InfoPage
from Pages.add_good import AddGood
from Pages.search_goods import SearchGoods


class MenuBar(QtWidgets.QMainWindow):
    def __init__(self, size, db):
        super().__init__()

        self.menuBar = QtWidgets.QMenuBar()

        # main menu
        mainMenu = self.menuBar.addMenu("Меню")
        quitAction = mainMenu.addAction("Закрыть программу")
        quitAction.setShortcut('Ctrl+Q')
        quitAction.triggered.connect(QtWidgets.qApp.quit)

        # goods menu
        goodsMenu = self.menuBar.addMenu("Товары")

        self.sg = SearchGoods(size, db)
        searchGoodsAction = goodsMenu.addAction("Поиск товаров")
        searchGoodsAction.setShortcut('Ctrl+F')
        searchGoodsAction.triggered.connect(self.sg.show)

        self.ag = AddGood(size, db)
        addGoodAction = goodsMenu.addAction("Добавить товар")
        addGoodAction.setShortcut('Ctrl+A')
        addGoodAction.triggered.connect(self.ag.show)

        editGoodAction = goodsMenu.addAction("Изменить товар")
        editGoodAction.setShortcut('Ctrl+E')

        editGoodAction = goodsMenu.addAction("Удалить товар")
        editGoodAction.setShortcut('Ctrl+D')

        # orders menu
        ordersMenu = self.menuBar.addMenu("Заказы")

        # info menu
        infoAction = self.menuBar.addAction("О программе")
        self.ip = InfoPage(size)
        infoAction.setShortcut('Ctrl+I')
        infoAction.triggered.connect(self.ip.show)

    def get_menu_bar(self):
        return self.menuBar
