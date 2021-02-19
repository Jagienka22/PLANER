from pynotifier import Notification
import datetime

from db import Database

def send_notify(title='Notification Title', description='Notification Description', urgency=Notification.URGENCY_NORMAL):
	Notification(
		title=title,
		description=description,
		icon_path='path/to/image/file/icon.png',
		duration=10,                              # Duration in seconds
		urgency=urgency
	).send()


def start_thread( db ):
	today = datetime.datetime.now()
	second = today.second
	s.enter(60 - second, 1, check_events, (s, db))
	s.run()


import sched, time
s = sched.scheduler(time.time, time.sleep)
def check_events(sc, db): 
	print("checking events...")

	today = datetime.datetime.now()
	second = today.second

	date = today.strftime("%Y-%m-%d")
	time = today.strftime("%H:%M:00")
	print(date)
	print(time)

	query = "SELECT start_event, stop_event, description, id FROM events where date='"+date+"' AND start_event='"+time+"' ORDER BY stop_event"
	db.connect()
	for x in db.execute_query(query, ""):
		print(x)
		send_notify("uwaga wydarzenie", x[2], urgency=Notification.URGENCY_CRITICAL)
	db.close()

	# do your stuff
	s.enter(60, 1, check_events, (sc, db))