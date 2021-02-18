from tkinter import *
from tkcalendar import *
import datetime


from db import Database


def grab_data():
	query = "INSERT INTO events (date, stop_event, description) VALUES(%s, %s, %s)"
	date= cal.selection_get().strftime("%Y-%m-%d")
	db.connect()
	db.insert(query, (date, stop_hour.get(), description.get()))
	db.close()

	get_data_from_table()

def get_data_from_table():
	list_of_event.delete(0, 100)
	date = cal.selection_get().strftime("%Y-%m-%d")
	query = "SELECT description FROM events where date='"+date+"'"
	db.connect()
	i = 0
	for x in db.execute_query(query, ""):
		list_of_event.insert(i, x[0])
		i=i+1
	db.close()


def change_date(event):
	my_label.config(text=cal.selection_get())
	get_data_from_table()


if __name__ == "__main__":
	today = datetime.datetime.now()

	root = Tk() 
	root.geometry("600x400")

	cal = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day)
	my_button = Button(root, text="Insert event", command=grab_data)
	list_of_event = Listbox(root, height=10, width=40)
	start_hour = Entry(root)
	stop_hour = Entry(root)
	description = Entry(root)
	my_label = Label(root, text="")

	cal.grid(row=0, column=0)
	my_button.grid(row=3, column=0)
	start_hour.grid(row=5, column=0)
	stop_hour.grid(row=7, column=0)
	description.grid(row=9, column=0)
	my_label.grid(row=11, column=0)

	list_of_event.grid(row=0, column=1, columnspan=3)



	cal.bind("<<CalendarSelected>>", change_date)




	db = Database('kalendarz', username='root', password='password', host='localhost')
	sql_file = open("db_create_table.sql")
	sql_as_string = sql_file.read()
	db.connect()
	db.create_table(sql_as_string)
	db.close()

	my_label.config(text=cal.selection_get())
	get_data_from_table()





  
# root.geometry("600x400") 
  
# cal = Calendar(root, selectmode = 'day', 
#                year = 2020, month = 5, 
#                day = 22) 
  
# cal.pack(pady = 20) 
  
# def grad_date(): 
#     date.config(text = "Selected Date is: " + cal.get_date()) 
  
# Button(root, text = "Get Date", 
#        command = grad_date).pack(pady = 20) 
  
# date = Label(root, text = "") 
# date.pack(pady = 20) 
  

root.mainloop()
