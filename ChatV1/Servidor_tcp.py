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
    msg = "Manda dos valores separados por comas" + "\r\n"
    cs.send(msg.encode('ascii'))

    msgc = cs.recv(1024)
    msg,num1,num2 = msgc.decode("ascii").split(",")
    print("{}: {} + {}".format(msg, num1, num2))
    res = int(num1) + int(num2)
    msg = "Resultado ,{}".format(res)
    cs.send(msg.encode('ascii'))
cs.close()