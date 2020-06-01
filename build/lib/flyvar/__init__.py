# coding:utf-8

import os
import sys
import hashlib
import socket
import time


#FlyVar Server Compment

class Server():
    def __init__(self, host=socket.gethostname(), port=8012, maxlisten=30):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(maxlisten)

    def CreateDatabase(Databasename, Databaseuser, Databasepassword):
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
            print('数据名称：' + Databasename + ' 并不合法')
            print('只能用英文字母作为FlyVar的数据库名称')
            return False
        sha1Hash = hashlib.sha1(Databasepassword)
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
            os.mkdir('flyvar')
        except:
            pass
        if os.path.exists('./flyvar/' + Databasename + '.flyvar'):
            print('数据库名称已在' + os.getcwd() + '文件夹中重复')
            return False
        with open('./flyvar/' + Databasename + '.flyvar','r',encoding="utf-8") as f:
            f.write(str(database))
        print('数据库已在' + os.getcwd() + '/flyvar/' + Databasename + '.flyvar 创建，但并没有开始运行')
        return True

