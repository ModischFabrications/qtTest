from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


def main():
    app = QApplication()

    # TODO: use compiled ui file instead of dynamic loading
    #  pyside2-uic mainwindow.ui > ui_mainwindow.py
    ui_file = QFile("mainwindow.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()

    exit(app.exec_())


if __name__ == '__main__':
    main()
