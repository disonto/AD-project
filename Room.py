import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLineEdit, QToolButton, QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtGui import QFont

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Room():
    def __init__(self, parent=None):
        super().__init__()

        self.miraebutton = [x for x in range(0 , 45)]
        for i in range(0 , 4):
            self.miraebutton[i] = Button(str(i+1), self.buttonClicked)
        for i in range(4, 5):
            self.miraebutton[i] = Button("X", self.buttonClicked)
        for i in range(5 , 9):
            self.miraebutton[i] = Button(str(i), self.buttonClicked)
        for i in range(9 , 18):
            self.miraebutton[i] = Button("X", self.buttonClicked)
        for i in range(18 , 22):
            self.miraebutton[i] = Button(str(i-9), self.buttonClicked)
        for i in range(22 , 23):
            self.miraebutton[i] = Button("X", self.buttonClicked)
        for i in range(23 , 27):
            self.miraebutton[i] = Button(str(i-10), self.buttonClicked)
        for i in range(27 , 36):
            self.miraebutton[i] = Button("X", self.buttonClicked)
        for i in range(36 , 40):
            self.miraebutton[i] = Button(str(i-19), self.buttonClicked)
        for i in range(40 , 45):
            self.miraebutton[i] = Button("X", self.buttonClicked)
        
        self.miraeLayout = QGridLayout()

        for i in range(0, 45):
            if 0 <= i <= 8:
                self.miraeLayout.addWidget(self.miraebutton[i], 0, i)
            elif 9 <= i <= 17:
                self.miraeLayout.addWidget(self.miraebutton[i], 1, i-9)
            elif 18 <= i <= 26:
                self.miraeLayout.addWidget(self.miraebutton[i], 2, i-18)
            elif 27 <= i <= 35:
                self.miraeLayout.addWidget(self.miraebutton[i], 3, i-27)
            elif 36 <= i <= 44:
                self.miraeLayout.addWidget(self.miraebutton[i], 4, i-36)

    미래관449호 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
    ]

    복지관317호 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25",
        "26", "27", "28", "29", "30",
        "31", "32", "33", "34", "35",
        "36", "37", "38", "39", "40",
        "41", "42", "43", "44", "45",
        "46", "47", "48", "49", "50",
        "51", "52", "53", "54", "55",
        "56", "57", "58", "59", "60",
        "61", "62", "63", "64", "65",
        "66", "67", "68", "69", "70",
        "71", "72", "73", "74", "75",
        "76", "77", "18", "79", "80"
    ]

    복지관스터디카페 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25",
        "26", "27", "28", "29", "30",
        "31", "32", "33", "34", "35",
        "36", "37", "38", "39", "40",
        "41", "42", "43", "44", "45",
        "46", "47", "48", "49", "50",
        "51", "52", "53", "54", "55",
        "56", "57", "58"
    ]

    복지관303호 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25",
        "26", "27", "28", "29", "30",
        "31", "32", "33", "34", "35",
        "36"
    ]

    복지관306호 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25",
        "26", "27", "28", "29", "30",
        "31", "32", "33", "34", "35",
        "36", "37", "38", "39", "40",
        "41", "42", "43", "44", "45",
        "46", "47", "48", "49", "50",
        "51", "52", "53", "54", "55",
        "56", "57", "58", "59", "60",
        "61", "62", "63", "64", "65",
        "66", "67", "68", "69", "70",
        "71", "72", "73", "74"
    ]

    복지관311호 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25",
        "26"
    ]
    
    def buttonClicked(self):
        button = self.sender()
        key = button.text()