from tkinter import *
from tkcalendar import *
import datetime

def grab_date():
	my_label.config(text="PLANER")

if __name__ == "__main__":
	today = datetime.datetime.now()

	root = Tk() 
	root.geometry("600x400")

	cal = Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day)
	my_button = Button(root, text="Get Date", command=grab_date)
	list_of_event = Listbox(root, height=10, width=40)
	start_hour = Entry(root)
	stop_hour = Entry(root)
	description = Entry(root)

	cal.grid(row=0, column=0)
	my_button.grid(row=3, column=0)
	start_hour.grid(row=5, column=0)
	stop_hour.grid(row=7, column=0)
	description.grid(row=9, column=0)

	list_of_event.grid(row=0, column=1, columnspan=3)



	my_label = Label(root, text="")

	list_of_event.insert(0, "wolter")
	list_of_event.insert(1, "jagienka")







  
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
