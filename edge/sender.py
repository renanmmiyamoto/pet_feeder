import time
import datetime
from connection import Connection

class Sender:
    def __init__(self, port, baud, datetime):
        self.port = port
        self.baud = baud
        self.conn = Connection(port=port, baud=baud).connect()
        self.datetime = datetime

    def alimentar(self):
        if(self.conn != 0):
            if (datetime.datetime.now() >= self.datetime):
                self.conn.write('open'.encode())
                self.datetime = datetime.datetime.now() + datetime.timedelta(microseconds=60)
        else:
            time.sleep(30)
            self.conn = Connection(port=self.port, baud=self.baud).connect()
            self.alimentar
