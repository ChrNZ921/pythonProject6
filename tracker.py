import asyncio
import json
import sqlite3
from datetime import datetime

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()

        print('Send: {!r}'.format(message))

        # Ajouter les données à la base de données SQLite
        # con = sqlite3.connect('mabase.db')
        # cur = con.cursor()
        # cur.execute("CREATE TABLE IF NOT EXISTS matable (user , date, data )")
        # cur.execute("INSERT INTO matable VALUES (?, ?, datetime('now'))", (str(self.user), str(données["data"])))
        # con.commit()
        # con.close()

async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '51.210.112.107', 12345)

    async with server:
        await server.serve_forever()

asyncio.run(main())
