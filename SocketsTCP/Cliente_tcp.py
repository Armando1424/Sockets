import socket as s

sc = s.socket(s.AF_INET, s.SOCK_STREAM)
#s.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1)
#host = sc.gethostname()
host = "localhost"
port = 2000
sc.connect((host, port))
msg = sc.recv(1024)
print("Mensaje recibido: {}".format(msg.decode("ascii")))
sc.send("Gracias servidor ".encode("ascii"))
sc.close()