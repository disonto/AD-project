# 좌석 서버 구현
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import Seatnum
import sys
import socket

port = 8080

# 서버 GUI 구성
class CWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.s = Seatnum.ServerSocket(self)
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('서버')
         
        # 서버 설정 부분
        ipbox = QHBoxLayout()
 
        gb = QGroupBox('서버 설정')
        ipbox.addWidget(gb)
 
        box = QHBoxLayout()
 
        label = QLabel('Server IP')
        self.ip = QLineEdit(socket.gethostbyname(socket.gethostname()))
        box.addWidget(label)
        box.addWidget(self.ip)
 
        label = QLabel('Server Port')
        self.port = QLineEdit(str(port))
        box.addWidget(label)
        box.addWidget(self.port)
 
        self.btn = QPushButton('서버 실행')
        self.btn.setCheckable(True)        
        self.btn.toggled.connect(self.toggleButton)
        box.addWidget(self.btn)      
 
        gb.setLayout(box)
 
        # 접속자 정보 부분
        infobox = QHBoxLayout()
        gb = QGroupBox('좌석')
        infobox.addWidget(gb)
 
        box = QHBoxLayout() 
 
        self.guest = QTableWidget()             
 
        box.addWidget(self.guest)
        gb.setLayout(box)
 
        # 전체 배치
        vbox = QVBoxLayout()
        vbox.addLayout(ipbox)       
        vbox.addLayout(infobox)
        self.setLayout(vbox)
         
        self.show()
 
    def toggleButton(self, state):
        if state:
            ip = self.ip.text()
            port = self.port.text()
            if self.s.start(ip, int(port)):
                self.btn.setText('서버 종료')                
        else:
            self.s.stop()
            self.btn.setText('서버 실행')
 
    def sendMsg(self):
        pass
 
    def closeEvent(self, e):
        self.s.stop()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())