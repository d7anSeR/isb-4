import sys
import logging

from PyQt5.QtWidgets import QApplication

from app import MainWindow


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
