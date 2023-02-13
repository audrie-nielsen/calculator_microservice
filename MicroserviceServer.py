import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

arr = []

while True:
    #  Waits for next request from client
    req = socket.recv()
    print("Received request: %s" % req)
    time.sleep(1)

    #  If request is "POP", server sends back a JSON containing the last pushed equation and result
    if req == b"POP":
        if arr == []:
            resJSON = {"equation": "empty", "result": "empty"}
            res = json.dumps(resJSON)
            socket.send_json(res)
        else:
            result = arr[-1].decode("ASCII")
            arr.pop()
            equation = arr[-1].decode("ASCII")
            arr.pop()

            resJSON = {"equation": equation, "result": result}
            res = json.dumps(resJSON)
            socket.send_json(res)
    # Else, adds the request data to the array
    else:
        arr.append(req)
        socket.send(b"Result added to the stack")
