# coding:utf-8
import os
import sys
import hashlib
import socket
import time
import threading

# FlyVar Server Compment


class Server():
    def __init__(self, host='127.0.0.1', port=18012, maxlisten=30):
        self.host = host
        self.port = port
        self.maxlisten = maxlisten

    def Runing(self):
        try:
            os.mkdir('flying')
        except:
            pass
        self.__connections = list()
        self.__client = list()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.maxlisten)
        print('[Server]Start Server')
        print('[Server]Runing on ' + self.host + ':' + str(self.port))
        self.__connections.clear()
        self.__client.clear()
        while True:
            self.client_, self.addr_ = self.socket.accept()
            print(self.client_)
            print('Connections：' + str(self.addr_))
            self.client.recv()
    
    def __clientTreading(self,connectId):
        print("A new processing thread has been opened")


    def CreateDatabase(self, Databasename, Databaseuser, Databasepassword):
        self.databasenameokstr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k',
                                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.databasenameok = False
        self.databasenamestrok = False
        for i in str(Databasename):
            for a in self.databasenameokstr:
                if a == i:
                    self.databasenamestrok = True
                    break
            if self.databasenamestrok == False:
                self.databasenameok = False
            elif self.databasenamestrok == True:
                self.databasenameok = True
        if self.databasenameok == False:
            print('DatabaseNamee：' + Databasename + ' wrongful')
            print('Only English letters can be used as the database name of flyvar')
            return False
        sha1Hash = hashlib.sha1(Databasepassword.encode("utf8"))
        database = {
            "header": {
                "Databasename": Databasename,
                "Databaseuser": Databaseuser,
                "Databasepassword": sha1Hash.hexdigest()
            },
            "table": [],
            "commit": [],
            "log": [],
        }
        try:
            os.mkdir('flying')
        except:
            pass
        if os.path.exists('./flying/' + Databasename + '.flying'):
            print('Duplicate database name')
            return False
        with open('./flying/' + Databasename + '.flying', 'w+', encoding="utf-8") as f:
            f.write(str(database))
        print('Created in relative path ./flying')
        return True


# FlyVar Client Compment

class Database():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.statecode = False

    def connect(self, host, port, name, user, password):
        try:
            self.socket.connect((host, port))
            print('Successfully connected')
            self.socket.send(str({'type': 'login', 'database': name,
                                  'user': user, 'password': password}).encode('utf-8'))
        except:
            print('Connection failed, please check the network or address')
