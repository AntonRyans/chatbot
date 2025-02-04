import mysql.connector as mc
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

myCon = mc.connect(host=DB_HOST, user= DB_USER, passwd=DB_PASS, db = DB_NAME) # Create Connection
mycursor = myCon.cursor() # Create Cursor
engine = pyttsx3.init() # Establish Voice Bot and Assign it to variable engine
engine.say("Hello there, I am Bot. Your friendly neighbourhood Chatbot.")
engine.runAndWait()
print("Hello there, I am Bot. Your friendly neighbourhood Chatbot.")
engine.say("What's your name?")
engine.runAndWait()
user_name=input("What's your name? ")
engine.say("Nice to meet you," + str(user_name))
engine.runAndWait()
print("Nice to meet you,", user_name)
engine.say("What's your age? ")
engine.runAndWait()
age=int(input("What's your age? "))
engine.say("Where are you from? ")
engine.runAndWait()
home=input("Where are you from? ")
engine.say("Oh ," + str(home) + " is a nice place.")
engine.runAndWait()
print("Oh ," + home + " is a nice place.")
engine.say("What do you study? ")
engine.runAndWait()
course=input("What do you study? ")
sql = "INSERT INTO user_data (user_name, age, home, course) VALUES (%s, %s, %s, %s)"
val = (user_name, age, home, course)
mycursor.execute(sql, val) # Insert user data into MySQL
myCon.commit()
print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM USER_DATA")
rows = mycursor.fetchall() # Store fetched data into variable rows
print("Here is the User Data Table")
for row in rows:
    print(row)
mycursor.close()
myCon.close()    
print("Connection closed successfully.") # Close connection and print message                     