import pymysql as p

def getConntion():
    username="root"
    password=""
    serverName="localhost";
    dbName="dj23july"
    return p.connect(serverName,username,password,dbName)

    
def addUser(t):
    db=getConntion()
    sql="insert into user01 values(%s,%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllUser():
    db=getConntion()
    sql="select * from  user01"
    cr=db.cursor()
    cr.execute(sql)
    ul=cr.fetchall()
    db.commit()
    db.close()
    return ul

def deleteUser(id):
    db=getConntion()
    sql="delete from user01 where id=%s"
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectUserById(id):
    db=getConntion()
    sql="select * from  user01 where id=%s"
    cr=db.cursor()
    cr.execute(sql,id)
    ul=cr.fetchall()
    db.commit()
    db.close()
    return ul[0]

def updateUser(t):
    #for i in t:
        #print()
    db=getConntion()
    sql= f"update user01 set name ='{t[1]}', Contact = '{t[2]}', email = '{t[3]}', salary = '{t[4]}' where id = '{t[0]}'"
    cr=db.cursor()
    cr.execute(sql)
    db.commit()
    db.close()

