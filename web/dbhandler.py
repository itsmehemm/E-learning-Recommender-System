import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="diskuss")        
cur = db.cursor()
idx = 1
parentid = 1
create = "2016-07-31"
title = "How does database indexing work?"
body = "Given that indexing is so important as your data set increases in size can someone explain how does indexing works at a database agnostic level?"
cur.execute("INSERT INTO posts VALUES(%s, %s, %s, %s, %s)" % (idx, parentid, create, title, body))

