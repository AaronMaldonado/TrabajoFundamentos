# -*- coding: utf-8 -*-

import os
import sqlite3

def create_db(db_name):
	
    conn = sqlite3.connect(db_name)
    
    c= conn.cursor()
    
    query = """CREATE TABLE productos (id_producto integer PRIMARY KEY AUTOINCREMENT,
                                       nombre text,especificacion text,formato text,tipo text,precio integer,stock integer)"""
      
    c.execute(query)
    
    
    
if __name__ == "__main__":
    db_name = 'BDProductos.db'
    if not os.path.exists(db_name):
        create_db(db_name)
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()


    query = "INSERT INTO productos(id_producto,nombre,especificacion,formato,tipo,precio,stock) VALUES (?,?,?,?,?,?,?)"	
    
    p1 =["001", "Pulpa de Aji","Caja de bolsas","10x1","Salsa","10000","100"]
    p2 =["002", "Pulpa de Aji","Caja de bolsas","24x200","Salsa","12000","50"]
    p3 =["003", "Pulpa de Aji","Caja de frascos","24x240","Salsa","15000","60"]
    p4 =["004", "Salsa de Aji","Caja de bolsas","10x1","Salsa","8000","100"]
    p5 =["005", "Salsa de Aji","Caja de bolsas","24x200","Salsa","10000","50"]
    p6 =["006", "Salsa de Aji","Caja de frascos","24x240","Salsa","12000","60"]
    p7 =["007", "Condimento de Mostaza","Caja de bolsas","10x1","Salsa","13000","100"]
    p8 =["008", "Condimento de Mostaza","Caja de bolsas","24x200","Salsa","15000","150"]
    p9 =["009", "Condimento de Mostaza","Caja de frascos","24x240","Salsa","18000","160"]
    p10 =["010", "Ketchup","Caja de bolsas","10x1","Salsa","9000","100"]
    p11 =["011", "Ketchup","Caja de bolsas","24x200","Salsa","11000","50"]
    p12 =["012", "Ketchup","Caja de frascos","24x240","Salsa","12000","60"]

    p13 =["013", "Aceitunas Huasco","Caja de bolsas","6x1","Encurtido","20000","100"]
    p14=["014", "Aceitunas Huasco","Balde","Granel","Encurtido","15000","50"]
    p15=["015", "Aceituna Sevillana","Caja de bolsas","6x1","Encurtido","22000","60"]
    p16=["016", "Aceituna Sevillana","Balde","Granel","Encurtido","17000","60"]
    
      
    p17 =["017", "Pickles finos","Caja de bolsas","6x1","Encurtido","5000","100"]
    p18 =["018", "Pickles finos","Caja de bolsas","24x200","Encurtido","4000","200"]
    p19 =["019", "Salsa Americana","Caja de bolsas","6x1","Encurtido","5000","100"]
    p20 =["020", "Salsa Americana","Caja de bolsas","24x200","Encurtido","4000","200"]
    p21 =["021", "Chucrut","Caja de bolsas","6x1","Encurtido","5000","100"]
    p22 =["022", "Chucrut","Caja de bolsas","24x200","Encurtido","4000","200"]
    p23 =["023", "Cebollitas Perla","Caja de bolsas","6x1","Encurtido","5000","100"]
    p24 =["024", "Cebollitas Perla","Caja de bolsas","24x200","Encurtido","4000","200"]
    p25 =["025", "Pepinillos Cocktail","Caja de bolsas","6x1","Encurtido","5000","100"]
    p26 =["026", "Pepinillos Cocktail","Caja de bolsas","24x200","Encurtido","4000","200"]
    p27 =["027", "Pickles finos","Caja de bolsas","6x1","Encurtido","5000","100"]
    p28 =["028", "Pickles finos","Caja de bolsas","24x200","Encurtido","4000","200"]


    
    
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p1)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p2)    
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p3)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p4)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p5)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p6)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p7)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p8)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p9)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p10)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p11)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p12)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p13)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p14)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p15)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p16)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p17)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p18)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p19)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p20)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p21)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p22)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p23)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p24)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p25)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p26)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p27)
    c.execute("INSERT INTO productos VALUES (?,?,?,?,?,?,?)",p28)


    conn.commit()

    	
    
