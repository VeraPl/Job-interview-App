import sys
import csv

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

from Numbers import NumberOfQuestions




class Application(QMainWindow):

    def __init__(self):
        super(Application, self).__init__()
        form, _ = uic.loadUiType('main.ui')
        self.ui = form()
        self.ui.setupUi(self)
        self.setWindowTitle("Job Interview")
        self.quest = None

        self.btn_algorithms = self.ui.btn_algorithms
        self.btn_git = self.ui.btn_git
        self.btn_linux = self.ui.btn_linux
        self.btn_mix = self.ui.btn_mix
        self.btn_prac = self.ui.btn_prac
        self.btn_py = self.ui.btn_py
        self.btn_sql = self.ui.btn_sql

        self.btn_algorithms.clicked.connect(self.algorithms)
        self.btn_git.clicked.connect(self.git)
        self.btn_linux.clicked.connect(self.linux)
        self.btn_mix.clicked.connect(self.mix)
        self.btn_prac.clicked.connect(self.prac)
        self.btn_py.clicked.connect(self.py)
        self.btn_sql.clicked.connect(self.sql)

    def algorithms(self):
        self.quest = "algorithms"
        self.get_num()

    def git(self):
        self.quest = "git"
        self.get_num()

    def linux(self):
        self.quest = "linux"
        self.get_num()

    def mix(self):
        self.quest =  "mix"
        self.get_num()

    def prac(self):
        self.quest = "prac"
        self.get_num()

    def py(self):
        self.quest = "python.csv"
        self.get_num()

    def sql(self):
        self.quest = "sql"
        self.get_num()

    def get_num(self):
        self.num = NumberOfQuestions(self.quest)
        self.num.show()





app = QApplication(sys.argv)
wid = Application()
wid.show()
sys.exit(app.exec_())
