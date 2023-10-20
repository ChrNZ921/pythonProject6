# Client
import asyncio
import json

class EchoClientProtocol(asyncio.Protocol) :
    def __init__(self, on_con_lost) :
        self.transport = None
        self.on_con_lost = on_con_lost
        self.username = input("Entrez votre nom : ")

    def connection_made(self, transport) :
        self.transport = transport
# Send the username  to the server
        self.send_message('user', self.username)

# Send the message to the server
        message = input(" Entrez un message : ")
        self.send_message('mess', message)

    def data_received(self, data) :
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc) :
        print('The server closed the connection')
        self.on_con_lost.set_result(True)

    def send_message(self, type, data = None):
        dict = {'type' : type,
                'data' : data}
        paquet = json.dumps(dict)
        self.transport.write(paquet.encode())
        print('sent: {!r}'.format(paquet))

async def ping(protocol):
        while True:
            # envoie du ping
            protocol.send_message('ping')
            # Attente
            await asyncio.sleep(5)

async def main() :
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    transport, protocol = await loop.create_connection(
        lambda : EchoClientProtocol(on_con_lost),
        '127.0.0.1', 8888)

    # Création d'une tâche asynchrone ping
    task1 = asyncio.create_task(ping(protocol))

    try :
        await on_con_lost
    finally :
        task1.cancel()
        transport.close()

asyncio.run(main())
