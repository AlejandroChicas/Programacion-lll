import mysql.connector

conexion1=mysql.connector.connect(host="localhost",
                                  user= "root",
                                  passwd="" ,
                                  database="DB1")

cursor1=conexion1.cursor()
sql="insert articulo(descripcion, precio) values (%s,%s)"
datos=("Bocina",5)
cursor1.execute(sql,datos)
conexion1.commit()
conexion1.close()
print("Se han guardado correctamente")