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
 def roomview():
	print("Do you want to see room type available : Enter 1 for yes :")
	ch=int(input("enter your choice:"))
	if ch==1:
    	sql="select * from room"
    	mycursor.execute(sql)
	rows=mycursor.fetchall()
	for x in rows:
    	print(x)
 def roomrent(): 
	print ("We have the following rooms for you:-")
	print ("1. SINGLE ROOM---->rs 1000 PN\-")
	print ("2. DOUBLE ROOM---->rs 1500 PN\-")
	print ("3. TWIN ROOM---->rs 1800 PN\-")
	print ("4. SINGLE DELUXE ROOM---->rs 2500 PN\-")
	print ("5. DOUBLE DELUXE ROOM---->rs 3000 PN\-")
	print ("6. LUXURY A ROOM---->rs 4500 PN\-")
	print ("7. LUXURY B ROOM---->rs 4000 PN\-")
	print ("8. FAMILY A---->rs 2000 PN\-")
	print ("9. FAMILY B---->rs 3000 PN\-")
	print ("10. FAMILY C---->rs 4000 PN\-")
	x=int(input("Enter Your Choice Please->"))
	n=int(input("For How Many Nights Did You Stay:"))	
	if(x==1):
    	s=1000*n
    	print ("you have opted SINGLE ROOM")
    	print ("your bill is :- ",s)
        	elif (x==2):
    		print ("you have opted DOUBLE ROOM")
    		s=1500*n
    		print ("your bill is :- ",s)
	elif (x==3):
    		print ("you have opted TWIN ROOM")
    		s=1800*n
    		print ("your bill is :- ",s)
	elif (x==4):
    		print ("you have opted SINGLE DELUXE ROOM")
    		s=2500*n
    		print ("your bill is :- ",s)
	elif (x==5):
    		print ("you have opted DOUBLE DELUXE ROOM")
    		s=3000*n
    		print ("your bill is :- ",s)
	elif (x==6):
    		print ("you have opted LUXURY A ROOM")
    		s=4500*n
    		print ("your bill is :- ",s)
	elif (x==7):
    		print ("you have opted LUXURY B ROOM")
    		s=4000*n
    		print ("your bill is :- ",s)
	elif (x==8):
    		print ("you have opted FAMILY A")
    		s=2000*n
    		print ("your bill is :- ",s)
elif (x==9):
    		print ("you have opted FAMILY B")
    		s=3000*n
    		print ("your bill is :- ",s)
    	elif (x==10):
    		print ("you have FAMILY C")
    		s=4000*n
    		print ("your bill is :- ",s)
else:
    		print ("please choose a room")
    		print ("your room rent is =",s,"\n")
 def restaurentmenuview():
	print("Do you want to see menu available : Enter 1 for yes :")
	ch=int(input("enter your choice:"))
	if ch==1:
    		sql="select * from food;"
    		mycursor.execute(sql)
    		rows=mycursor.fetchall()
	for x in rows:
    		print(x)
 def orderitem():
  	print("Do you want to see menu available : Enter 1 for yes :")
	ch=int(input("enter your choice:"))
	if ch==1:
    		sql="select * from food"
    		mycursor.execute(sql)
    		rows=mycursor.fetchall()
    		print("do you want to purchase from above list:enter your choice:")
   d=int(input("enter your choice:"))
        if(d==1):
        	print("you have ordered tea")
        	a=int(input("enter quantity"))
        	s=5*a
        	print("your amount for tea is :",s,"\n")
    elif (d==2):
        	print("you have ordered coffee")
        	a=int(input("enter quantity"))
        	s=10*a
        	print("your amount for coffee is :",s,"\n") 	
  elif(d==3):
        	print("you have ordered colddrink")
        	a=int(input("enter quantity"))
        	s=20*a
        	print("your amount for colddrink is :",s,"\n")
     elif(d==4):
        	print("you have ordered samosa")
        	a=int(input("enter quantity"))
        	s=10*a
        	print("your amount for samosa is :",s,"\n")
       elif(d==5):
        	print("you have ordered sandwich")
        	a=int(input("enter quantity"))
        	s=50*a
        	print("your amount for sandwich is :",s,"\n")
    elif(d==6):
        	print("you have ordered dhokla")
        	a=int(input("enter quantity"))
        	s=30*a
        	print("your amount for dhokla is :",s,"\n")
    elif(d==7):
        	print("you have ordered kachori")
        	a=int(input("enter quantity"))
        	s=10*a
        	print("your amount for kachori is :",s,"\n")
    elif(d==8):
        	print("you have ordered milk")
        	a=int(input("enter quantity"))
        	s=20*a
            print("your amount for kachori is :",s,"\n")
    elif(d==9):
        	print("you have ordered noodles")
        	a=int(input("enter quantity"))
        	s=50*a
        	print("your amount for noodles is :",s,"\n")
    elif(d==10):
        	print("you have ordered pasta")
        	a=int(input("enter quantity"))
        	s=50*a
        	print("your amount for pasta is :",s,"\n")
    elif (d==11):
        	print("you have ordered pani puri")
        	a=int(input("enter quantity"))
        	s=25*a
        	print("your amount for pani puri is :",s,"\n")
    elif(d==12):
        	print("you have ordered chole-bhature")
        	a=int(input("enter quantity"))
        	s=60*a
        	print("your amount for chole-bhature is :",s,"\n")
    elif(d==13):
        	print("you have ordered masala dosa")
        	a=int(input("enter quantity"))
        	s=50*a
        	print("your amount for masala dosa is :",s,"\n")
    elif(d==14):
        	print("you have ordered dahi-vada")
        	a=int(input("enter quantity"))
      	  s=70*a
        	print("your amount for dahi-vada is :",s,"\n")
     elif(d==15):
        	print("you have ordered sambhar-vada")
        	a=int(input("enter quantity"))
        	s=80*a
        	print("your amount for sambar-vada is :",s,"\n")
    elif(d==16):
        	print("you have ordered matar paneer")
        	a=int(input("enter quantity"))
        	s=70*a
        	print("your amount for matar paneer is :",s,"\n")
    elif(d==17):
        	print("you have ordered shahi paneer")
        	a=int(input("enter quantity"))
        	s=80*a
        	print("your amount for shahi paneer is :",s,"\n")
    elif(d==18):
        	print("you have ordered palak paneer")
        	a=int(input("enter quantity"))
        	s=60*a
        	print("your amount for palak paneer is :",s,"\n")
    elif(d==19):
        		print("you have ordered chapatis")
        		a=int(input("enter quantity"))
        		s=10*a
        		print("your amount for chapatis is :",s,"\n")
    	elif(d==20):
        		print("you have ordered bharva-baigan")
        		a=int(input("enter quantity"))
        		s=70*a
        		print("your amount for bharva-baigan is :",s,"\n")
    elif (d==21):
        	print("you have ordered tangdi-kabab")
        	a=int(input("enter quantity : "))
        	s=225*a
        	print("your amount for tangdi-kabab is :",s,"\n")
    elif(d==22):
        	print("you have ordered egg-curry")
        	a=int(input("enter quantity"))
        	s=125*a
        	print("your amount for egg_curry is :",s,"\n")
    elif(d==23):
        	print("you have ordered biryani")
        	a=int(input("enter quantity"))
        	s=60*a
        	print("your amount for biryani is :",s,"\n")
    elif(d==24):
        	print("you have ordered salad")
        	a=int(input("enter quantity"))
        	s=30*a
        	print("your amount for salad is :",s,"\n")
    elif(d==25):
        	print("you have ordered poha")
        	a=int(input("enter quantity"))
            s=30*a
        	print("your amount for poha is :",s,"\n")
    elif(d==66):
        	print("you have ordered jalebi_phaphda")
        	a=int(input("enter quantity"))
        	s=50*a
        	print("your amount for jalebi_phaphda is :",s,"\n")
    elif(d==27):
        	print("you have ordered manchurian")
        	a=int(input("enter quantity"))
        	s=70*a
        	print("your amount for manchurian is :",s,"\n")
    elif(d==28):
        	print("you have ordered paneer manchurian")
        	a=int(input("enter quantity"))
        	s=90*a
        	print("your amount for paneer manchurian is :",s,"\n")
    elif(d==29):
            print("you have ordered chicken manchurian")
        	a=int(input("enter quantity"))
        	s=140*a
        	print("your amount for chicken manchurian is :",s,"\n")
    elif(d==30):
        	print("you have ordered pav-bhaji")
        	a=int(input("enter quantity"))
        	s=40*a
        	print("your amount for pav-bhaji is :",s,"\n")       
    	else:
        	print("please enter your choice from the menu")
 
def laundarybill():
	print("Do you want to see rate for laundry : Enter 1 for yes :")
	ch=int(input("enter your choice:"))
	
	if ch==1:
    	     sql="select * from laundry"
    	      mycursor.execute(sql)
    	     rows=mycursor.fetchall()
    	     for x in rows:
	        print(x)
	
	y=int(input("Enter Your number of clothes->"))
	z=y*10
	print("your laundry bill:",z,"\n")
 
def ratings():  
	rating=[10,10,15,35,30]
	stars=["1 STAR","2 STAR","3 STAR","4 STAR","5 STAR"]
	expl=[0,0,0.1,0.1,0.1]
    plt.pie(rating,labels=stars,autopct="%1.1f%%",explode=expl,shadow=True)
	plt.title("Hotel Ratings")
	plt.show()
 
def Menuset():  
	print("enter 1: To enter customer data")
	print("enter 2 : To view roomtype")
	print("enter 3 : for calculating room bill")
	print("enter 4 : for viewing restaurant menu")
	print("enter 5 : for restaurant bill")
	print("enter 6 : for laundry bill")
	print("enter 7 : for ratings")  
  
	try:
    	userinput=int(input("please select an above option:"))
	except ValueError:
    	exit("\n hi that's not a number") 
 
	if(userinput==1):
    	    registercust()	
	elif(userinput==2):
    	     roomview()	
	elif(userinput==3):
    	     roomrent()	
	elif(userinput==4):
    	     restaurentmenuview()	
	elif(userinput==5):
    	     orderitem()	
	elif(userinput==6):
    	     laundarybill()	
	elif(userinput==7):
    	     ratings()    	
	else:
    	     print("enter correct choice")
Menuset()
 
def runagain(): 
	runagn=input("\n want to run again y/n:")
	while(runagn.lower()=='y'):
        if(platform.system()=="windows"):
        	print(os.system('cls'))
    	else:
        	print(os.system('clear'))
    	Menuset()
    	runagn=input("\n want to run again y/n:")
runagain()

