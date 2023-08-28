import csv
import random

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class GenerateQuestions(QWidget):

    def __init__(self, res, quest):
        super(GenerateQuestions, self).__init__()
        form, _ = uic.loadUiType('quest.ui')
        self.ui = form()
        self.ui.setupUi(self)
        self.setWindowTitle("Answer the question")

        self.res = int(res)
        self.quest = quest
        self.ind = 0

        self.ui.btn_cancel.clicked.connect(self.close_win)
        self.ui.btn_next.clicked.connect(self.next)
        self.ui.btn_info.clicked.connect(self.show_answer)
        self.ui.info.hide()

        with open(quest, encoding="utf-8") as f:
            self.questions = tuple(csv.DictReader(f, delimiter=","))
            self.indexes = random.sample(list(range(0, len(list(self.questions)))), self.res)
        self.ui.label.setText(self.questions[self.indexes[0]]["Question"])
        self.ui.progressBar.setValue(int((self.ind + 1) / self.res * 100))

    def next(self):
        if len(self.indexes) - 1 > self.ind:
            self.ind += 1
            self.ui.label.setText(self.questions[self.indexes[self.ind]]["Question"])
            self.ui.progressBar.setValue(int((self.ind + 1) / self.res * 100))


    def show_answer(self):
        pass
        self.ui.info.show()
        self.ui.info.setText(self.questions[self.indexes[self.ind]]["info"])

    def close_win(self):
        self.close()
