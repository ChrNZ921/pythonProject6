import asyncio
from Regex import decoder_message
from BaseDeDonnees import base_de_donnees

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        d= decoder_message(message)
        if d != None :
            base_de_donnees(d)
            print('Send: {!r}'.format(message))



async def main():

    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '51.210.112.107', 12345)

    async with server:
        await server.serve_forever()

asyncio.run(main())
