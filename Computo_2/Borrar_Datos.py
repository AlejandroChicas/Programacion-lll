import mysql.connector

# Conexión a la base de datos
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="DB1"
)

cursor1 = conexion1.cursor()

# Mostrar datos actuales
cursor1.execute("SELECT id, descripcion, precio FROM articulo")
print("Datos actuales en la tabla:")
for datos in cursor1:
    print(datos)

# ======== BORRAR REGISTRO =========
# Cambia este número por el id que quieremos borrar
id_borrar = 48
sql = "DELETE FROM articulo WHERE id = %s"
val = (id_borrar,)
cursor1.execute(sql, val)

# Confirmar cambios
conexion1.commit()
print(f"Se borró el registro con id = {id_borrar}")

# Verificar datos después de borrar
cursor1.execute("SELECT id, descripcion, precio FROM articulo")
print("Datos después de borrar:")
for datos in cursor1:
    print(datos)

# Cerrar conexión
conexion1.close()
print("Listo Articulo Borrado Correctamente")