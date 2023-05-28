import os
import time

from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QFileDialog, QMessageBox,
                             QPushButton, QVBoxLayout, QTabWidget, QHBoxLayout)
from PyQt5.QtGui import QDoubleValidator
import multiprocessing as mp

from check_card import find_num_card
from work_with_file import write_settings, read_settings, read_statistic, write_statistic
from graph import create_graph
from luhn import algorithm_luhn


class MainWindow(QWidget):
    """class window with working functionality"""

    def __init__(self) -> None:
        """class constructor"""
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        """the method initializes the input values"""
        self.setGeometry(100, 100, 800, 200)
        self.setWindowTitle('Laboratory Work №4')
        self.flag_select_folder = False
        self.flag_find_num_card = False
        self.flag_luhn = False
        self.flag_hist = False
        settings = {
            'bins': ['519747', '537643', '548601', '548655',
                     '552186', '555947', '514055',
                     '531237', '558334', '541190', '545036',
                     '547450', '555156'],
            'default_hash':
            'cb28fea647fab039e21aedf9762c895f6514d70ae404d5eac3c2b1da26547745',
            'last_num': '5623',
            'card_num': '',
            'processes': '',
            'res_luhn': '',
            'graph': ''
        }
        write_settings(settings, 'settings.json')
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()
        tabs.addTab(self.main(), "main")
        tabs.addTab(self.generation_graph(), "generation of graph")
        tabs.addTab(self.card_num_verification(), "card number verification")
        layout.addWidget(tabs)
        self.show()

    def gen_num_card(self) -> None:
        """the method launches a function to find 
        the card number for different pools"""
        if self.flag_select_folder and self.flag_find_num_card == False:
            pools = mp.cpu_count()
            result = 0
            settings = read_settings('settings.json')
            for i in range(1, pools + 1):
                start_time = time.time()
                result = find_num_card(
                    settings['default_hash'],
                    settings['bins'],
                    settings['last_num'], pools)
                final_time = time.time() - start_time
                write_statistic(
                    final_time, i, settings['processes'])
            self.flag_find_num_card = True
            settings['card_num'] = result
            self.button_num_card.setStyleSheet("background-color : green")
            write_settings(settings, 'settings.json')
        elif self.flag_select_folder == False:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("error: you have not selected a folder...")
            error.exec_()
        elif self.flag_find_num_card == True:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText(
                "error: you have already calculated the card number...")
            error.exec_()

    def main(self) -> QWidget:
        """the method outputs the main tab 
        with finding the card number"""
        path_tab1 = QWidget()
        layout = QVBoxLayout()
        layout_main = QHBoxLayout()
        settings = read_settings('settings.json')
        layout.addWidget(QLabel("Bins for the card number:\n"))
        for i in range(0, len(settings['bins'])):
            layout.addWidget(QLabel(f"{i + 1}. {settings['bins'][i]}\n"))
        layout.addWidget(
            QLabel("\n\n\nLast numbers of card: "))
        layout.addWidget(
            QLabel(settings['last_num']))
        layout.addWidget(
            QLabel("\n\n\nSelect the path where you want to save all files\n"))
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
            QLabel("You can use the selection to find the true card number\n"))
        self.button_num_card = QPushButton("calculation card number")
        self.button_num_card.clicked.connect(self.gen_num_card)
        layout_button_num_card.addWidget(self.button_num_card)
        layout.addLayout(layout_main)
        layout.addLayout(layout_button_num_card)
        path_tab1.setLayout(layout)
        return path_tab1

    def create_histogram(self) -> None:
        """the method calls the histogram 
        creation function"""
        if self.flag_select_folder == False:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("error: you have not selected a folder...")
            error.exec_()
        elif self.flag_find_num_card == False:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("error: you have not calculated the card number...")
            error.exec_()
        elif self.flag_hist == True:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("error: you have already created graphic...")
            error.exec_()
        else:
            self.flag_hist = True
            settings = read_settings('settings.json')
            create_graph(read_statistic(
                settings['processes']), settings['graph'])
            self.button_hist.setStyleSheet("background-color : green")

    def generation_graph(self) -> QWidget:
        """the method outputs a tab with which 
        can create a graph"""
        path_tab2 = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel("You can build a graph based on the received data\n"))
        self.button_hist = QPushButton("create histogram")
        self.button_hist.clicked.connect(self.create_histogram)
        layout.addWidget(self.button_hist)
        path_tab2.setLayout(layout)
        return path_tab2

    def algorithm_luhn(self) -> None:
        """the method calls the function of the luhn algorithm"""
        if self.flag_select_folder == False:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("error: you have not selected a folder...")
            error.exec_()
        elif self.flag_find_num_card == False:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("error: you have not calculated the card number...")
            error.exec_()
        elif self.flag_luhn == True:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("error: you have already done algorithm Luhn...")
            error.exec_()
        else:
            self.flag_luhn = True
            settings = read_settings('settings.json')
            result_algorithm = algorithm_luhn(settings["card_num"])
            val_luhn = f"Algorithm Luhn return - {result_algorithm}"
            settings['res_luhn'] = val_luhn
            write_settings(settings, 'settings.json')
            self.button_algorithm.setStyleSheet("background-color : green")

    def card_num_verification(self) -> QWidget:
        """the method that outputs the number 
        verification tab by the luna algorithm"""
        path_tab3 = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(
            QLabel("Check the card number using the 'Lunh' algorithm"))
        layout.addSpacing(100)
        self.button_algorithm = QPushButton("checking of number")
        self.button_algorithm.clicked.connect(self.algorithm_luhn)
        layout.addWidget(self.button_algorithm)
        path_tab3.setLayout(layout)
        return path_tab3

    def insert_dir(self) -> None:
        """method for selecting the folder where 
        input and output data will be saved"""
        name = QFileDialog.getExistingDirectory(self)
        settings = read_settings('settings.json')
        settings['processes'] = os.path.join(name, "processes.csv")
        settings['graph'] = os.path.join(name, "graph.jpg")
        write_settings(settings, 'settings.json')
        self.flag_select_folder = True
        self.flag_luhn = False
        self.flag_find_num_card = False
        self.flag_hist = False
        self.filename_edit.setText(name)
        self.button_num_card.setStyleSheet("background-color : white")
        self.button_algorithm.setStyleSheet("background-color : white")
        self.button_hist.setStyleSheet("background-color : white")
