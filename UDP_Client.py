import socket

target_host = "0.0.0.0"
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"AAABBBCCC", (target_host,target_port))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()