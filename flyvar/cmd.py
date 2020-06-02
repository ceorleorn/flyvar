# coding:utf-8
from flask import *
import os
import hashlib
import time
import _thread
import random
import huepy
import traceback


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
            if not os.path.exists("./" + cmd + '.fvdata'):
                cmd1 = input('Password:')
                hash = hashlib.sha256(cmd1.encode('utf-8'))
                with open('./' + cmd + '.fvdata', 'wb+') as fh:
                    fh.write(
                        str({'database': cmd, 'password': hash.hexdigest()}).encode('utf-8'))
                print(huepy.good("Database created successfully:" + cmd))
            else:
                print(
                    huepy.bad("The same database name already exists in the directory"))
        else:
            print(huepy.bad("Database name must be English lowercase"))
    elif run == "run"