import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLineEdit, QToolButton, QMessageBox
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtGui import QFont

from Seatnum import Seat
from Room import Room
from login import check

# mycalc3의 Button class 그대로 가져옴
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

# 로그인 창의 GUI 코드
class Login(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Display Window
        title = QLabel("국민대 자습실 현황", self)
        title.setFont(QFont("Arial", 20))

        id_text = QLineEdit()
        pw_text = QLineEdit()

        id_text.setPlaceholderText("아이디")
        pw_text.setPlaceholderText("비밀번호")
        pw_text.setEchoMode(QLineEdit.Password)

        # Button
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

    # 로그인 정보가 맞다면 Controller에 신호보냄
    def loginComfirm(self, id, pw):
        if id == '':
            QMessageBox.about(self, "로그인", "아이디를 입력하세요")
        elif pw == '':
            QMessageBox.about(self, "로그인", "비밀번호를 입력하세요")
        else:
            result = check(id, pw)
            if result:
                self.switch_window.emit()
            else:
                QMessageBox.about(self, "로그인", "아이디 비밀번호가 잘못되었습니다")

# 자습실을 보여주는 창의 GUI 코드
class Main(QWidget):
    # 일단 돌아가는지 확인하기 위해서 unable은 10으로, entire을 20으로 설정하도록 하자. -> 이제 오류 안나는데 확인바람
    entireSeat = int(input()) # 가려고 하는 장소의 좌석 수, 서버에서 정수형으로 받아와야 함. input으로 받는 건 임시코드
    unableSeat = int(input()) # 앉을 수 없는 좌석 수, 서버에서 정수형으로 받아와야 함. input으로 받는 건 임시코드
    Seat = Seat(entireSeat, unableSeat)
    switch_window = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Display Window

        # Digit Buttons
        roomLayout = QGridLayout()

        # roomlist을 room.py로 넘기면 좋을것같음
        # 6개 정도? 아니면 미래관 449랑 복지관 317, 복지관 306 정도로만 줄여도 될 듯.
        roomlist = [
            "미래관 449호 : ", "복지관 317호 : ", "법학관 스터디카페 : ",
            "복지관 303호 : ", "복지관 306호 : ", "복지관 311호 : ",
        ]

        r = 0; c = 0
        for btnText in roomlist:
            # 돌아가는지 확인하기 위해 Seat(10, 20)으로 설정.
            # 각각마다 n, m의 값이 달라지니 이를 받아와야할듯.
            s = Seat(self.entireSeat, self.unableSeat)
            # 남은 자리수와 전체 자리수 모두 나오도록 함
            # 남은 자리수가 음수여도 뜨는 문제가 있음 - 수정 필요
            button = Button(btnText + str(s.getLeftSeatNum()) + "/" + str(s.getSeatNum()), self.Switch)
            roomLayout.addWidget(button, r, c)
            c += 1
            if c > 2:
                c = 0
                r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addLayout(roomLayout, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # Controller에 보낼 신호를 생성
    # 버튼을 누르면 Controller에 방이름 신호보냄
    def Switch(self):
        button = self.sender()
        key = button.text()[:-5]
        self.switch_window.emit(key)

# 방의 상세정보를 보여주는 창의 GUI 코드
class Reservation(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room):
        super().__init__()

        # Display Window
        title = QLabel(room, self)

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mirae = Room()
        mainLayout.addWidget(title, 0, 0)
        mainLayout.addLayout(mirae.miraeLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 6, 9)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # 버튼을 누르면 Controller에 신호보냄
    def quit(self):
        self.switch_window.emit()

# 신호를 받아서 다른 창을 띄워주는 코드
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
