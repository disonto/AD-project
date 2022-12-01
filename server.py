# 좌석 서버 구현
import asyncio
from main import handler

HOST = '127.0.0.1'
PORT = 8282

# 서버 구현
async def main():
    server = await asyncio.start_server(handler, HOST, PORT)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())