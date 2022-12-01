from PyQt5.QtWidgets import QToolButton, QSizePolicy, QGridLayout

Room_value = [
    ('미래관 449호 : ', 20), ('복지관 317호 : ', 80), ('법학관 스터디카페 : ', 58),
    ('복지관 303호 : ', 36), ('복지관 306호 : ', 74), ('복지관 311호 : ', 26)
]

roomlist = [x[0] for x in Room_value]
numlist = [x[1] for x in Room_value]

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
            if i == 1 or 3 or 4 or 5 or 7:
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            if i == 0:
                self.bubhakbutton[i] = Button(str("1"), self.buttonClicked)
            if i == 2:
                self.bubhakbutton[i] = Button(str("2"), self.buttonClicked)
            if i == 6:
                self.bubhakbutton[i] = Button(str("3"), self.buttonClicked)  
            for i in range(8 , 16):
                self.bubhakbutton[i] = Button(str(i-4), self.buttonClicked)
            for i in range(23, 32):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(17, 18):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(19, 21):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(21, 22):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(16, 17):
               self.bubhakbutton[i] = Button(str("12"), self.buttonClicked)
            for i in range(18, 19):
                self.bubhakbutton[i] = Button(str("13"), self.buttonClicked)
            for i in range(20, 21):
                self.bubhakbutton[i] = Button(str("14"), self.buttonClicked)
            for i in range(22, 23):
                self.bubhakbutton[i] = Button(str("15"), self.buttonClicked)
            for i in range(33, 34):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(35, 36):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(37, 38):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(39, 40):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(32, 33):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(34, 35):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(36, 37):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(38, 39):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(40, 42):
                self.bubhakbutton[i] = Button(str(i-20), self.buttonClicked)
            for i in range(42 , 46):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(46 , 48):
                self.bubhakbutton[i] = Button(str(i-24), self.buttonClicked)
            for i in range(48, 49):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(50, 51):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(52, 53):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(54, 55):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(49, 50):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(51, 52):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(53, 54):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(55, 56):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(56 , 58):
                self.bubhakbutton[i] = Button(str(i-28), self.buttonClicked)
            for i in range(58 , 62):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(62 , 64):
                self.bubhakbutton[i] = Button(str(i-32), self.buttonClicked)
            for i in range(64 , 65):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(66 , 67):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(68 , 69):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(70 , 71):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(65 , 66):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(67 , 68):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(69 , 70):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(71 , 72):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(72 , 74):
                self.bubhakbutton[i] = Button(str(i-36), self.buttonClicked)
            for i in range(74 , 78):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(78 , 80):
                self.bubhakbutton[i] = Button(str(i-40), self.buttonClicked)
            for i in range(80 , 81):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(82 , 83):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(84 , 85):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(86 , 87):
                self.bubhakbutton[i] = Button(str(i//2), self.buttonClicked)
            for i in range(81 , 82):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(83 , 84):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(85 , 86):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(87 , 88):
                self.bubhakbutton[i] = Button("X", self.buttonClicked)
            for i in range(88, 90):
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
    
    법학관스터디카페 = [
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

class Room3():
    def __init__(self, parent=None):
        super().__init__()

        self.bokjionebutton = [x for x in range(0 , 48)]
        for i in range(0 , 48):
            for i in range(0 , 3):
                self.bokjionebutton[i] = Button(str(i+1), self.buttonClicked)
            for i in range(3, 4):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
            for i in range(4 , 6):
                self.bokjionebutton[i] = Button(str(i), self.buttonClicked)
            for i in range(6 , 9):
                self.bokjionebutton[i] = Button(str(i), self.buttonClicked)
            for i in range(9 , 10):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
            for i in range(10 , 12):
                self.bokjionebutton[i] = Button(str(i-1), self.buttonClicked)
            for i in range(12 , 18):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
            for i in range(18 , 21):
                self.bokjionebutton[i] = Button(str(i-7), self.buttonClicked)
            for i in range(21 , 22):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
            for i in range(22 , 24):
                self.bokjionebutton[i] = Button(str(i-8), self.buttonClicked)
            for i in range(24 , 27):
                self.bokjionebutton[i] = Button(str(i-8), self.buttonClicked)
            for i in range(27 , 28):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
            for i in range(28 , 30):
                self.bokjionebutton[i] = Button(str(i-9), self.buttonClicked)
            for i in range(30 , 36):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
            for i in range(36 , 39):
                self.bokjionebutton[i] = Button(str(i-15), self.buttonClicked)
            for i in range(39 , 42):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
            for i in range(42 , 45):
                self.bokjionebutton[i] = Button(str(i-18), self.buttonClicked)
            for i in range(45 , 48):
                self.bokjionebutton[i] = Button("X", self.buttonClicked)
        
        self.bokjioneLayout = QGridLayout()

        for i in range(0, 48):
            if 0 <= i <= 5:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 0, i)
            elif 6 <= i <= 11:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 1, i-6)
            elif 12 <= i <= 17:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 2, i-12)
            elif 18 <= i <= 23:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 3, i-18)
            elif 24 <= i <= 29:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 4, i-24)
            elif 30 <= i <= 35:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 5, i-30)
            elif 36 <= i <= 41:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 6, i-36)
            elif 42 <= i <= 47:
                self.bokjioneLayout.addWidget(self.bokjionebutton[i], 7, i-42)
            
    def buttonClicked(self):
        button = self.sender()
        key = button.text()

    복지관311호 = [
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15",
        "16", "17", "18", "19", "20",
        "21", "22", "23", "24", "25",
        "26"
    ]

class Room4():
    def __init__(self, parent=None):
        super().__init__()

        self.bokjithreebutton = [x for x in range(0 , 56)]
        for i in range(0, 56):
            for i in range(0 , 3):
                self.bokjithreebutton[i] = Button(str(i+1), self.buttonClicked)
            for i in range(3, 4):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(4 , 7):
                self.bokjithreebutton[i] = Button(str(i), self.buttonClicked)
            for i in range(7 , 10):
                self.bokjithreebutton[i] = Button(str(i), self.buttonClicked)
            for i in range(10 , 11):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(11 , 14):
                self.bokjithreebutton[i] = Button(str(i-1), self.buttonClicked)
            for i in range(14 , 21):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(21 , 24):
                self.bokjithreebutton[i] = Button(str(i-8), self.buttonClicked)
            for i in range(24 , 25):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(25 , 28):
                self.bokjithreebutton[i] = Button(str(i-9), self.buttonClicked)
            for i in range(28 , 31):
                self.bokjithreebutton[i] = Button(str(i-9), self.buttonClicked)
            for i in range(31 , 32):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(32 , 35):
                self.bokjithreebutton[i] = Button(str(i-10), self.buttonClicked)
            for i in range(35 , 42):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(42 , 45):
                self.bokjithreebutton[i] = Button(str(i-17), self.buttonClicked)
            for i in range(45 , 46):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(46 , 49):
                self.bokjithreebutton[i] = Button(str(i-18), self.buttonClicked)
            for i in range(49 , 52):
                self.bokjithreebutton[i] = Button(str(i-18), self.buttonClicked)
            for i in range(52 , 53):
                self.bokjithreebutton[i] = Button("X", self.buttonClicked)
            for i in range(53 , 56):
                self.bokjithreebutton[i] = Button(str(i-19), self.buttonClicked)
        
        self.bokjithreeLayout = QGridLayout()

        for i in range(0, 56):
            if 0 <= i <= 6:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 0, i)
            elif 7 <= i <= 13:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 1, i-7)
            elif 14 <= i <= 20:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 2, i-14)
            elif 21 <= i <= 27:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 3, i-21)
            elif 28 <= i <= 34:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 4, i-28)
            elif 35 <= i <= 41:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 5, i-35)
            elif 42 <= i <= 48:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 6, i-42)
            elif 49 <= i <= 55:
                self.bokjithreeLayout.addWidget(self.bokjithreebutton[i], 7, i-49)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

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

class Room5():
    def __init__(self, parent=None):
        super().__init__()

        self.bokjisixbutton = [x for x in range(0 , 126)]
        for i in range(0, 126):
            for i in range(0 , 5):
                self.bokjisixbutton[i] = Button(str(i+1), self.buttonClicked)
            for i in range(5, 6):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(6 , 9):
                self.bokjisixbutton[i] = Button(str(i), self.buttonClicked)
            for i in range(9 , 14):
                self.bokjisixbutton[i] = Button(str(i), self.buttonClicked)
            for i in range(14 , 15):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(15 , 18):
                self.bokjisixbutton[i] = Button(str(i-1), self.buttonClicked)
            for i in range(18 , 27):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(27 , 32):
                self.bokjisixbutton[i] = Button(str(i-10), self.buttonClicked)
            for i in range(32 , 33):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(33 , 36):
                self.bokjisixbutton[i] = Button(str(i-11), self.buttonClicked)
            for i in range(36 , 41):
                self.bokjisixbutton[i] = Button(str(i-11), self.buttonClicked)
            for i in range(41, 42):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(42 , 45):
                self.bokjisixbutton[i] = Button(str(i-12), self.buttonClicked)
            for i in range(45 , 54):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(54 , 59):
                self.bokjisixbutton[i] = Button(str(i-21), self.buttonClicked)
            for i in range(59 , 60):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(60 , 63):
                self.bokjisixbutton[i] = Button(str(i-22), self.buttonClicked)
            for i in range(63 , 68):
                self.bokjisixbutton[i] = Button(str(i-22), self.buttonClicked)
            for i in range(68 , 69):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(69 , 72):
                self.bokjisixbutton[i] = Button(str(i-23), self.buttonClicked)
            for i in range(72 , 81):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(81, 86):
                self.bokjisixbutton[i] = Button(str(i-32), self.buttonClicked)
            for i in range(86 , 87):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(87 , 90):
                self.bokjisixbutton[i] = Button(str(i-33), self.buttonClicked)
            for i in range(90 , 95):
                self.bokjisixbutton[i] = Button(str(i-33), self.buttonClicked)
            for i in range(95 , 96):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(96 , 99):
                self.bokjisixbutton[i] = Button(str(i-34), self.buttonClicked)
            for i in range(99 , 108):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(108 , 113):
                self.bokjisixbutton[i] = Button(str(i-43), self.buttonClicked)
            for i in range(113 , 117):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
            for i in range(117 , 122):
                self.bokjisixbutton[i] = Button(str(i-47), self.buttonClicked)
            for i in range(122 , 126):
                self.bokjisixbutton[i] = Button("X", self.buttonClicked)
        
        self.bokjisixLayout = QGridLayout()

        for i in range(0, 126):
            if 0 <= i <= 8:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 0, i)
            elif 9 <= i <= 17:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 1, i-9)
            elif 18 <= i <= 26:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 2, i-18)
            elif 27 <= i <= 35:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 3, i-27)
            elif 36 <= i <= 44:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 4, i-36)
            elif 45 <= i <= 53:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 5, i-45)
            elif 54 <= i <= 62:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 6, i-54)
            elif 63 <= i <= 71:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 7, i-63)
            elif 72 <= i <= 80:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 8, i-72)
            elif 81 <= i <= 89:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 9, i-81)
            elif 90 <= i <= 98:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 10, i-90)
            elif 99 <= i <= 107:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 11, i-99)
            elif 108 <= i <= 116:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 12, i-108)
            elif 117 <= i <= 125:
                self.bokjisixLayout.addWidget(self.bokjisixbutton[i], 13, i-117)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

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

class Room6():
    def __init__(self, parent=None):
        super().__init__()

        self.bokjisevenbutton = [x for x in range(0 , 220)]
        for i in range(0, 220):
            for i in range(0 , 4):
                self.bokjisevenbutton[i] = Button(str(i+1), self.buttonClicked)
            for i in range(4, 5):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(5 , 14):
                self.bokjisevenbutton[i] = Button(str(i), self.buttonClicked)
            for i in range(14 , 15):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(15 , 20):
                self.bokjisevenbutton[i] = Button(str(i-1), self.buttonClicked)
            for i in range(20 , 40):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(40 , 44):
                self.bokjisevenbutton[i] = Button(str(i-21), self.buttonClicked)
            for i in range(44 , 45):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(45 , 46):
                self.bokjisevenbutton[i] = Button(str(i-22), self.buttonClicked)
            for i in range(46 , 51):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(51 , 54):
                self.bokjisevenbutton[i] = Button(str(i-27), self.buttonClicked)
            for i in range(54 , 55):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(55 , 60):
                self.bokjisevenbutton[i] = Button(str(i-28), self.buttonClicked)
            for i in range(60 , 65):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(65 , 66):
                self.bokjisevenbutton[i] = Button(str(i-33), self.buttonClicked)
            for i in range(66 , 71):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(71 , 74):
                self.bokjisevenbutton[i] = Button(str(i-38), self.buttonClicked)
            for i in range(74 , 80):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(80 , 100):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(100 , 104):
                self.bokjisevenbutton[i] = Button(str(i-64), self.buttonClicked)
            for i in range(104 , 105):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(105 , 106):
                self.bokjisevenbutton[i] = Button(str(i-65), self.buttonClicked)
            for i in range(106 , 111):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(111 , 114):
                self.bokjisevenbutton[i] = Button(str(i-70), self.buttonClicked)
            for i in range(114 , 115):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(115 , 120):
                self.bokjisevenbutton[i] = Button(str(i-71), self.buttonClicked)
            for i in range(120 , 125):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(125 , 126):
                self.bokjisevenbutton[i] = Button(str(i-76), self.buttonClicked)
            for i in range(126 , 131):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(131 , 134):
                self.bokjisevenbutton[i] = Button(str(i-81), self.buttonClicked)
            for i in range(134 , 160):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(160 , 164):
                self.bokjisevenbutton[i] = Button(str(i-107), self.buttonClicked)
            for i in range(164 , 165):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(165 , 166):
                self.bokjisevenbutton[i] = Button(str(i-108), self.buttonClicked)
            for i in range(166 , 171):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(171 , 174):
                self.bokjisevenbutton[i] = Button(str(i-113), self.buttonClicked)
            for i in range(174 , 175):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(175 , 180):
                self.bokjisevenbutton[i] = Button(str(i-114), self.buttonClicked)
            for i in range(180 , 185):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(185 , 186):
                self.bokjisevenbutton[i] = Button(str(i-119), self.buttonClicked)
            for i in range(186 , 191):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(191 , 194):
                self.bokjisevenbutton[i] = Button(str(i-124), self.buttonClicked)
            for i in range(194 , 215):
                self.bokjisevenbutton[i] = Button("X", self.buttonClicked)
            for i in range(215 , 220):
                self.bokjisevenbutton[i] = Button(str(i-145), self.buttonClicked)     
        
        self.bokjisevenLayout = QGridLayout()

        for i in range(0, 220):
            if 0 <= i <= 19:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 0, i)
            elif 20 <= i <= 39:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 1, i-20)
            elif 40 <= i <= 59:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 2, i-40)
            elif 60 <= i <= 79:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 3, i-60)
            elif 80 <= i <= 99:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 4, i-80)
            elif 100 <= i <= 119:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 5, i-100)
            elif 120 <= i <= 139:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 6, i-120)
            elif 140 <= i <= 159:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 7, i-140)
            elif 160 <= i <= 179:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 8, i-160)
            elif 180 <= i <= 199:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 9, i-180)
            elif 200 <= i <= 219:
                self.bokjisevenLayout.addWidget(self.bokjisevenbutton[i], 10, i-200)

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
    