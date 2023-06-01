from models.event import *
import datetime

event1 = Event(datetime.date(2023,6,2), "Delicious Donut Derby", 15, "Breakout Room", "Delicious donuts for everyone!")
event2 = Event(datetime.date(2023,6,5), "Ping Pong Party", 10, "Breakout Room", "Ping pong mania for ping pong maniacs!")

events = [event1, event2]

def add_new_event(event):
    events.append(event)