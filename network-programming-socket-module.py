

# MATH SERVER - server will receive any math expresion, evalute it and send the result back to client

import socket

s = socket.socket() # creating connection socket object,using this only servr will accept there request and and will senn the respnse
s.bind(("localhost", 5050)) # Define on which ip:port this service will run? give that. binding ip address and port, so if any request comming on this ip and port keep on listning for it, bind take argument in Tuple.
print("Math Server Is Running...")
s.listen(5)

while True:
    t = s.accept() #accepting the request and stroing in t, t is a tuple which has multiple information about client server
    client_server = t[0] # tuple at index 0, client ip is stored, we storing it in client_server variable. 
    b = client_server.recv(1024) # reciving math expresion of maximum 1024 bytes data from client
    expr = b.decode() # data received in bytes, so decoding and converting it into str
    result = eval(expr)# evaluting the math expresion and stroing in 'result' its digit
    result = str(result) # again converting digits into str, becase we have to sent thre result to vlient into byte format
    client_server.send(result.encode)#encoding result into byte and sending it to client server


# MATH CLIENT - Sends Math Expresion to Math Server for evalution, and will get the response back. 
import socket

s =socket.socket()
expr = input("input any math expresion: ")
s.connect("localhost", 5050) # making conection request, as math server is listning on this ip and port already
print("Connected to Math server, Evaluating your expresion !")
s.send(expr.encode()) # converting expersion in bytes and sending to Math Sever
b = s.recv(1024) # receving result from Math Server in bytes
print(b.decode) # decoding result and print it. 





