#남은 좌석 알려주는 파일
class Seat():
    def __init__(self, m, n):
        # m값과 n값은 각 학습 공간별 정보를 불러올 예정
        self.entireSeatNum = n
        self.alreadyTaken = m
        if n < m:
            self.Seatnum = "Error; 전체 좌석수가 이미 누군가 사용중인 좌석수보다 적습니다."
        self.Seatnum = n-m

    def getSeatNum(self):
        return self.entireSeatNum

    def getAlreadyTakenSeatNum(self):
        return self.alreadyTaken

    def getLeftSeatNum(self):
        return self.Seatnum