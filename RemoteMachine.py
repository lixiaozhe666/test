import socket
ip = ""
port =0
def ServerListen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET 表示计算机之间的通信 ，AF_INET表示进程间的通信
    host_name = socket.getfqdn(socket.gethostname())
    local_ip = socket.gethostbyname(host_name)
    s.bind((local_ip))
    s.listen(1)
    while True:
        global ip
        global port
        sock, addr = s.accept()
        ip =addr[0]
        port = addr[1]
        if ip !="":
            print("connect server ip is %s"% ip)
            break

# def Client():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((ip,port))
ServerListen()