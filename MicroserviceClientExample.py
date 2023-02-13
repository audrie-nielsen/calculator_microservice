#   Connects REQ socket to tcp://localhost:5555
import zmq
context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# ZeroMQ uses bytes to communicate data.
# When sending a request to the server, encode the value as byte in 1 of 2 ways:

# Option 1: socket.send('[request]'.encode('ASCII'))
socket.send('16/4'.encode('ASCII'))
res = socket.recv()

# Option 2: socket.send((b"[request]")
socket.send(b"4.0")
res = socket.recv()

socket.send(b"3 + 6 / 2 - 9")
res = socket.recv()

socket.send('3'.encode('ASCII'))
res = socket.recv()

socket.send('7 + 4 * 3'.encode('ASCII'))
res = socket.recv()

socket.send('19'.encode('ASCII'))
res = socket.recv()

socket.send(b"POP")  # Send request "POP" to retrieve the last equation and result pushed
res = socket.recv_json() # Use socket.recv_json() to receive the equation and result as a JSON
print(res)

socket.send('POP'.encode('ASCII'))
res = socket.recv_json()
print(res)

socket.send(b"POP")
res = socket.recv_json()
print(res)
