from tkinter import *
from tkcalendar import *
import datetime


from db import Database

event_id = []

def grab_data():
	query = "INSERT INTO events (date, start_event, stop_event, description) VALUES(%s, %s, %s, %s)"
	date= cal.selection_get().strftime("%Y-%m-%d")
	db.connect()
	field_1 = date
	field_2 = start_hour.get()
	field_3 = stop_hour.get()
	field_4 = description.get()
	db.insert(query, (field_1, field_2, field_3, field_4))
	db.close()

	get_data_from_table()

def get_data_from_table():
	list_of_event.delete(0, 100)
	date = cal.selection_get().strftime("%Y-%m-%d")
	query = "SELECT start_event, stop_event, description, id FROM events where date='"+date+"' ORDER BY start_event"
	db.connect()
	i = 0
	for x in db.execute_query(query, ""):
		field_1 = str(x[0])
		field_2 = str(x[1])
		field_3 = str(x[2])
		event_id.insert(i, x[3]) 
		list_of_event.insert(i, field_1+" | "+field_2+ " | "+ field_3)
		i=i+1
	if i == 0:
		list_of_event.insert(i, "BRAK WYDARZEŃ")
	db.close()


def change_date(event):
	date_label.config(text=cal.selection_get())
	get_data_from_table()


def change_listbox(event):
	selection = event.widget.curselection()[0]
	event_id_str = str(event_id[selection])
	print(selection)
	query = "SELECT start_event, stop_event, description FROM events where id='"+event_id_str+"'"
	db.connect()
	for x in db.execute_query(query, ""):
		print(x)
	db.close()



if __name__ == "__main__":
	today = datetime.datetime.now()

	root = Tk() 
	root.geometry("700x380")
	root.title("PLANER")

	cal = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day)
	my_button = Button(root, text="Dodaj wydarzenie", command=grab_data)
	list_of_event = Listbox(root, height=10, width=40)
	start_hour = Entry(root)
	stop_hour = Entry(root)
	description = Entry(root, width=40)
	date_label = Label(root, text="")
	start_hour_label = Label(root, text="Godzina początek")
	stop_hour_label = Label(root, text="Godzina koniec")
	description_label = Label(root, text="Opis wydarzenia")
	list_of_event_label = Label(root, text="Twoje wydarzenia w ten dzień")

	cal.grid(row=0, column=0, rowspan=8)
	start_hour_label.grid(row=8, column=0)
	start_hour.grid(row=9, column=0)
	stop_hour_label.grid(row=10, column=0)
	stop_hour.grid(row=11, column=0)
	description_label.grid(row=12, column=0)
	description.grid(row=13, column=0)
	date_label.grid(row=14, column=0)
	my_button.grid(row=15, column=0)

	list_of_event_label.grid(row=0, column=4)
	list_of_event.grid(row=1, column=4, rowspan=10)

	cal.bind("<<CalendarSelected>>", change_date)
	list_of_event.bind("<<ListboxSelect>>", change_listbox)




	db = Database('kalendarz', username='root', password='password', host='localhost')
	sql_file = open("db_create_table.sql")
	sql_as_string = sql_file.read()
	db.connect()
	db.create_table(sql_as_string)
	db.close()

	date_label.config(text=cal.selection_get())
	get_data_from_table()


	root.mainloop()
