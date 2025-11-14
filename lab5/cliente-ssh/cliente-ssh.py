import paramiko
import socket
HOST_IP = "c4-s1" 
PUERTO = 22
VERSION_A_FALSIFICAR = "SSH-2.0-OpenSSH_?"
USUARIO = "prueba"
PASSWORD = "prueba"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST_IP, PUERTO))
transport = paramiko.Transport(sock)
transport.local_version = VERSION_A_FALSIFICAR
transport.start_client()
transport.auth_password(username=USUARIO, password=PASSWORD)