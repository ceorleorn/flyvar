# coding:utf-8
from .httpServer import httpServer
import os
import hashlib
import time
import _thread
import random
from flask import *
import huepy
import traceback
import requests

print(huepy.good('Welcome use Flyvar'))


'''
Hello, I'm glad you're here. 
This is the source of flyvar. If you want to learn, 
I'd like to. But if you want to change, please follow license, 
thank you
'''

class Database():
    def __init__(self):
        self.stateCode = False
    def init(self,url,database,password):
        password = hashlib.sha256(password)
        rv = requests.post(url,data={'database':database,'password':password.hexdigest()})
        rv = dict(eval(rv.text))



def cmd():
    # coding:utf-8
    
    print(huepy.good('Welcome to the flyvar command tool, enter "help" for help'))
    while True:

        cmd = input('anything:')
        if cmd == "help":
            print('')
            print(huepy.info('Existing instructions:'))
            print('')
            print(huepy.info('createdatabase:Create Database'))
            print('')
            print(huepy.info('createdatabase:Create Database'))
            print('')
        elif cmd == "createdatabase":
            cmd = input('DatabaseName:')
            if cmd.isalpha() and cmd.islower():
                try:
                    os.mkdir('database')
                except:
                    pass
                if not os.path.exists("./database/" + cmd + '.fvdata'):
                    cmd1 = input('Password:')
                    hash = hashlib.sha256(cmd1.encode('utf-8'))
                    with open('./database/' + cmd + '.fvdata', 'wb+') as fh:
                        fh.write(
                            str({'type': 'init', 'database': cmd, 'password': hash.hexdigest()}).encode('utf-8'))
                    print(huepy.good("Database created successfully:" + cmd))
                else:
                    print(
                        huepy.bad("The same database name already exists in the directory"))
            else:
                print(huepy.bad("Database name must be English lowercase"))
        elif cmd == "run":
            httpServer.run(port=3112)
