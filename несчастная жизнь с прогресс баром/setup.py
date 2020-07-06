import backend
import main
import time
from PySide2 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, \
    QProgressBar, QPushButton, QVBoxLayout


g_prog = 0


def outsider(prog):
    global g_prog
    g_prog = prog


class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while True:
            cnt = g_prog
            self.change_value.emit(cnt)


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Комиссия"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(100)
        vbox.addWidget(self.progressbar)
        self.button = QPushButton("Start Progressbar")
        self.button.clicked.connect(self.startProgressBar)
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        self.show()

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)


class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.select_folder_button.clicked.connect(
            self.selection_folder_check)
        self.show_csv_button.clicked.connect(
            self.selection_file_check)
        self.page_back_button.clicked.connect(self.back)
        self.page_forward_button.clicked.connect(self.forward)

        self.g_login = ""
        self.g_begin = ""
        self.g_end = ""
        self.g_folder_path = ""
        self.g_file_path = ""

        self.g_current_data = []
        self.g_current_page_num = 1
        self.g_last_page_num = 1

    def save_login(self, login):
        if login == "":
            login = None
        self.g_login = login
        print("сохранён login:", self.g_login)

    def save_begin(self, begin):
        self.g_begin = begin
        print("сохранён begin:", self.g_begin)

        self.g_begin = backend.ok_to_unix(self.g_begin)

    def save_end(self, end):
        self.g_end = end
        print("сохранён end:", self.g_end)

        self.g_end = backend.ok_to_unix(self.g_end)

    def load_folder(self, folder):
        self.g_folder_path = folder
        print("сохранён folder:", self.g_folder_path)

        backend.check_csv_files_folder(self.g_folder_path)
        backend.init_note_list()
        backend.filter(login=self.g_login, date_range=[
                       self.g_begin, self.g_end])

    def load_file(self, file_path):
        self.g_file_path = file_path
        print("сохранён file:", self.g_file_path)
        self.g_current_page_num = 1

        self.g_current_data, self.g_last_page_num = backend.show_page_from_csv(
            self.g_file_path, 1)

    def reload_page(self):
        self.g_current_data, self.g_last_page_num = backend.show_page_from_csv(
            self.g_file_path, self.g_current_page_num)

    def get_folder_name(self):
        return QtWidgets.QFileDialog.getExistingDirectory(
            self, "Файловый менеджер")

    def get_file_name(self):
        return QtWidgets.QFileDialog.getOpenFileName()[0]

    def selection_folder_check(self):
        status = self.get_folder_name()
        if not status:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Папка не была выбрана")
        else:
            self.save_begin(self.begin_date.dateTime().toPython())
            self.save_end(self.end_date.dateTime().toPython())
            self.save_login(self.login_line.text())
            self.load_folder(status)

    def selection_file_check(self):
        status = self.get_file_name()
        if not status:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Файл не был выбран")
        else:
            self.load_file(status)
            self.create_table()
            self.show_current_page()

    def back(self):
        if len(self.g_current_data) == 0:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Файл не был выбран")
            return

        if self.g_current_page_num > 1:
            self.g_current_page_num -= 1
            self.reload_page()
            self.current_page_inticator()
            self.show_current_page()
        else:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Это самая первая страница")

    def forward(self):
        if len(self.g_current_data) == 0:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Файл не был выбран")
            return

        if self.g_current_page_num < self.g_last_page_num:
            self.g_current_page_num += 1
            self.reload_page()
            self.current_page_inticator()
            self.show_current_page()
        else:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Это самая последняя страница")

    def current_page_inticator(self):
        self.current_page_num.setPlainText(str(self.g_current_page_num))

    def last_page_indicator(self):
        self.last_page_num.setPlainText(str(self.g_last_page_num))

    def create_table(self):
        self.table_csv.setRowCount(0)
        self.table_csv.setColumnCount(0)
        for row in self.g_current_data:
            self.table_csv.insertRow(0)
        for col in self.g_current_data[0]:
            self.table_csv.insertColumn(0)

    def paint(self, row, col):
        self.table_csv.item(row, col).setBackground(
            QtGui.QColor(106, 188, 183))

    def show_current_page(self):
        self.current_page_inticator()
        self.last_page_indicator()

        if len(self.g_current_data) != 0:
            for row_number, row_value in enumerate(self.g_current_data):
                for item_number, item_value in enumerate(row_value):
                    self.table_csv.setItem(
                        row_number, item_number, QtWidgets.QTableWidgetItem(
                            list(row_value.values())[item_number])
                    )
                    roww = list(row_value.values())
                    if roww[4].isspace() or roww[4] == "" or \
                            roww[12] != str(0):
                        self.paint(row_number, item_number)

            self.table_csv.setHorizontalHeaderLabels(backend.headers)
            self.table_csv.horizontalHeaderItem(
                item_number).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.table_csv.resizeColumnsToContents()
        else:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Файл пуст")


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    App = QApplication([])
    window = Window()
    App.exec_()
    app.exec_()
