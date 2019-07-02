from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


def main():
    # could accept args, no idea why
    app = QApplication()

    window = get_ui()
    window.show()

    exit(app.exec_())


def get_ui():
    # TODO: use compiled ui file instead of dynamic loading
    #  pyside2-uic mainwindow.ui > ui_mainwindow.py

    ui_file = QFile("mainwindow.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    return window


if __name__ == '__main__':
    main()
