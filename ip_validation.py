import socket

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False

print valid_ip('10.10.20.30')
print valid_ip('999.10.20.30')
print valid_ip('gibberish')
