from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore
import time

import progress

g_prog = 0


def outsider(prog):
    global g_prog
    g_prog = prog


class MainUiClass(QtWidgets.QMainWindow, progress.Ui_Form):
    def __init__(self, parent=None):
        super(MainUiClass, self).__init__(parent)
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.threadclass.start()
        self.connect(self.threadclass, QtCore.SIGNAL(
            "PROGRESS_VALUE"), self.update_progress_bar)

    def update_progress_bar(self, val):
        self.progressBar.setValue(val)


class ThreadClass(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        global g_prog
        while True:
            val = g_prog
            self.emit(QtCore.SIGNAL("PROGRESS_VALUE"), val)


if __name__ == "__main__":
    a = QtWidgets.QApplication()
    app = MainUiClass()
    app.show()
    a.exec_()
