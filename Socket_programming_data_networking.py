import socket
host= '127.0.0.1'
port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
data=s.recv(1024)
ele=data.decode()
print(ele)
string="HELLO dcosta.aa\n"
s.send(string.encode())
print(string)
while True:
    data=s.recv(1024)
    ele=data.decode()
    print(ele)
    x=ele.split(' ',1)
    if (x[0]=="DONE"):
        s.close()
        break
    elif(x[0]=="MATH"):
        answer=eval(x[1])
       # print(int(answer))
        m="ANSWER"+" "+str(int(answer))+"\n"
        s.send(m.encode())
        print(m)
    else:
        print("unexpected output")
        break
