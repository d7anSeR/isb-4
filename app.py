import os

from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QFileDialog, QMessageBox,
                             QPushButton, QVBoxLayout, QTabWidget, QHBoxLayout)
from PyQt5.QtGui import QIcon, QDoubleValidator
import multiprocessing as mp

from check_card import find_num_card
from work_with_file import write_file, read_file
from graph import create_stats
from luhn import algorithm_luhn


class MainWindow(QWidget):
    """class window with working functionality"""

    def __init__(self) -> None:
        """class constructor"""
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(100, 400, 1500, 200)
        self.setWindowTitle('Laboratory Work №4')
        self.flag_num_card = False
        self.dict_path = {
            "path_bins": '\0',
            "path_default_hash": '\0',
            "path_num_card": '\0',
            "path_last_number": '\0',
            "path_processes": '\0',
            "path_graph": '\0',
            "path_check_luhn": '\0',
            "path_time_statistic": '\0'
        }
        
        # self.setWindowIcon(QIcon('icon.jpg'))
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.main(), "main")
        tabs.addTab(self.generation_graph(), "generation of graph")
        tabs.addTab(self.card_num_verification(), "card number verification")
        layout.addWidget(tabs)
        self.show()

    def gen_num_card(self):
        write_file(self.dict_path["path_num_card"], find_num_card(
            read_file(self.dict_path["path_default_hash"]),
            read_file(self.dict_path["path_bins"]),
            read_file(self.dict_path["path_last_number"]),
            int(read_file(self.dict_path["path_processes"]))))

    def main(self) -> QWidget:
        path_tab1 = QWidget()
        layout = QVBoxLayout()
        layout_main = QHBoxLayout()
        layout.addWidget(QLabel("bins for the card number\n"))
        layout.addWidget(QLabel("1. 5197 47\n2. 5376 43\n3. 5486 01\n4. 5486 55\n5. 5521 86\n6. 5551 56\n7. 5559 47\n8. 5140 55\n9. 5312 37\n10. 5583 34\n11. 5411 90\n12. 5450 36\n13. 5474 50\n\n\n"))
        layout.addWidget(QLabel("select the path where you want to save all files\n"))
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.insert_dir)
        self.filename_edit = QLineEdit()
        self.filename_edit.setValidator(
            QDoubleValidator(0.99, 99.99, 2))
        layout_main.addWidget(QLabel('Folder:'))
        layout_main.addWidget(self.filename_edit)
        layout_main.addWidget(file_browse)
        layout_main.addSpacing(100)
        layout_main.addLayout(layout_main)
        layout_button_num_card = QVBoxLayout()
        layout_button_num_card.addWidget(
            QLabel("You can build a graph based on the received data\n"))
        self.button_num_card = QPushButton("calculation card number")
        self.button_num_card.clicked.connect(self.gen_num_card)
        layout_button_num_card.addWidget(self.button_num_card)
        layout.addLayout(layout_button_num_card)
        layout.addLayout(layout_main)
        path_tab1.setLayout(layout)
        return path_tab1

    def create_histogram(self):
        # write_file(self.dict_path["path_time_statistic"])
        print(1)
    
    def generation_graph(self) -> QWidget:
        path_tab2 = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(
            QLabel("You can build a graph based on the received data\n"))
        layout.addSpacing(100)
        self.button_hist = QPushButton("create histogram")
        self.button_hist.clicked.connect(self.create_histogram)
        layout.addWidget(self.button_hist)
        path_tab2.setLayout(layout)
        return path_tab2

    def algorithm_luhn(self):
        # write_file(self.dict_path["path_check_luhn"],
        #             str(read_file(self.dict_path["path_num_card"]) + 
        #                 " is " + algorithm_luhn(read_file(self.dict_path["path_num_card"]))))
        print(1)

    def card_num_verification(self) -> QWidget:
        path_tab3 = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(
            QLabel("Check the card number using the 'Lunh' algorithm"))
        layout.addSpacing(100)
        self.button_algorithm = QPushButton("checking of number")
        self.button_algorithm.clicked.connect(self.algorithm_luhn)
        layout.addWidget(self.button_algorithm)
        path_tab3.setLayout(layout)
        return path_tab3

    def insert_dir(self) -> None:
        name = QFileDialog.getExistingDirectory(self)
        self.dict_path["path_num_card"] = os.path.join(name, "card_num.txt")
        self.dict_path["path_default_hash"] = os.path.join(name, "default_hash.txt")
        self.dict_path["path_bins"] = os.path.join(name, "bins.txt")
        self.dict_path["path_last_number"] = os.path.join(name, "last_number.txt")
        self.dict_path["path_processes"] = os.path.join(name, "processes.txt")
        self.dict_path["path_time_statistic"] = os.path.join(name, "time_statistic.txt")
        self.dict_path["path_check_luhn"] = os.path.join(name, "check_luhn.txt")
        self.dict_path["path_graph"] = os.path.join(name, "graph.jpg")
        self.flag_num_card = False
        self.filename_edit.setText(self.dict_path["path_num_card"])
        self.button_num_card.setStyleSheet("background-color : white")
        self.button_algorithm.setStyleSheet("background-color : white")
        self.button_hist.setStyleSheet("background-color : white")
        write_file(self.dict_path["path_default_hash"],
                   "cb28fea647fab039e21aedf9762c895f6514d70ae404d5eac3c2b1da26547745")
        write_file(self.dict_path["path_bins"]," ".join(["519747", "537643", "548601", "548655",
                                                         "552186", "555156", "555947", "514055", 
                                                         "531237", "558334", "541190", "545036", "547450"]))
        write_file(self.dict_path["path_last_number"], "5623")
        write_file(self.dict_path["path_processes"], str(mp.cpu_count()))
