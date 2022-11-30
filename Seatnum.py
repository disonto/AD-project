#남은 좌석 알려주는 파일
from threading import Thread
from socket import *
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from Room import Room

port = 8080

class Seat():
    def __init__(self, ent, una):
        # ent값과 una값은 각 학습 공간별 정보를 불러올 예정
        self.entireSeatNum = ent
        self.unableSeatNum = una
        if ent - una < 0:
            self.Seatnum = "Error; 전체 좌석수가 이미 누군가 사용중인 좌석수보다 적습니다." # 임시코드; 나중엔 이 메세지 창으로 띄워야
        self.Seatnum = ent-una

    def getSeatNum(self):
        return self.entireSeatNum

    def getUnableSeatNum(self):
        return self.unableSeatNum

    def getLeftSeatNum(self):
        return self.Seatnum

# 서버 소켓 구현
class ServerSocket(QObject):
    
    update_signal = pyqtSignal(tuple, bool)
    recv_signal = pyqtSignal(str)
    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.bListen = False
        self.clients = []
        self.ip = []
        self.threads = []
        
        # 임시방편으로 변수 설정
        self.takenSeat = Seat.getUnableSeatNum = Room.미래관449호.__len__()
        self.entireSeat = Seat.getSeatNum = Room.미래관449호.__len__()
        Seat.getLeftSeatNum = self.entireSeat - self.takenSeat
        
    def __del__(self):
        self.stop()
        
    def start(self, ip, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        
        try:
            self.server.bind((ip, port))
        except Exception as e:
            print('Bind Error : ', e)
            return False
        else:
            self.bListen = True
            self.t = Thread(target=self.listen, args=(self.server,))
            self.t.start()
            print('Server Listening...')
            
        return True
    
    def stop(self):
        self.bListen = False
        if hasattr(self, 'Server'):
            self.server.close()
            print('Server Stop!')
            
    def listen(self, server):
        while self.bListen:
            server.listen(5)
            try:
                client, addr = server.accept()
            except Exception as e:
                print('Accept() Error : ', e)
                break
            else:
                self.clients.append(client)
                self.ip.append(addr)                
                self.update_signal.emit(addr, True)                
                t = Thread(target=self.receive, args=(addr, client))
                self.threads.append(t)
                t.start() 

        self.server.close()
 
    def receive(self, addr, client):
        while True:            
            try:
                recv = client.recv(1024)                
            except Exception as e:
                print('Recv() Error :', e)                
                break
            else:                
                msg = str(recv, encoding='utf-8')
                if msg:
                    self.recv_signal.emit(msg)
                    print('[RECV]:', addr, msg)
 
    def send(self, msg):
        try:
            for c in self.clients:
                c.send(msg = Room.미래관449호.__len__(self))
        except Exception as e:
            print('Send() Error : ', e)