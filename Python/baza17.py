global kud
global otk
global usi
global text

import mysql.connector
from mysql.connector import Error


import mysql.connector
def baza (usi,kud,otk,text):
  conn = mysql.connector.connect(
         user='root',
         password='lizard',
         host='localhost',
         database='tele')


  cur = conn.cursor()
  query = ("SELECT n * FROM users WHERE usid=usi")
  n1=n




  query = "INSERT INTO posts(usid,id_gr_otk,id_gr_kud,post,naneusid) VALUES(%s,%s,%s,%s,%s)"
  args = (usi,otk,kud,text,n1)
#print(args)
  cur.execute(query,args)




  conn.commit()  







  conn.close()
 



  conn.close()
 
