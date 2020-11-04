global kud
global otk
global usi
global text

import mysql.connector
from mysql.connector import Error


import mysql.connector
def baza (kud,otk,usi,text):
  conn = mysql.connector.connect(
         user='root',
         password='lizard',
         host='localhost',
         database='tele')

  print('id ользователя=',usi)
  print('kud в базе=',kud)
  print('otk в базе=',otk)
  print('text в базе  ',text)
  
  us=str(usi)
  print('us=',us)
  cur = conn.cursor()
  query = "SELECT  * FROM users WHERE usid LIKE \"%" + us+"%\""
  
  cur.execute(query,us)
  data = cur.fetchall()
  print(data)
  nam=data[0]
  nam1=nam[0]

  print(data)
  print("полученное из базы имя", nam1)

  
  
  query = "INSERT INTO posts(usid,id_gr_otk,id_gr_kud,post,naneusid) VALUES(%s,%s,%s,%s,%s)"
  args = (usi,otk,kud,text,nam1)
  print(args)
  cur.execute(query,args)




  conn.commit()  







  conn.close()
 



  conn.close()
 
