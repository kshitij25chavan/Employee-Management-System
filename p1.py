from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import matplotlib.pyplot as plt
from matplotlib import pyplot



#mw programmig

def ad():
	mw.withdraw()
	aw.deiconify()

def up():
	mw.withdraw()
	uw.deiconify()
	
def de():
	mw.withdraw()
	dw.deiconify()
def vi():
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	con = None
	try:
		con = connect("ems.db")
		cursor = con.cursor()
		sql = "select * from emp "
		
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data :
			info += "id = " +str(d[0]) + "   "+ "name = " + str(d[1])+"    " + "sal = " + str(d[2]) +"\n"
		vw_st_data.insert(INSERT , info)
		
		
	except Exception as e:
		showerror("issue 1 " , e)
	finally:
		if con is not None:
			con.close()



def addlabels(x, y):
	for i in range(len(x)):
		plt.text(i,y[i],y[i])


def ch():
	
	con = None
	try:
		con=connect("ems.db")
		cursor=con.cursor()
		sql = "select name, sal from emp order by sal desc limit 5"
		cursor.execute(sql)
		data=cursor.fetchall()
		name=[]
		salary=[]
		for d in data:
			name.append(d[0])
			salary.append(d[1])

		plt.bar(name, salary, color=['red', 'yellow', 'black', 'blue', 'orange'],width=0.5)
		addlabels(name, salary)
		plt.xlabel("Name")
		plt.ylabel("Salary")
		plt.title("Salary Of Top 5 Employees")
		plt.show()

	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()


mw = Tk()
mw.title("E.M.S")
mw.geometry("700x700+100+100")

# creating icon
p1 = PhotoImage(file = 'icon.png')
  
# Setting icon of master window
mw.iconphoto(False, p1)
  
bg = PhotoImage( file = "ems.png")
  
# Show image using label
label1 = Label( mw, image = bg)
label1.place(x = 0,y = 0)



try :
	wa = "https://ipinfo.io/"
	response = requests.get(wa)
	
	data = response.json()
	
	cityname = data["city"]

except Exception as e :
	print("issue" , e)


try :
	a1="https://api.openweathermap.org/data/2.5/weather"
	a2="?q="+cityname
	a3="&appid="+"c6e315d09197cec231495138183954bd"
	a4 ="&units="+"metric"
	wa = a1+a2+a3+a4
	res = requests.get(wa)
	data = res.json()
	temp = data['main']['temp']
	
except Exception as e:
	print("issue" , e)

f = ("Arial" , 25 , "bold")
f1 = ("Arial" , 12 )
y=13
mw_btn_add = Button (mw , text = " Add Emp" , font = f , width = 13 , command = ad , bg='ivory2' )
mw_btn_view= Button (mw , text = "View Emp" , font = f , width = 13 , command = vi , bg = 'ivory3')
mw_btn_upd= Button (mw , text = "Update Emp" , font = f , width = 13  , command = up , bg='ivory4') 
mw_btn_del= Button (mw , text = "Delete Emp " , font = f , width = 13  , command = de , bg='seashell') 
mw_btn_chrt= Button (mw , text = "Chart" , font = f , width = 13 , command = ch , bg='honeydew2')
mw_lab_loc = Label(mw , text = "location : " , font = f )
mw_lab_locname = Label(mw ,  font = f , text=cityname )
mw_lab_tem = Label(mw , text = "temperature : " , font=f)
mw_lab_temvalue = Label(mw ,  font=f , text=temp )


mw_lab_temp = Label(mw , text = "temp : " , font = f )

mw_btn_add.pack(pady=y)
mw_btn_view.pack(pady=y)
mw_btn_upd.pack(pady=y)
mw_btn_del.pack(pady=y)
mw_btn_chrt.pack(pady=y)
mw_lab_loc.place(x= 20 , y=500)
mw_lab_locname.place(x=180 , y=500)
mw_lab_tem.place(x=380 , y=500)
mw_lab_temvalue.place(x=590 , y=500)



# AW PROG
def bac ():
	aw.withdraw()
	mw.deiconify()
def save1():
	con = None 
	try :
		con = connect("ems.db")
		cursor = con.cursor()
		sql = "insert into emp values ('%d' , '%s' , '%d')"

		
		tid = aw_ent_id.get()
		if (not(tid.isdigit())) or   tid=='0'  :
			raise Exception("Only Positive Integers Are Allowed in : ID")
		elif tid=='':
			raise Exception("Fill all the fields correctly")
		id = int(aw_ent_id.get())
		
		
		

		name = aw_ent_name.get()
		
		name = aw_ent_name.get()
		if not (name.isalpha()):
			raise Exception("'Name' : should contain letters only.")
		elif not len(name) > 1:
			raise Exception(" length of name should be more than 2 letters ")
		else:
			name = aw_ent_name.get()


		
		esal = aw_ent_sal.get()
		if not (esal.isdigit())  or esal=='0':
			raise Exception( "Salary : Should Contain  Only Positive Integers ")

		sal =int(aw_ent_sal.get())
		if sal < 8000 :
			raise Exception("Salary should be greater than 8000.")
		
		


		cursor.execute(sql%(id,name,sal))
		if cursor.rowcount == 1:  #to show data in vw
			con.commit()
			showinfo("success", "Record Added")
		else:
			showwarning("mistake", "record not added")

	except Exception as e:
		showerror("issue" , e)
	
	

	finally:
		if con is not None :
			con.close()
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_sal.delete(0,END)
		aw_ent_id.focus()
		




aw = Toplevel(mw)
aw.title("Add Employee")
aw.geometry("600x600+100+100")
aw.configure(bg="gold")



aw_lab_id = Label(aw, text = " Add Employee Id" , font = f , bg="gold")
aw_lab_id2 = Label(aw , text = "( NOTE : * Enter Only Positive Integers )" , font=f1 , bg = "gold")
aw_ent_id = Entry(aw , font = f)

aw_lab_name = Label(aw, text = "Add Employee Name" , font = f , bg="gold")
aw_lab_name2 = Label(aw , text = "(NOTE : * Enter Letters Only )" , font = f1 , bg="gold" )
aw_ent_name = Entry(aw , font = f)


aw_lab_sal = Label(aw, text = "Enter employee Salary" , font = f  , bg="gold")
aw_lab_sal2 = Label(aw , text = "( NOTE : * Enter Only Positive Integers greater than 8000 )" , font=f1 , bg = "gold")
aw_ent_sal = Entry(aw , font = f)

aw_btn_save = Button(aw, text = "SAVE" , font = f , command =save1 , bg = 'lawn green' ) 
aw_btn_back = Button(aw , text="BACK" , font = f , command = bac , bg = 'coral' )


aw_lab_id2.place(x=165 ,  y=55)
aw_lab_name2.place(x=180 , y=197)
aw_lab_sal2.place( x=100 ,y=330)
aw_lab_id.pack(pady=y)
aw_ent_id.pack(pady=y)
aw_lab_name.pack(pady=y)
aw_ent_name.pack(pady=y)
aw_lab_sal.pack(pady=y)
aw_ent_sal.pack(pady=y)
aw_btn_save.pack(pady=y)
aw_btn_back.pack(pady=y)
aw.withdraw()


 

#VW PROG
def bac2():
	vw.withdraw()
	mw.deiconify()

vw = Toplevel(mw)
vw.title("View Employee")
vw.geometry("600x600+100+100")
vw.configure(bg="PeachPuff2")

vw_st_data = ScrolledText(vw , width = 45 , height = 10 , font = f)
vw_st_data.pack(pady=y)

vw_btn_back = Button(vw , text = "BACK" , font = f , command = bac2 , bg = "coral")
vw_btn_back.pack(pady =y)
vw.withdraw()




#UW PROG


def save2 ():
	con = None
	try:
		con = connect("ems.db")
		cursor = con.cursor()
		sql = "update emp set name='%s' , sal='%d' where id='%d'"
	
		uid = uw_ent_id.get()
		if not(uid.isdigit()) or uid=='' or uid=='0':
			raise Exception("Only Positive Integers are Allowed in ID")

		id = int(uw_ent_id.get())
		
		
		
		name = uw_ent_name.get()
		if not (name.isalpha()) :
			raise Exception("Name should contain letters only.")
		elif name=='':
			raise Exception("no field shud be empty")
		elif not len(name) > 1:
			raise Exception(" length of name should be more than 2 letters ")
		else:
			name = uw_ent_name.get()

		
		esal = uw_ent_sal.get()
		if not (esal.isdigit())  or esal=='0':
			raise Exception( "Salary : Should Contain  Only Positive Integers ")

		sal =int(uw_ent_sal.get())
		if sal < 8000 :
			raise Exception("Salary should be greater than 8000.")
		
		
		cursor.execute(sql%(name,sal,id))
		if cursor.rowcount == 1:    
			con.commit()
			showinfo("Done" , "Record Updated successfully ")
		else:
			showwarning("OOPS" ,  "Only Added Data Can Update Here")
		
		
	except Exception as e:
		#showerror(" update issue " , "Only added data canbe Updated here ")
		con.rollback()
		showerror("issue 3" , e)
	finally :
		if con is not None:
			con.close()
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_sal.delete(0,END)
		uw_ent_id.focus()




def bac3():
	uw.withdraw()
	mw.deiconify()

uw = Toplevel(mw)
uw.title("Update Employee")
uw.geometry("700x600+90+90")
uw.configure(bg="lawn green")

uw_lab_id = Label(uw, text="Enter Employee ID", bg ="lawn green",font=f)
uw_lab_id2 = Label(uw , text = "( NOTE : * Enter Only Positive Integers )" , font=f1 , bg = "lawn green")
uw_ent_id = Entry(uw, font=f)
uw_lab_name = Label(uw, text="Enter Name",  bg="lawn green",font=f)
uw_lab_name2 = Label(uw , text = "(NOTE : * Enter Letters Only )" , font = f1 , bg="lawn green" )
uw_ent_name = Entry(uw, font=f)
uw_lab_sal = Label(uw, text="Enter Salary",  bg="lawn green",font=f)
uw_lab_sal2 = Label(uw , text = "( NOTE : * Enter Only Positive Integers greater than 8000 )" , font=f1 , bg = "lawn green")
uw_ent_sal = Entry(uw, font=f)
uw_btn_save = Button(uw, text="Save", font=f,  bg="cyan" , command = save2 )
uw_btn_back = Button(uw, text="Back", font=f, command = bac3,  bg="coral" )

uw_lab_id2.place(x=200 ,  y=55)
uw_lab_name2.place(x=250 , y=197)
uw_lab_sal2.place(x=150 ,y=330)
uw_lab_id.pack(pady=y)
uw_ent_id.pack(pady=y)
uw_lab_name.pack(pady=y)
uw_ent_name.pack(pady=y)
uw_lab_sal.pack(pady=y)
uw_ent_sal.pack(pady=y)
uw_btn_save.pack(pady=y)
uw_btn_back.pack(pady=y)
uw.withdraw()




#DW PROG



def delete ():
	con = None
	try:
		con = connect("ems.db")
		cursor = con.cursor()
		sql = "delete from emp where id='%d' "
		
		wid = dw_ent_id.get()
		if not(wid.isdigit()) or wid=='0':
			raise Exception("Only Positive Integers are Allowed in ID")
		
		id = int(dw_ent_id.get())

		cursor.execute(sql%(id))
		if cursor.rowcount == 1:    
			con.commit()
			showinfo("Done" , "Record Deleted successfully ")
		else:
			showwarning("OOPS" ,  "Only Added Data Can Delete Here")
		
		
	except Exception as e:
		
		con.rollback()
		showerror("issue 3" , e)
	finally :
		
		if con is not None:
			con.close()
		dw_ent_id.delete(0, END)
		dw_ent_id.focus()



def bac4 ():
	dw.withdraw()
	mw.deiconify()




dw = Toplevel(mw)
dw.title("Delete Employee")
dw.geometry("600x600+100+100")
dw.configure(bg = "OliveDrab4")

dw_lab_id = Label(dw, text = " Enter id " , font = f)
dw_lab_id2 = Label(dw , text = "( NOTE : * Enter Only Positive Integers )" , font=f1 , bg = "OliveDrab4")
dw_ent_id = Entry(dw , font = f)

dw_btn_save = Button(dw, text = "DELETE" , font = f , command = delete)
dw_btn_back = Button(dw , text="BACK" , font = f , command= bac4)

dw_lab_id2.place(x=150 ,  y=55)
dw_lab_id.pack(pady=y)
dw_ent_id.pack(pady=y)
dw_btn_save.pack(pady=y)
dw_btn_back.pack(pady=y)

dw.withdraw()




# chart window programming




mw.mainloop()