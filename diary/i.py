from pybricks.hubs import PrimeHub
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

hub = PrimeHub()
server = BluetoothMailboxServer()
m = TextMailbox('command', server)

print("Waiting for connection...")
server.wait_for_connection()
print("Connected!")

while True:
    if m.read_ready():
        command = m.read()
        if command == "go":
            hub.speaker.beep()
