import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

calcArray = []

while True:
    #  Waits for next request from client
    req = socket.recv()
    print("Received request: %s" % req)

    time.sleep(1)

    #  If the request is "POP", the server sends back the last result that was PUSHed
    if req == b"POP":
        res = calcArray[-1]
        calcArray.pop()
        socket.send(res)
    else:
        calcArray.append(req)
        socket.send(b"Result added to the stack")
