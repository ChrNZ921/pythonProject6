# Client
import asyncio
import json


class EchoClientProtocol(asyncio.Protocol) :
    def __init__(self, on_con_lost) :
        self.on_con_lost = on_con_lost
        self.username = input("Entrez votre nom : ")

    def connection_made(self, transport) :
# Send the username  to the server
        dict = { 'type': 'user',
                 'data': self.username}
        paquet = json.dumps(dict)
        transport.write(paquet.encode())




# Send the message to the server
        message = input(" Entrez un message : ")
        dict = {'type' : 'mess',
                'data' : message}
        paquet = json.dumps(dict)
        transport.write(paquet.encode())
        print('Data sent: {!r}'.format(paquet))

    def data_received(self, data) :
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc) :
        print('The server closed the connection')
        self.on_con_lost.set_result(True)


async def main() :
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    transport, protocol = await loop.create_connection(
        lambda : EchoClientProtocol(on_con_lost),
        '127.0.0.1', 8888)



    try :
        await on_con_lost
    finally :
        transport.close()

asyncio.run(main())
