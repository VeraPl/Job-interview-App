from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5 import uic
from PyQt5 import QtCore
from Question import GenerateQuestions


class NumberOfQuestions(QDialog):

    def __init__(self, quest):
        super(NumberOfQuestions, self).__init__()
        form, _ = uic.loadUiType('dlg_num.ui')
        self.ui = form()
        self.ui.setupUi(self)
        self.setWindowTitle("Choose the number of questions")
        self.res = None
        self.quest = quest

        self.ui.btn_ok.clicked.connect(self.close_win)

    def close_win(self):
        self.res = (self.ui.cb.currentText())
        self.close()
        self.gen = GenerateQuestions(self.res, self.quest)
        self.gen.show()