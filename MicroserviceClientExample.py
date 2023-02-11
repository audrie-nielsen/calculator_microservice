#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# ZeroMQ uses bytes to communicate data.
# When sending a request to the server, encode the value as byte in 1 of 2 ways:

# Option 1: socket.send(('#').encode('ASCII'))
socket.send(('-6.9').encode('ASCII'))
res = socket.recv()

# Option 2: socket.send((b"#")
socket.send(b"4.0")
res = socket.recv()

socket.send(('2.8').encode('ASCII'))
res = socket.recv()

socket.send(b"POP")  # Send request "POP" to let the server know you'd like to retrieve the last calculation
res = socket.recv().decode('ASCII')  # To convert server response back into a string
print(res)

socket.send(('POP').encode('ASCII'))
res = socket.recv().decode('ASCII')
print(res)

socket.send(b"POP")
res = socket.recv().decode('ASCII')
print(res)