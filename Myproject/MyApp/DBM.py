import pymysql as p

def getConntion():
    username="root"
    password=""
    serverName="localhost";
    dbName="Student"
    return p.connect(serverName,username,password,dbName)

    
def addStudent(t):
    db=getConntion()
    sql="insert into student values(%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
