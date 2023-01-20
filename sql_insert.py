from optparse import Values
import MySQLdb

host = "localhost"
user = "aplicacao"
password = "123456"
db = "escola_curso"
port=3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if (where): 
        query = query + " WHERE " + where
    
    c.execute(query)
    return c.fetchall()

def insert(values, table, fields=None):
    global c, con

    querry = "Insert INTO " + table
    if (fields):
        querry = querry + " (" + fields + ") "
    querry = querry + " VALUES " + ",". join(["(" + v + ")" for v in values])

    c.execute(querry)
    con.commit() #commit garante que a execução aconteça, seja inserida no banco de dados

values = [
        "DEFAULT, 'Augusto Pedro', '1998-04-22', 'Av das Pedras, 123', 'Divinópolis', 'MG', '03541878954'",]
       
insert(values, "alunos")  
print(select("*", "alunos"))        
