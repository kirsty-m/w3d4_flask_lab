from flask import render_template, request
from app import app
from models.events import events, add_new_event
from models.event import Event

@app.route('/events')
def show_events():
    return render_template("index.html", event_list=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["event_name"]
    event_guest_number = request.form["guest_number"]
    event_room = request.form["room"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name, event_guest_number, event_room, event_description)
    add_new_event(new_event)
    return render_template("index.html", event_list=events) 