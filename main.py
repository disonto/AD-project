import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from Seatnum import Seat
from Room import Room

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

class Login(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Display Window
        id_text = QLineEdit()
        pw_text = QLineEdit()

        # Digit Buttons
        Login_btn = Button("login", self.loginComfirm)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(id_text, 0, 0)
        mainLayout.addWidget(pw_text, 1, 0)
        mainLayout.addWidget(Login_btn, 2, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    def loginComfirm(self):
        if True:
            self.switch_window.emit()

class Main(QWidget):
    Seat = Seat()
    switch_window = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()

        # Display Window

        # Digit Buttons
        roomLayout = QGridLayout()
        roomlist = [
            "미래관 449호 : ", "00관 ***호 : ", "00관 ***호 : ",
            "00관 ***호 : ", "00관 ***호 : ", "00관 ***호 : ",
            "00관 ***호 : ", "00관 ***호 : ", "00관 ***호 : ",
        ]
        r = 0; c = 0
        for btnText in roomlist:
            button = Button(btnText + str(Seat.Seatnum), self.Switch)
            roomLayout.addWidget(button, r, c)
            c += 1
            if c > 2:
                c = 0;
                r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(roomLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    def Switch(self):
        button = self.sender()
        key = button.text()[:-5]
        if True:
            self.switch_window.emit(key)

class Reservation(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room):
        super().__init__()
        title = QLabel(room, self)
        quit_btn = Button("나가기", self.quit)

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(title, 0, 0)
        mainLayout.addWidget(quit_btn, 1, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    def quit(self):
        if True:
            self.switch_window.emit()

class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(lambda: self.show_main('login'))
        self.login.show()

    def show_main(self, where):
        self.main = Main()
        self.main.switch_window.connect(self.show_Seat)
        if where == 'login':
            self.login.close()
        elif where == 'seat':
            self.seat.close()
        self.main.show()

    def show_Seat(self, room):
        self.seat = Reservation(room)
        self.seat.switch_window.connect(lambda: self.show_main('seat'))
        self.main.close()
        self.seat.show()


def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()