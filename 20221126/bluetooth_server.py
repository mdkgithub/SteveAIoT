import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("",1))
server_sock.listen(1)

client_sock, client_info=server_sock.accept()
print("Accepted connection from", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            print("Received", data)
except OSError:
    pass

print("Disconnected.")

client_sock.close()
server_sock.close()
print("All done")




"""
importbluetooth
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("",1))
server_sock.listen(1)
client_sock,client_info=server_sock.accept()
print("Acceptedconnectionfrom",client_info)
try:
whileTrue:
data=client_sock.recv(1024)
ifnotdata:
break
print("Received",data)
exceptOSError:
pass
print("Disconnected.")
client_sock.close()
server_sock.close()
print("Alldone.")
"""