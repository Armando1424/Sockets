import socket as s

cliente = s.socket(s.AF_INET, s.SOCK_DGRAM)
nombre = input("Cual es tu nombre? ")
cliente.sendto(nombre.encode("ascii"), ("127.0.0.1", 2500))

msg, addr = cliente.recvfrom(1024)
print("Mensaje: ", msg," recibido por: ",addr) 

cliente.close()