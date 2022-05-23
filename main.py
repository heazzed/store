from PyQt5 import QtWidgets

from add_good import AddGood

app = QtWidgets.QApplication([])

window = AddGood()
window.show()

app.exec_()
