global kud
global otk
global usi
global text
global name

import mysql.connector
from mysql.connector import Error


import mysql.connector
def baza (kud,otk,usi,text,name):
  conn = mysql.connector.connect(
         user='root',
         password='lizard',
         host='localhost',
         database='tele')


  cur = conn.cursor()

  print('id ользователя=',usi)

  print('kud в базе=',kud)
  print('otk в базе=',otk)
  print('text в базе  ',text)
  print('name  базе  ',name)
  
  
  
  query = "INSERT INTO posts(usid,id_gr_otk,id_gr_kud,post,naneusid) VALUES(%s,%s,%s,%s,%s)"
 
  args = (usi,otk,kud,text,name)
  print(name)
  print(args)
  cur.execute(query,args)

  
  query = "SELECT  * FROM posts WHERE naneusid LIKE \"%" + name+"%\""
  cur.execute(query,name)
  data = cur.fetchall()
  print('data=',data)        
  for row in data:
            print(row)         

  conn.commit()  
  
  conn.close()
 




 
