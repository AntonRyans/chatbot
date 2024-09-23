import mysql.connector as mc
import pyttsx3
engine = pyttsx3.init() 
engine.say("Hello there, I am Bot. Your friendly neighbourhood Chatbot.")
engine.runAndWait()
print("Hello there, I am Bot. Your friendly neighbourhood Chatbot.")
engine.say("What's your name?")
engine.runAndWait()
name=input("What's your name? ")
engine.say("Nice to meet you," + str(name))
engine.runAndWait()
print("Nice to meet you,", name)
engine.say("What's your age? ")
engine.runAndWait()
age=int(input("What's your age? "))
engine.say("Where are you from? ")
engine.runAndWait()
home=input("Where are you from? ")
engine.say("What do you study? ")
engine.runAndWait()
course=input("What do you study? ")
myCon = mc.connector.connect( host=hostname, user=username, passwd=root, db = bot_data)
mycursor = myCon.cursor()
sql = "INSERT INTO user_data (name, age, home, course) VALUES (%s, %s, %s, %s)"
val = (name, age, home, course)
mycursor.execute(sql, val)
myCon.commit()
print(mycursor.rowcount, "record inserted.")
"""engine.say("Do you want to save your data to the database? ")
engine.runAndWait()
consent=input("Do you want to save your data to the database?[y/n] ")
while consent.lower == "y":
    myCon = mc.connector.connect( host=hostname, user=username, passwd=root, db = bot_data)
    mycursor = myCon.cursor()
    sql = "INSERT INTO user_data (name, age, home, course) VALUES (%s, %s, %s, %s)"
    val = (name, age, home, course)
    mycursor.execute(sql, val)
    myCon.commit()
    print(mycursor.rowcount, "record inserted.")"""
    
    
    

