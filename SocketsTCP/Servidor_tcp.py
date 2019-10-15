import socket as s

ss = s.socket(s.AF_INET, s.SOCK_STREAM)
#s.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1)
#host = ss.gethostname()
host = "localhost"
port = 2000
ss.bind((host, port)) 
ss.listen(5)
while True:
    cs, addr = ss.accept()
    print("Conexion exitosa desde %s" %str(addr))
    msg = "Gracias por conectarte " + "\r\n"
    cs.send(msg.encode('ascii'))
    msgc = cs.recv(1024)
    print("Mensaje recibido del cliente: {}".format(msgc.decode("ascii")))
cs.close()