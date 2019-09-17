import socket

class MySocket():
    def connetServer(self, server_ip, server_port):
        # 建立连接:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_ip, int(server_port)))
        return "OK"