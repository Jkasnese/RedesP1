import asyncio

class ClienteLeve:
    """ Classe ClienteLeve define um protocolo de comunicação leve, que não sobrecarregue a rede dos sensores.
        Atributos:
            Mensagem
            Loop
            Transporte"""

    def __init__(self, mensagem, loop):
        self.mensagem = mensagem 
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Enviado:', self.menssagem)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print("Received:", data.decode())

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Socket closed, stop the event loop")
        loop = asyncio.get_event_loop()
        loop.stop()

loop = asyncio.get_event_loop()
message = "Hello World!"
connect = loop.create_datagram_endpoint(
    lambda: EchoClientProtocol(message, loop),
    remote_addr=('127.0.0.1', 9999))
transport, protocol = loop.run_until_complete(connect)
loop.run_forever()
transport.close()
loop.close()
