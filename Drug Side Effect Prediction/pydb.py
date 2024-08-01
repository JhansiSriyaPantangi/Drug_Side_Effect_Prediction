import pymysql
con=pymysql.connect(host='localhost',port=3306,database='dirtyminds',user="root",password="root")
print(con)
cur = con.cursor()
result = cur.execute("show databases")
for i in cur:
    print(i)
con.close()
