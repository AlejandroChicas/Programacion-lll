import mysql.connector

class Articulos:
    def abrir(self):
        conexion1 = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="",
                                            database="ugb01")

        return conexion1

    def guardar(self, datos):
        cone = self.abrir()
        cursor=cone.cursor()
        sql="insert into productos (nombre, precio) values (%s, %s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.fetchall()


    def consulta(self, datos):
        cone = self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from productos where codigo=%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self, datos):
        cone = self.abrir()
        cursor=cone.cursor()
        sql="select nombre, precio from productos)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.fetchall()


    def baja (self, datos):
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "delete from productos where codigo=%s"
            cursor.execute(sql, datos)
            cone.commit()
            cone.close()
            return cursor.rewcount() # retonar la cantidad de filas afectadas


    def Modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "UPDATE productos SET nombre = %s, precio = %s WHERE codigo = %s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rewcount()
