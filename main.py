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
from Room import Room1, Room2, Room3, Room4, Room5, Room6
from Room import roomlist, numlist, Room_value
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
    switch_window = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Display Window

        # Digit Buttons
        roomLayout = QGridLayout()

        # 임시코드. 서버에서 실시간으로 불러오는 코드를 대체한다.
        unablelist = ['fIDILIX', 'wCCCXVII', 'wStudyCafe', 'wCCCIII', 'wCCCVI', 'wCCCXI']
        for entire in numlist:
            unablelist[numlist.index(entire)] = random.randint(1, entire)

        r = 0
        c = 0
        for btnText in roomlist:
            # 임시로 이미 찬 좌석 수는 입력 코드로 대체
            # i는 이게 끝나면 1씩 증가
            x = roomlist.index(btnText)
            s = Seat(numlist[x], unablelist[x])
            # 남은 자리수와 전체 자리수 모두 나오도록 함
            # 남은 자리수가 음수여도 뜨는 문제가 있음 - 수정 필요
            button = Button(btnText + " : " + str(s.getLeftSeatNum()) + "/" + str(s.getSeatNum()), self.Switch())
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
        key = button.text()
        self.switch_window.emit(key)

# 방의 상세정보를 보여주는 창의 GUI 코드
class Reservation1(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Display Window
        title = QLabel(self)

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mirae = Room1()
        mainLayout.addWidget(title, 0, 0)
        mainLayout.addLayout(mirae.miraeLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 6, 10)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # 버튼을 누르면 Controller에 신호보냄
    def quit(self):
        self.switch_window.emit()

class Reservation2(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room2):
        super().__init__()

        # Display Window
        title = QLabel(room2, self)

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        bubhak = Room2()
        mainLayout.addWidget(title, 0, 0)
        mainLayout.addLayout(bubhak.bubhakLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 9, 17)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # 버튼을 누르면 Controller에 신호보냄
    def quit(self):
        self.switch_window.emit()

class Reservation3(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room3):
        super().__init__()

        # Display Window
        title = QLabel(room3, self)

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        bokjione = Room3()
        mainLayout.addWidget(title, 0, 0)
        mainLayout.addLayout(bokjione.bokjioneLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 9, 7)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # 버튼을 누르면 Controller에 신호보냄
    def quit(self):
        self.switch_window.emit()

class Reservation4(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room4):
        super().__init__()

        # Display Window
        title = QLabel(room4, self)

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        bokjithree = Room4()
        mainLayout.addWidget(title, 0, 0)
        mainLayout.addLayout(bokjithree.bokjithreeLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 9, 8)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # 버튼을 누르면 Controller에 신호보냄
    def quit(self):
        self.switch_window.emit()

class Reservation5(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room5):
        super().__init__()

        # Display Window
        title = QLabel(room5, self)

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        bokjisix = Room5()
        mainLayout.addWidget(title, 0, 0)
        mainLayout.addLayout(bokjisix.bokjisixLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 15, 10)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Seat Reservation")

    # 버튼을 누르면 Controller에 신호보냄
    def quit(self):
        self.switch_window.emit()

class Reservation6(QWidget):
    switch_window = pyqtSignal()

    def __init__(self, room6):
        super().__init__()

        # Display Window
        title = QLabel(room6, self)

        # Digit Buttons
        quit_btn = Button("나가기", self.quit)
        # 좌석배치에 맞는 버튼을 생성

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        bokjiseven = Room6()
        mainLayout.addWidget(title, 0, 0)
        mainLayout.addLayout(bokjiseven.bokjisevenLayout, 1, 0)
        mainLayout.addWidget(quit_btn, 12, 20)
        
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
        self.login.switch_window.connect(self.show_main('login'))
        self.login.show()

    # 여기부분 고쳐야함;;;
    def show_main(self, text):
        self.main = Main()
        if '미래관' in text:
            self.main.switch_window.connect(self.show_Seat1())
        self.login.close()
        self.main.show()

    def show_Seat1(self):
        self.seat1 = Reservation1()
        self.main.close()
        self.seat1.show()
    
    def show_Seat2(self, room):
        self.seat2 = Reservation2(room)
        self.seat2.switch_window.connect(lambda: self.show_main('seat2'))
        self.main.close()
        self.seat2.show()
    
    def show_Seat3(self, room):
        self.seat3 = Reservation3(room)
        self.seat3.switch_window.connect(lambda: self.show_main('seat3'))
        self.main.close()
        self.seat3.show()
    
    def show_Seat4(self, room):
        self.seat4 = Reservation4(room)
        self.seat4.switch_window.connect(lambda: self.show_main('seat4'))
        self.main.close()
        self.seat4.show()
    
    def show_Seat5(self, room):
        self.seat5 = Reservation5(room)
        self.seat5.switch_window.connect(lambda: self.show_main('seat5'))
        self.main.close()
        self.seat5.show()
    
    def show_Seat6(self, room):
        self.seat6 = Reservation6(room)
        self.seat6.switch_window.connect(lambda: self.show_main('seat6'))
        self.main.close()
        self.seat6.show()

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
