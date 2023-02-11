REQUIREMENTS TO USE:
This program uses PyZMQ, instructions for installing PyZMQ can be found at: https://zeromq.org/get-started/?language=python#

REQUESTING DATA:
This program saves data that is sent to it into an array until that data is requested back.
In order to send the data to the server to be saved into the array. Data sent to the server must be sent as bytes, to convert strings to bytes and send it to the server there are two options:

   OPTION A:
   socket.send(('-6.9').encode('ASCII'))
   
   OPTION B:
   socket.send(b"-6.9")

After data has been sent to the server and the server has successfully saved the data to the array, a request can be made to return the last data that was added to the array (pop the stack). When this is done the data should be converted back into string. 
Similarly to above, this can implemented in two ways:

  OPTION A:
  socket.send(('POP').encode('ASCII'))

  OPTION B:
  socket.send(b"POP")
  
RECEIVING DATA:
When the server responds to the request, the response will be sent back in bytes. If the data is wanted as a string, it can be decoded as:
  
  res = socket.recv().decode('ASCII')
 
This is important when you are receiving the integer back from the server.
When you send data to the server to be placed in the array, the server will respond back with 'b"Result added to the stack"'. You don't need to decode this unless you would like to print it out as a string. 

An example of a full call to the program is as follows:

  socket.send(b"4.0")
  
  res = socket.recv()
  
or...

  socket.send(('POP').encode('ASCII'))
  
  res = socket.recv().decode('ASCII')



