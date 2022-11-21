import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLineEdit, QToolButton, QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtGui import QFont

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

        title = QLabel("국민대 자습실 현황",self)
        title.setFont(QFont("Arial", 20))

        id_text.setPlaceholderText("아이디")
        pw_text.setPlaceholderText("비밀번호")
        pw_text.setEchoMode(QLineEdit.Password)

        # Digit Buttons
        Login_btn = Button("login", lambda : self.loginComfirm(id_text.text(), pw_text.text()))

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(title, 0, 0)
        mainLayout.addWidget(id_text, 1, 0)
        mainLayout.addWidget(pw_text, 2, 0)
        mainLayout.addWidget(Login_btn, 3, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    def loginComfirm(self, id, pw):
        if id == '':
            QMessageBox.about(self, "로그인", "아이디를 입력하세요")
        elif pw == '':
            QMessageBox.about(self, "로그인", "비밀번호를 입력하세요")
        else:
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
            "미래관 449호 : ", "공학관 ***호 : ", "00관 ***호 : ",
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
    
#참고한 코드 : https://stackoverflow.com/questions/40982518/argument-1-has-unexpected-type-nonetype
#    https://blog.naver.com/PostView.naver?blogId=jochanig&logNo=222454643551&categoryNo=1&parentCategoryNo=1&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
#    소프2 계산기
#    https://wikidocs.net/35792
#    https://mr-doosun.tistory.com/10