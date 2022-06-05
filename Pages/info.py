from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class InfoPage(QtWidgets.QDialog):
    def __init__(self, size):
        super().__init__()

        self.setWindowTitle("О программе")
        self.frameGeometry().moveCenter(size)
        self.setMinimumSize(260, 80)

        self.infoLabel = QtWidgets.QLabel("\n"
                                          "Проект разработал студент гр.БИС191\n"
                                          "Милисов Максим\n"
                                          "'PyStore', v. 1.0", self)
        self.infoLabel.setFont(QFont("Times", 10, QFont.Bold))
        self.infoLabel.setAlignment(Qt.AlignCenter)

