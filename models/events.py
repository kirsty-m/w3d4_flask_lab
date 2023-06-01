from models.event import *
import datetime

event1 = Event("2/6/23", "Delicious Donut Derby", 15, "Breakout Room", "Delicious donuts for everyone!")
event2 = Event("5/6/23", "Ping Pong Party", 10, "Breakout Room", "Ping pong mania for ping pong maniacs!")

events = [event1, event2]

def add_new_event(event):
    events.append(event)