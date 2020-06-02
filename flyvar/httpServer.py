from flask import *
import os
import sys
import time
import hashlib
import random

httpServer = Flask(__name__)
client = list()
token = list()

@httpServer.route('/api/contect',methods=['POST'])
def apiContect():
    if os.path.exists('./database/' + request.form['database'] + '.fvdata'):
        with open('./database/' + request.form['database'] + '.fvdata','wb+') as fh:
            for i in fh.readline():
                if dict(eval(i))['type'] == 'init':
                    initline = dict(eval(i))
                    break
            if initline['database'] == request.form['database'] and initline['password'] == request.form['password']:
                tokenValue = hashlib.sha1(random.randint(1,900000))
                token.append(tokenValue.hexdigest())
                client.append({'token':tokenValue.hexdigest,'database':request.form['database']})
                return str({'type':'loginok','token':tokenValue.hexdigest()})
            else:
                return str({'type':'error','state':'user-nomatch'})


    else:
        return str({'type':'error','state':'not-found'})
    