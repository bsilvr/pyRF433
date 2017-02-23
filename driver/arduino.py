
import serial


class Arduino433:

    def __init__(self, port=None, baudrate=9600):
        self.baudrate = baudrate
        self.set_port(port)

    def set_port(self, port):
        self.port = port
        self.comm = serial.Serial(self.port, self.baudrate)

    def open(self):
        self.comm.open()

    def close(self):
        self.comm.close()

    def send(self, msg):
        self.comm.write(msg)

    def receive(self, size):
        return self.comm.read(size)
