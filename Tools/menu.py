from PyQt5 import QtWidgets


class MenuBar(QtWidgets.QMainWindow):

    def create_menu(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QtWidgets.QMenu("&amp;File", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&amp;Edit")
        helpMenu = menuBar.addMenu("&amp;Help")
        return menuBar