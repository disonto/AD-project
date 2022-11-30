#남은 좌석 알려주는 파일
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