import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

resArray = []
equArray = []

while True:
    #  Waits for next request from client
    req = socket.recv()
    print("Received request: %s" % req)

    time.sleep(1)

    #  If request is "POP EQUATION" or "POP RESULT", server sends back last result PUSHed to that stack
    if req == b"POP EQUATION":
        if equArray == []:
            socket.send(b"The equation backlog is currently empty.")
        else:
            res = equArray[-1]
            equArray.pop()
            socket.send(res)
    elif req == b"POP RESULT":
        if resArray == []:
            socket.send(b"The result backlog is currently empty.")
        else:
            res = resArray[-1]
            resArray.pop()
            socket.send(res)
    else:  # Checks if request is an equation or a result
        str = req.decode('ASCII')
        if ' + ' in str or ' - ' in str or ' / ' in str or ' * ' in str:
            equArray.append(req)
            socket.send(b"Result added to the equation stack")
        else:
            resArray.append(req)
            socket.send(b"Result added to the result stack")
