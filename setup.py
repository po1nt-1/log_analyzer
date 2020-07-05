import backend
import main
from PySide2 import QtWidgets, QtCore, QtGui

g_login = ""
g_begin = ""
g_end = ""
g_folder_path = ""
g_file_path = ""

g_csv_cache = []

g_current_data = []
g_current_page_num = 1
g_last_page_num = 1


def save_login(login):
    global g_login
    if login == "":
        login = None
    g_login = login
    print("сохранён login:", g_login)


def save_begin(begin):
    global g_begin
    g_begin = begin
    print("сохранён begin:", g_begin)

    g_begin = backend.ok_to_unix(g_begin)


def save_end(end):
    global g_end
    g_end = end
    print("сохранён end:", g_end)

    g_end = backend.ok_to_unix(g_end)


def load_folder(folder):
    global g_login
    global g_folder_path
    global g_begin
    global g_end
    g_folder_path = folder
    print("сохранён folder:", g_folder_path)

    backend.check_csv_files_folder(g_folder_path)
    backend.init_note_list()

    backend.filter(login=g_login, date_range=[g_begin, g_end])


def load_file(file_path):
    global g_file_path
    global g_current_data
    global g_current_page_num
    global g_last_page_num
    g_file_path = file_path
    print("сохранён file:", g_file_path)
    g_current_page_num = 1

    g_current_data, g_last_page_num = backend.show_page_from_csv(
        g_file_path, 1)


def reload_page():
    global g_file_path
    global g_current_data
    global g_current_page_num
    global g_last_page_num

    g_current_data, g_last_page_num = backend.show_page_from_csv(
        g_file_path, g_current_page_num)


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
            save_begin(self.begin_date.dateTime().toPython())
            save_end(self.end_date.dateTime().toPython())
            save_login(self.login_line.text())
            load_folder(status)

    def selection_file_check(self):
        status = self.get_file_name()
        if not status:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Файл не был выбран")
        else:
            load_file(status)
            self.create_table()
            self.show_current_page()

    def back(self):
        global g_current_page_num
        global g_last_page_num
        global g_current_data

        if len(g_current_data) == 0:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Файл не был выбран")
            return

        if g_current_page_num > 1:
            g_current_page_num -= 1
            reload_page()
            self.current_page_inticator()
            self.show_current_page()
        else:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Это самая первая страница")

    def forward(self):
        global g_current_page_num
        global g_last_page_num
        global g_current_data

        if len(g_current_data) == 0:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Файл не был выбран")
            return

        if g_current_page_num < g_last_page_num:
            g_current_page_num += 1
            reload_page()
            self.current_page_inticator()
            self.show_current_page()
        else:
            QtWidgets.QMessageBox.about(
                self, "Предупреждение", "Это самая последняя страница")

    def current_page_inticator(self):
        self.current_page_num.setPlainText(str(g_current_page_num))

    def last_page_indicator(self):
        self.last_page_num.setPlainText(str(g_last_page_num))

    def create_table(self):
        global g_current_data
        self.table_csv.setRowCount(0)
        self.table_csv.setColumnCount(0)
        for row in g_current_data:
            self.table_csv.insertRow(0)
        for col in g_current_data[0]:
            self.table_csv.insertColumn(0)

    def paint(self, row, col):
        self.table_csv.item(row, col).setBackground(
            QtGui.QColor(106, 188, 183))

    def show_current_page(self):
        global g_current_data
        self.current_page_inticator()
        self.last_page_indicator()

        if len(g_current_data) != 0:
            for row_number, row_value in enumerate(g_current_data):
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
    app.exec_()
