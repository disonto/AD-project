#남은 좌석 알려주는 파일
import asyncio
import pickle

PACKET_SIZE = 256

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

# async를 이용한 비동기적 TCP 통신 수행 클래스
class TcpClientAsync():
    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.__reader = reader
        self.__writer = writer

    # 데이터를 비동기적으로 수신합니다.
    async def getDataAsync(self, packetSize: int = PACKET_SIZE):
        packet = b''

        dataSize = int.from_bytes(await self.__reader.read(packetSize), 'little')

        while dataSize > 0:
            packet += await self.__reader.read(min(dataSize, packetSize))
            dataSize -= packetSize

        return pickle.loads(packet)

    # 데이터를 비동기적으로 송신합니다.
    async def sendDataAsync(self, data, packetSize: int = PACKET_SIZE):
        packet = pickle.dumps(data)

        await self.__writer.drain()
        self.__writer.write(len(packet).to_bytes(packetSize, 'little'))

        while packet:
            await self.__writer.drain()
            self.__writer.write(packet[:packetSize])
            packet = packet[packetSize:]
