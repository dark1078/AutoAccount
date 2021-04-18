import sqlite3   #enable control of an sqlite database


DB_FILE="static/data/accs.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops


db.commit() #save changes
db.close()  #close database