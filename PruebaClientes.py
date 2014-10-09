#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sqlite3

con = sqlite3.connect('BDClientes.db')
#con=connect()
cursor=con.cursor()

print "La base de datos inicio correctamente"    

cursor.execute("Delete from cliente where id_cliente=0")
con.commit()
print "Registros borrados:" , con.total_changes


cursor.execute("Select id_cliente,nombre,rut,direccion,telefono,empresa,rut_empresa,correo from cliente")


for i in cursor:
    print "Codigo=",i[0]
    print "Nombre del cliente=",i[1]
    print "Rut=",i[2]
    print "Direccion=",i[3]
    print "Telefono=",i[4]
    print "Empresa=",i[5]
    print "Rut de la empresa=",i[6]
    print "Correo del cliente=",i[7], "\n"

print "Operacion realizada"

con.close()

