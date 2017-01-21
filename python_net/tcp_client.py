import socket

tar_host = 'www.google.com'
tar_prot = 80

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((tar_host,tar_prot))

client.send(b'GET / HTTP/1.1\r\nHost:google.com\r\n\r\n')

response = client.recv(4096)

print (response)
