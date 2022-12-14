import sys
import asyncio
import random

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QLineEdit, QToolButton, QMessageBox, QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtGui import QFont, QPixmap

from Seatnum import Seat, TcpClientAsync
from Room import roomlist, numlist, Room_value
from Room import miraeList, bubhakList, bokjioneList, bokjithreeList, bokjisixList, bokjisevenList
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
        pixmap = QPixmap("logo.png").scaled(125, 125)
        logo_img = QLabel()
        logo_img.setPixmap(pixmap)
        logo_img.setAlignment(Qt.AlignCenter)

        title = QLabel("국민대 자습실 현황", self)
        title.setFont(QFont("Arial", 20))

        id_text = QLineEdit()
        self.pw_text = QLineEdit()

        id_text.setPlaceholderText("아이디")
        self.pw_text.setPlaceholderText("비밀번호")
        self.pw_text.setEchoMode(QLineEdit.Password)

        # Button
        Login_btn = Button("login", lambda : self.loginComfirm(id_text.text(), self.pw_text.text()))

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(logo_img, 0, 0)
        mainLayout.addWidget(title, 1, 0)
        mainLayout.addWidget(id_text, 2, 0)
        mainLayout.addWidget(self.pw_text, 3, 0)
        mainLayout.addWidget(Login_btn, 4, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # 로그인 정보가 맞다면 Controller에 신호보냄
    def loginComfirm(self, id, pw):
        self.pw_text.setEchoMode(QLineEdit.Normal)
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
                self.pw_text.setEchoMode(QLineEdit.Password)

# 자습실을 보여주는 창의 GUI 코드
class Main(QWidget):
    switch_window = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()

        # Display Window

        # Digit Buttons
        roomLayout = QGridLayout()

        # 임시코드. 서버에서 실시간으로 불러오는 코드를 대체한다.
        unablelist = [random.randint(1, entire) for entire in numlist]

        r = 0; c = 0
        for btnText in roomlist:
            # 임시로 이미 찬 좌석 수는 입력 코드로 대체
            # i는 이게 끝나면 1씩 증가
            x = roomlist.index(btnText)
            s = Seat(numlist[x], unablelist[x])
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
        key = self.sender().text()[0]
        unable = self.sender().text()[-5:-3]
        self.switch_window.emit(key, int(unable.lstrip()))

# 방의 상세정보를 보여주는 창의 GUI 코드
class Reservation(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room, unable):
        super().__init__()

        temp = roomlist[::]

        #임시코드
        for i in roomlist:
            if room == i[0]:
                name = temp.index(i)
                unableseat = random.sample(range(1, numlist[name]+1), unable)
                title = QLabel(i[2:], self)
                temp.pop(name)
                print(unableseat)
        # Display Window
        

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        seatLayout = QGridLayout()

        buttonGroups = {
            '1.미래관 449호': {'buttons': miraeList, 'columns': 8},
            '2.법학관 스터디카페': {'buttons': bubhakList, 'columns': 15},
            '3.복지관 311호': {'buttons': bokjioneList, 'columns': 5},
            '4.복지관 303호': {'buttons': bokjithreeList, 'columns': 6},
            '5.복지관 306호': {'buttons': bokjisixList, 'columns': 8},
            '6.복지관 317호': {'buttons': bokjisevenList, 'columns': 19},
        }

        mainLayout.addWidget(title, 0, 0)
        for label in buttonGroups.keys():
            if room ==label[0]:
                r = 0; c = 0
                buttonPad = buttonGroups[label]
                for btnText in buttonPad['buttons']:
                    button = Button(btnText, self.buttonClicked)
                    if button.text() == ' ':
                        button.setStyleSheet('QToolButton {background-color: black; color: black;}')
                    elif int(button.text()) in unableseat:
                        button.setStyleSheet('QToolButton {background-color: rgb(138,238,64); color: black;}')
                    else:
                        button.setStyleSheet('QToolButton {background-color: rgb(250,86,86); color: black;}')
                    seatLayout.addWidget(button, r, c)
                    c += 1
                    if c > buttonPad['columns']:
                        c = 0;
                        r += 1

        mainLayout.addLayout(seatLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 2, 1)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

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
 
    def show_Seat(self, room, unable):
        self.seat = Reservation(room, unable)
        self.seat.switch_window.connect(lambda: self.show_main('seat'))
        self.main.close()
        self.seat.show()

# 버튼 클릭시 서버로 신호를 보내는 클래스
class ClientHandler:
    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.client = TcpClientAsync(reader, writer)

    async def funcAHandler(self):
        pass # 버튼 누르면 seat 변수 계산

    async def funcBHandler(self):
        pass # 버튼 누르면 'X' 표시 뜨게 함

    async def startHandle(self):
        while True:
            await self.funcAHandler()
            await self.funcBHandler()

async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    clientHandler = ClientHandler(reader, writer)
    await clientHandler.startHandle()

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
#    https://wikidocs.net/33768
#    https://wikidocs.net/38038
#    https://stackoverflow.com/questions/46693355/pyqt5-typeerror-signal-has-0-arguments-but-1-provided
#    https://janeljs.github.io/python/sample()/
