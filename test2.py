import flyvar

db = flyvar.Database()

db.connect('127.0.0.1',18012,'test','test','test')
db.createTABLE('One',flyvar.Models({'name':'name','Pubshing':''},'name'))