# -*- coding: utf-8 -*-

import os
import sqlite3

def create_db(db_name):
	
    conn = sqlite3.connect(db_name)
    
    c= conn.cursor()
    
    query = """CREATE TABLE cliente (id_cliente integer PRIMARY KEY AUTOINCREMENT,
                                       nombre text,rut text,direccion text,telefono text,empresa text,rut_empresa text,correo text)"""
      
    c.execute(query)
    
    
    
if __name__ == "__main__":
    db_name = 'BDClientes.db'
    if not os.path.exists(db_name):
        create_db(db_name)
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()


    query = "INSERT INTO cliente(id_cliente,nombre,rut,direccion,telefono,empresa,rut_empresa,correo) VALUES (?,?,?,?,?,?,?,?)"	
    
    p1 =["001", "Juan Perez","12345678-k","Cochrane 72, Temuco","0303456","Supermercado Juanito","000-102","juanperez@asd.cl"]

    c.execute("INSERT INTO cliente VALUES (?,?,?,?,?,?,?,?)",p1)


    conn.commit()

    	
    
