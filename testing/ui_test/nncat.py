import socket
import time

def ncat(hostname, port, content):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((hostname, port))
        s.sendall(content)
        s.shutdown(socket.SHUT_WR)
        s.close()
        return True

    except ConnectionRefusedError:
        return False

def checkConnection(HOSTNAME,PORT,MAX_TIME):
    count=0
    while ncat(HOSTNAME, PORT, b'') == False:
        time.sleep(1)
        if count == MAX_TIME:
            print(f"Connection timeout for {HOSTNAME} at port {PORT}")
            raise TimeoutError()
        count+=1
    return True