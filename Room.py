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

class Room1():
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

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

    미래관449호 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
    ]

class Room2():
    def __init__(self, parent=None):
        super().__init__()

        self.bubhakbutton = [x for x in range(0 , 128)]
        
        for i in range(0, 128):
            if i == 0:
                self.bubhakbutton[i] = Button(str(1), self.buttonClicked)
            if i == 2:
                self.bubhakbutton[i] = Button(str(2), self.buttonClicked)
            if i == 6:
                self.bubhakbutton[i] = Button(str(3), self.buttonClicked)        
            if i == 1 or 3 or 4 or 5 or 7:
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(8 , 16):
                self.bubhakbutton[i] = Button(str(i-4), self.buttonClicked)
            if i == 16:
                self.bubhakbutton[i] = Button(str(12), self.buttonClicked)
            if i == 18:
                self.bubhakbutton[i] = Button(str(13), self.buttonClicked)
            if i == 20:
                self.bubhakbutton[i] = Button(str(14), self.buttonClicked)
            if i == 22:
                self.bubhakbutton[i] = Button(str(15), self.buttonClicked)
            for i in range(23, 32):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            if i == 17 or 19 or 21:
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            if i == 32 or 34 or 36 or 38:
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            if i == 33 or 35 or 37 or 39:
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            if i == 40 or 41:
                self.bubhakbutton[i] = Button(str(i-20), self.buttonClicked)
            for i in range(42 , 46):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(46 , 48):
                self.bubhakbutton[i] = Button(str(i-24), self.buttonClicked)
            if i == 48 or 50 or 52 or 54:
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            if i == 49 or 51 or 53 or 55:
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(56 , 58):
                self.bubhakbutton[i] = Button(str(i-28), self.buttonClicked)
            for i in range(58 , 62):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(62 , 64):
                self.bubhakbutton[i] = Button(str(i-32), self.buttonClicked)
            if i == 64 or 66 or 68 or 70:
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            if i == 65 or 67 or 69 or 71:
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(72 , 74):
                self.bubhakbutton[i] = Button(str(i-36), self.buttonClicked)
            for i in range(74 , 78):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(78 , 80):
                self.bubhakbutton[i] = Button(str(i-40), self.buttonClicked)
            if i == 80 or 82 or 84 or 86:
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            if i == 81 or 83 or 85 or 87:
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            if i == 88 or 89:
                self.bubhakbutton[i] = Button(str(i-44), self.buttonClicked)
            for i in range(90 , 94):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(94 , 96):
                self.bubhakbutton[i] = Button(str(i-48), self.buttonClicked)
            for i in range(96, 107):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(107, 109):
                self.bubhakbutton[i] = Button(str(i-59), self.buttonClicked)
            for i in range(109 , 112):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(112, 123):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(123, 125):
                self.bubhakbutton[i] = Button(str(i-73), self.buttonClicked)
            for i in range(125 , 128):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
        
        self.bubhakLayout = QGridLayout()

        for i in range(0, 128):
            if 0 <= i <= 15:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 0, i)
            elif 16 <= i <= 31:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 1, i-16)
            elif 32 <= i <= 47:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 2, i-32)
            elif 48 <= i <= 63:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 3, i-48)
            elif 64 <= i <= 79:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 4, i-64)
            elif 80 <= i <= 95:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 5, i-80)
            elif 96 <= i <= 111:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 6, i-96)
            elif 112 <= i <= 127:
                self.bubhakLayout.addWidget(self.bubhakbutton[i], 7, i-112)
    
    def buttonClicked(self):
        button = self.sender()
        key = button.text()

class Room3():
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
            
    def buttonClicked(self):
        button = self.sender()
        key = button.text()

class Room4():
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

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

class Room5():
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

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

class Room6():
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

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

    

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