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

cursor.execute("""INSERT INTO users (id,role_id,seller_id,name,email,password)VALUES (1,23,30,'Felipe Guzman','felipe23@gmail.com','F123G') """)
comercializadora.commit()
cursor.execute('select * from users')
for ap in cursor:
     print(ap[0])
     print(ap[1])
     print(ap[2])
     print(ap[3])
