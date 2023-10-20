# Serveur
import asyncio
import json
from datetime import datetime

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        #decode la str json en dic
        données = json.loads(message)
        #in dic on vérifie la valeur type
        if données['type'] == "user":
            #action qui correspond
            #sauvegarde le nom d'utilisateur
            self.user = données['data']

        elif données['type'] == "mess":
            print('Data received: {!r}'.format(message))

        elif données['type'] == "ping":
            self.date = datetime.now()

        print('Send: {!r}'.format(message))
        self.transport.write(data)

async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
