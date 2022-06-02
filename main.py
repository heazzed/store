from PyQt5 import QtWidgets
from Pages.main_window import MainWindow


app = QtWidgets.QApplication([])

desktop = app.desktop().availableGeometry().center()

main_window = MainWindow(desktop)
main_window.show()

app.exec_()
