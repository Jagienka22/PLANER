from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import threading


from db import Database

from kalendarz_thread import *

event_id = []

def add_data():
	query = "INSERT INTO events (date, start_event, stop_event, description) VALUES(%s, %s, %s, %s)"
	date = cal.selection_get().strftime("%Y-%m-%d")
	
	field_1 = date
	field_4 = description.get()

	try:
		field_2 = datetime.datetime.strptime(start_hour.get(),"%H:%M:%S")
		field_3 = datetime.datetime.strptime(stop_hour.get(),"%H:%M:%S")
	except ValueError:
		messagebox.showinfo(title = 'Błąd danych', message = 'Nepoprawny format godziny! - poprawny to: 00:00:00')
		return

	if(field_2 > field_3):
		messagebox.showinfo(title = 'Błąd danych', message = 'Godzina początkowa musi być wcześniej niż godzina końcowa!')
		return

	field_2 = field_2.strftime("%H:%M:00")
	field_3 = field_3.strftime("%H:%M:00")

	db.connect()
	db.insert(query, (field_1, field_2, field_3, field_4))
	db.close()

	print("Dodano nowe wydarzenie")
	send_notify(title="Dodano nowe wydarzenie", description=field_4)
	messagebox.showinfo(title = 'Potwierdzenie', message = 'Dodano nowe wydarzenie')
	get_data_from_table()


def delete_data():
	selection = list_of_event.curselection()[0]
	event_id_str = str(event_id[selection])
	query = "DELETE FROM events WHERE id='"+event_id_str+"'"
	db.connect()
	db.update(query, "")
	db.close()

	print("Usunięto wydarzenie")
	send_notify(title="Usunięto wydarzenie", description="")
	messagebox.showinfo(title = 'Potwierdzenie', message = 'Wydarzenie zostało usunięte')
	get_data_from_table()


def modify_data():
	selection = list_of_event.curselection()[0]
	event_id_str = str(event_id[selection])

	query = "UPDATE events SET start_event=%s, stop_event=%s, description=%s WHERE id=%s"
	field_4 = description.get()

	try:
		field_2 = datetime.datetime.strptime(start_hour.get(),"%H:%M:%S")
		field_3 = datetime.datetime.strptime(stop_hour.get(),"%H:%M:%S")
	except ValueError:
		messagebox.showinfo(title = 'Błąd danych', message = 'Nepoprawny format godziny! - poprawny to: 00:00:00')
		return

	if(field_2 > field_3):
		messagebox.showinfo(title = 'Błąd danych', message = 'Godzina początkowa musi być wcześniej niż godzina końcowa!')
		return

	field_2 = field_2.strftime("%H:%M:00")
	field_3 = field_3.strftime("%H:%M:00")

	db.connect()
	db.update(query, (field_2, field_3, field_4, event_id_str))
	db.close()

	print("Zmodyfikowano wydarzenie")
	send_notify(title="Zmodyfikowano wydarzenie", description=field_4)
	messagebox.showinfo(title = 'Potwierdzenie', message = 'Zapisano zmiany')
	get_data_from_table()


def get_data_from_table():
	list_of_event.delete(0, 'end')
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

	start_hour.delete(0, 'end')
	stop_hour.delete(0, 'end')
	description.delete(0, 'end')

	get_data_from_table()


def change_listbox(event):
	selection = list_of_event.curselection()[0]
	event_id_str = str(event_id[selection])
	print(selection)
	query = "SELECT start_event, stop_event, description FROM events where id='"+event_id_str+"'"
	db.connect()
	for x in db.execute_query(query, ""):
		print(x)
		start_hour.delete(0, 'end')
		start_hour.insert(0, x[0])
		stop_hour.delete(0, 'end')
		stop_hour.insert(0, x[1])
		description.delete(0, 'end')
		description.insert(0, x[2])
	db.close()


if __name__ == "__main__":
	root = Tk() 
	root.geometry("680x430")
	root.title("PLANER")

	today = datetime.datetime.now()

	cal = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day)

	add_button = Button(root, text="Dodaj wydarzenie", command=add_data, bg = "dark gray")
	modify_button = Button(root, text="Edytuj", command=modify_data)
	delete_button = Button(root, text="Usuń", command=delete_data)

	list_of_event = Listbox(root, height=22, width=40, exportselection=False)
	start_hour = Entry(root)
	stop_hour = Entry(root)
	description = Entry(root, width=40)

	date_label = Label(root, text="", font = ("times", 16, 'bold'))
	start_hour_label = Label(root, text="Godzina początek:", font = ("times", 10))
	stop_hour_label = Label(root, text="Godzina koniec:", font = ("times", 10))
	description_label = Label(root, text="Opis wydarzenia:", font = ("times", 10))
	list_of_event_label = Label(root, text="Twoje wydarzenia w ten dzień", font = ("times", 11, 'bold'))

	#lewa strona
	cal.grid(row=0, column=0, rowspan=8, columnspan=3)
	date_label.grid(row=9, column=0, columnspan=3)
	start_hour_label.grid(row=10, column=0, columnspan=3)
	start_hour.grid(row=11, column=0, columnspan=3)
	stop_hour_label.grid(row=12, column=0, columnspan=3)
	stop_hour.grid(row=13, column=0, columnspan=3)
	description_label.grid(row=14, column=0, columnspan=3)
	description.grid(row=15, column=0, columnspan=3)
	
	modify_button.grid(row=19, column=0, rowspan=2)
	delete_button.grid(row=19, column=1, rowspan=2)

	add_button.grid(row=21, column=2, rowspan=3)

	#prawa strona
	list_of_event_label.grid(row=0, column=4)
	list_of_event.grid(row=1, column=4, rowspan=22)


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

	x = threading.Thread(target=start_thread, args=(db, ))
	x.start()

	root.mainloop()