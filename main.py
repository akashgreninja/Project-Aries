from math import floor
import time
from wsgiref.validate import validator
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import wikipedia
import smtplib
import random
import datetime
from Startup import Setup
import requests
from fun import Fun
from tech import Tech
from sqlalchemy import Table, Column, Integer, ForeignKey,Float,String
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trial-3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Volume(db.Model):
    __tablename__="volume"
    id=db.Column(db.Integer,primary_key=True)
    volume=db.Column(db.Integer)

class Notes(db.Model):
    __tablename__="notes"
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(100))
db.create_all()


###n Terminal type

# pip install pipwin
# Then
#
# pipwin install pyaudio





print("Started up boss")




setup=Setup()
fun=Fun()
tech=Tech()



setup.speak("Hello ")



  
def bootup():
    # self.engine.setProperty("rate", 200)
    a = int(datetime.datetime.now().strftime("%H"))
    b = int(datetime.datetime.now().strftime("%M"))

    if a>0 and a<12:
        setup.speak(f"good morning Sir welcome back its {f'{a} {b}'}am ")
    elif a >=12 and a<18:
        setup.speak(f"good afternoon Sir welcome back its {f'{a} {b}'}pm")

    else:
        setup.speak(f"good evening Sir welcome back its {f'{a} {b}'}pm")

    setup.speak("How may i be of help today")
bootup()



results=setup.take()
print(results)



if 'wikipedia' in results:
    setup.speak("searching on wikipedia")
    resultswiki=fun.wikipedia(results)
    setup.speak(resultswiki)
    setup.take()


elif "add" and "notes" or "notes" in results:
    notes=Notes.query.all()
    print(notes)
    for i in notes:
        
          setup.speak(f"{i.id}    {i.content}")
    setup.speak("to remove any notes state its serial number or tell delete all to erase all old notes")
    results=setup.take()
    if not "delete" and "all" in results:
        b=results.split()
        for i in b:
            try:
                z=int(i)
            except:
                z=i
        len=Notes.id.property.columns[0].type.length
        if len>=z:
            if type(z)==int:
                note=Notes.query.get(z)
                db.session.delete(note)
                db.session.commit()
                setup.speak(f"deleted note {z} succesfully")
        else:
            setup.speak("inappropriate input")
    if "delete" and "all" in results:
        db.session.query(Notes).delete()
        db.session.commit()
        setup.speak("all notes have been deleted")

                

    setup.speak("if you want me to add new notes please state it otherwise tell no ")
    results=setup.take()
    if not "no" in results:
        new=Notes(
            content=results
        )
        db.session.add(new)
        db.session.commit()
        setup.speak("notes added succesfully")
    

elif "choose" and "between" in results:
    setup.speak("what do i need to choose between ,please state first option")
    firstopt=setup.take()
    setup.speak("state the second option")
    secopt=setup.take()
    optlist=[]
    optlist.append(firstopt)
    optlist.append(secopt)
    chosen=random.choice(optlist)
    setup.speak(f"i think {chosen} is a better choice")
    

elif 'time now' in results:
   results=tech.timenow()
   setup.speak(results)


elif 'open youtube' in results:
    tech.openyt(results=results)


elif "change " and "volume" in results:
    setup.kai(results)
   


























   

elif 'dad joke' or 'add joke' in results:
    result_dad=tech.dad_joke()
    setup.speak(result_dad)


elif "joke" or "jokes" in results:
        result_joke=tech.joke()
        setup.speak(result_joke)
