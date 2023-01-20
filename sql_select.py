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

result = select("nome, cpf", "alunos",)

print(result[0])
