from flask import Flask, request
from icalevents.icalevents import events
import random

app = Flask(__name__)

snark = ["According to my research", "Looks like", "The calendar says", "I'm pretty sure", "You're going to love it"]

located = ["Whiskey Friday is going to be at", "we're going to", "the destination is", "we'll gather at"]

dunno = ["I don't know, sorry.", "I have no idea.", "Go ask someone else.", "I seem to have forgotten."]

@app.route("/",methods=["POST"])
def slackbot():
    newBoCoEvents = events("https://newbo.co/events/list/?shortcode=75735a1e&ical=1")
    newBoCoEvents = list(filter(lambda e: "Whiskey Friday" in e.summary, newBoCoEvents))
    if len(newBoCoEvents):
        eventSummary = newBoCoEvents[0].summary
        try:
            return random.choice(snark) + " " + random.choice(located) + " " + eventSummary.split(": ")[1]
        except:    
            return newBoCoEvents[0].summary
    else:
        return random.choice(dunno)
