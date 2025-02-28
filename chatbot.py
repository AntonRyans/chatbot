from sqlalchemy import create_engine, text
import pyttsx3
import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

# Load environment variables from .env file
load_dotenv()

# Load DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Initialize voice engine
voice_engine = pyttsx3.init()

# Voice prompts
voice_engine.say("Hello there, I am Bot. Your friendly neighbourhood Chatbot.")
voice_engine.runAndWait()
print("Hello there, I am Bot. Your friendly neighbourhood Chatbot.")

voice_engine.say("What's your name?")
voice_engine.runAndWait()
user_name = input("What's your name? ")

voice_engine.say("Nice to meet you, " + str(user_name))
voice_engine.runAndWait()
print("Nice to meet you,", user_name)

voice_engine.say("What's your age? ")
voice_engine.runAndWait()
age = int(input("What's your age? "))

voice_engine.say("Where are you from? ")
voice_engine.runAndWait()
home = input("Where are you from? ")

voice_engine.say("Oh, " + str(home) + " is a nice place.")
voice_engine.runAndWait()
print("Oh,", home, "is a nice place.")

voice_engine.say("What do you study? ")
voice_engine.runAndWait()
course = input("What do you study? ")

# Insert user data into MySQL using SQLAlchemy
insert_sql = text("""
    INSERT INTO user_data (user_name, age, home, course) 
    VALUES (:user_name, :age, :home, :course)
""")

with engine.begin() as connection:  # `begin()` ensures auto-commit
    connection.execute(insert_sql, {
        "user_name": user_name,
        "age": age,
        "home": home,
        "course": course
    })

print("1 record inserted.")

# Read table into Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM user_data", con=engine)
print(df)

def option(num):
    if num == 1:
        # Group data by age and count the number of users in each age group
        age_counts = df['age'].value_counts().sort_index()

        # Create the bar chart
        plt.bar(age_counts.index, age_counts.values)
        plt.xlabel("Age")
        plt.ylabel("Number of Users")
        plt.title("Distribution of Users by Age")
        plt.show()

    if num == 2:
        # Group data by home and count the number of users in each age group
        home_counts = df['home'].value_counts().sort_index()

        # Create the bar chart
        plt.bar(home_counts.index, home_counts.values)
        plt.xlabel("Home")
        plt.ylabel("Number of Users")
        plt.title("Distribution of Users by Home")
        plt.show()

    if num == 3:
        # Group data by course and count the number of users in each age group
        course_counts = df['course'].value_counts().sort_index()

        # Create the bar chart
        plt.bar(course_counts.index, course_counts.values)
        plt.xlabel("Course")
        plt.ylabel("Number of Users")
        plt.title("Distribution of Users by Course")
        plt.show()

print("Data Visualisation Options:")
print("1. View the Bar Chart of Distribution of Users by Age")
print("2. View the Bar Chart of Distribution of Users by Home")
print("3. View the Bar Chart of Distribution of Users by Course")
ch="y"
while ch.lower() == "y":
    num=int(input("What option do you choose? "))
    option(num)
    ch=input("Do you want to continue or not? [y/n] ")

print("Database operations completed successfully.")