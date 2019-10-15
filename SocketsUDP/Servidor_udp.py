import socket as s

servidor = s.socket(s.AF_INET, s.SOCK_DGRAM)
servidor.bind(("127.0.0.1",2500))

msg, addr = servidor.recvfrom(1024)
print("Mensaje ", msg," recibido por: ",addr)

ok = "Bienvenido " + str(msg)
servidor.sendto(ok.encode("ascii"), ("127.0.0.1", 2500))   

servidor.close()