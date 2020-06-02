# coding:utf-8
import os
import sys
import hashlib
import socket
import time
import _thread
import random
import huepy

print(huepy.good('Welcome use Flyvar'))

# FlyVar Server Compment


class Server():
    def __init__(self, host='127.0.0.1', port=18012, maxlisten=30):
        self.host = host
        self.port = port
        self.maxlisten = maxlisten
        self.__connections = list()
        self.__client = list()
        self.__token = list()

    def Runing(self):
        try:
            os.mkdir('flying')
        except:
            pass

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.maxlisten)
        print(huepy.info('[Server]Start Server'))
        print(huepy.info('[Server]Runing on ' + self.host + ':' + str(self.port)))
        self.__connections.clear()
        self.__client.clear()
        self.__token.clear()
        while True:
            self.client_, self.addr_ = self.socket.accept()
            print('Connections：' + str(self.addr_))
            _thread.start_new_thread(self.__clientTreading, (self.client_,))

    def __clientTreading(self, ConnectionClient):

        self.__connections.append(ConnectionClient)
        print(huepy.info("A new processing thread has been opened"))
        affair = dict(eval(ConnectionClient.recv(9000000)))
        if affair['type'] == 'login':
            if os.path.exists('./flying/' + affair['database'] + '/__init__.flying') and dict(eval(open('./flying/' + affair['database'] + '/__init__.flying', 'r', encoding="utf-8").read()))['name'] == affair['database']:
                if dict(eval(open('./flying/' + affair['database'] + '/__init__.flying', 'r', encoding="utf-8").read()))['user'] == affair['user'] and dict(eval(open('./flying/' + affair['database'] + '/__init__.flying', 'r', encoding="utf-8").read()))['password'] == affair['password']:
                    self.sha256Hash = hashlib.sha256(
                        str(random.randint(1, 3000)).encode('utf-8'))
                    self.__token.append(self.sha256Hash.hexdigest())
                    ConnectionClient.send(
                        str({'type': 'token', 'token': self.sha256Hash.hexdigest()}).encode('utf-8'))
                else:
                    ConnectionClient.send(
                        str({'type': 'error', 'state': '1304'}).encode('utf-8'))
            else:
                ConnectionClient.send(
                    str({'type': 'error', 'state': '404'}).encode('utf-8'))
        else:
            ConnectionClient.send(
                str({'type': 'error', 'state': '403'}).encode('utf-8'))
            return False

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
            print(huepy.bad('DatabaseNamee：' + Databasename + ' wrongful'))
            print(huepy.bad('Database can only be created in lowercase'))
            return False
        sha256Hash = hashlib.sha256(Databasepassword.encode("utf8"))
        try:
            os.mkdir('flying')
        except:
            pass
        try:
            os.mkdir('flying/' + Databasename)
        except:
            pass
        if os.path.exists('./flying/' + Databasename + '.flying'):
            print('Duplicate database name')
            return False
        with open('./flying/' + Databasename + '/__init__.flying', 'w+', encoding="utf-8") as f:
            f.write(str({
                'name': Databasename,
                'user': Databaseuser,
                'password': sha256Hash.hexdigest()
            }))
        print(huepy.info('Created in relative path ./flying'))
        return True


# FlyVar Client Compment

class Database():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.statecode = False
        self.hashobject = hashlib.sha256()
        self.Token = ''

    def connect(self, host, port, name, user, password):
        self.hashobject.update(password.encode('utf-8'))
        try:
            self.socket.connect((host, port))
            print(huepy.run('Successfully connected'))
            self.socket.send(str({'type': 'login', 'database': str(name),
                                  'user': str(user), 'password': self.hashobject.hexdigest()}).encode('utf-8'))
        except:
            print(huepy.bad('Connection failed, please check the network or address'))
        returnValue = dict(eval(self.socket.recv(3012)))
        if returnValue['type'] == 'error':
            if returnValue['state'] == '404':
                print(huepy.bad('Connection failed, please check the address or databasename'))
                return False
            elif returnValue['state'] == '1304':
                print(huepy.bad('Connection failed, please check the username or password'))
                return False
            else:
                print(huepy.bad('Connection failed'))
                return False
        else:
            returnValue['token']
