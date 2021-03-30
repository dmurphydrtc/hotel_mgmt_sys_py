import matplotlib.pyplot as plt
import platform
import mysql.connector
global z

mydb = mysql.connector.connect(user='root', password='mysql', host='localhost', database='nj')
mycursor=mydb.cursor()
 
  
def registercust():

  L=[]
	cid=input("CID:")
	L.append(cid)
  	name=input("Enter Name:")
	L.append(name)
 	addr=input("Enter Address:")
	L.append(addr)
 	phone_no=input("Enter Phone Number:")
	L.append(phone_no)
 	with_family=input("Enter are you with Family:")
	L.append(with_family)
	
  cust=(L)
     sql="insert into custdata(cid,name,addr,phone_no,with_family)values(%s,%s,%s,%s,%s)"
	mycursor.execute(sql,cust)
	
  mydb.commit()
    print("Entry Successful")
