#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sqlite3

con = sqlite3.connect('BDProductos.db')
#con=connect()
cursor=con.cursor()

print "La base de datos inicio correctamente"    

cursor.execute("Delete from productos where id_producto=002")
con.commit()
print "Registros borrados:" , con.total_changes


cursor.execute("Select id_producto,nombre,especificacion,formato,tipo,precio,stock from productos")


for i in cursor:
    print "Codigo=",i[0]
    print "Nombre del producto=",i[1]
    print "Especificacion=",i[2]
    print "Formato=",i[3]
    print "Tipo=",i[4]
    print "Precio=",i[5]
    print "Stock=",i[6], "\n"

print "Operacion realizada"

con.close()

