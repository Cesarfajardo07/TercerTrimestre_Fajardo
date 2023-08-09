import mysql.connector

comercializadora = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce_fajardo_cesar"
)
#print(type(db))

cursor=comercializadora.cursor()
cursor.execute('SHOW DATABASES')
#print(type(cursor))
for dbs in cursor:
     print(dbs)

# for n in cursor:
#     print(n)
print('--------------------')
cursor.execute("SHOW TABLES")
for n in cursor:
    print(n)

cursor.execute("""INSERT INTO usuarios (id_usuario,id_rol,id_vendedor,nombre,clave,email) VALUES(12,8,4,'Laura Forero','1111','laura14f@gmail.com') """)
comercializadora.commit()
cursor.execute('select * from usuarios')
for ap in cursor:
     print(ap[0])
     print(ap[1])
     print(ap[2])
     print(ap[3])
