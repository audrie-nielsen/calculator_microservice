# Requirements/Setup
This program uses PyZMQ, instructions for installing PyZMQ can be found at: https://zeromq.org/get-started/?language=python#

# Connecting to the Server:
Including the following at the top of your code to connect to the server through sockets (see MicroserviceClientExample.py for an example):
> socket = context.socket(zmq.REQ)
> socket.connect("tcp://localhost:5555")

# Requesting Data:
Data sent to the server must be sent as bytes, to convert strings to bytes and send it to the server there are two options:
> OPTION A:
> socket.send(('-6.9').encode('ASCII'))

> OPTION B:
> socket.send(b"1+4/2-9")

To request last equation and result added to the array (pop the stack), data will be sent back as a JSON.
> OPTION A:
> socket.send(('POP').encode('ASCII'))

> OPTION B:
> socket.send(b"POP")

# Receiving Data:
When the server responds to the request, the response will be sent back as a JSON. 
> res = socket.recv_json()
> print(res)

> > Example Output: {"equation": "7 + 4 * 3", "result": "19"}
  
# Where to find more information
For a more in depth explanation see Wiki Page 'Implementing this Microservice'.
For a UML Sequence Diagram for this program see Wiki Page 'UML Sequence Diagram'.
