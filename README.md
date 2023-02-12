REQUIREMENTS TO USE:
This program uses PyZMQ, instructions for installing PyZMQ can be found at: https://zeromq.org/get-started/?language=python#

REQUESTING DATA:
For the server to save data into an array until that data is requested back.

   OPTION A:
   socket.send(('-6.9').encode('ASCII'))
   
   OPTION B:
   socket.send(b"-6.9")

To request that the server return the last data that was added to the array (pop the stack). When this is done the data should be converted back into string. POP EQUATION returns the last pushed equation and POP RESULT returns the last pushed result.

  OPTION A:
  socket.send(('POP EQUATION').encode('ASCII'))

  OPTION B:
  socket.send(b"POP RESULT")
  
RECEIVING DATA:
When the server responds to the request, the response will be sent back in bytes. If the data is wanted as a string, it can be decoded as:
  
  res = socket.recv().decode('ASCII')
  
For a more in depth explanation see Wiki Page 'Implementing this Microservice'.
For a UML Sequence Diagram for this program see Wiki Page 'UML Sequence Diagram'.
