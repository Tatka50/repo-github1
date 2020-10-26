import mysql.connector
from mysql.connector import Error


import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='lizard',
         host='localhost',
         database='tele')


cur = conn.cursor()

query = ("SELECT * FROM users")

cur.execute(query)

for (n,usid) in cur:
  print(usid, '       ', n)


query = ("SELECT * FROM posts")

cur.execute(query)

for (usid,id_gr_otk,id_gr_kud,post,nameusid) in cur:
  print(usid,'  ',id_gr_otk,'   ',id_gr_kud,'  ',post,'  ',nameusid)
  


query = ("SELECT  * FROM posts,users WHERE post='#ggg'")

cur.execute(query)
for (post) in cur:
  print(post)

l=12
query = ("SELECT n FROM users WHERE usid=12")
cur.execute(query)
print('n=',n)
n1=n





  
#create_users = """
#INSERT INTO
#   'users' ( 'n','usid' )
#VALUES
 #(14, 'Totochka')
#"""

#query = "INSERT INTO users(n,usid) VALUES(%s,%s)"
#args = ('Totochka','14')

#cur.execute(query,args)



for (usid) in cur:
  print(usid)

us=21
idotk=56789
idkud=54321
pos='#mmm'
print('n1=',n1)
query = "INSERT INTO posts(usid,id_gr_otk,id_gr_kud,post,naneusid) VALUES(%s,%s,%s,%s,%s)"
args = (us,idotk,idkud,pos,n1)
print(args)
cur.execute(query,args)


query = ("SELECT  * FROM posts WHERE naneusid='Сема'")

cur.execute(query)
for (naneusid) in cur:
  print(post)



conn.commit()  







conn.close()
 



conn.close()
 
