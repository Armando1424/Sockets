import socket as s

sc = s.socket(s.AF_INET, s.SOCK_STREAM)
#s.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1)
#host = sc.gethostname()
host = "10.32.100.145"
port = 2000
sc.connect((host, port))

msg = sc.recv(1024)
print("Mensaje recibido: {}".format(msg.decode("ascii")))
num1 = 7
num2 = 3
msgVals = "Gracias servidor ,{},{}".format(num1,num2)
sc.send(msgVals.encode("ascii"))

msg = sc.recv(1024)
msg,valor = msg.decode("ascii").split(",")
print("{} : {}".format(msg,valor))

sc.close()