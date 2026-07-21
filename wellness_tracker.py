
from datetime import date
import os
import csv

def get_positive_number(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Number must be greater than 0")
            else:
                return number

        except ValueError:
            print("Please enter a valid number")

def get_mood ():

    mood_prompt = (
    "How Would You Rate Your Mood Today?:\n"
    "1 - Angry\n"
    "2 - Sad\n"
    "3 - Anxious\n"
    "4 - Cheerful\n"
    "5 - Calm\n"
    "6 - Neutral\n"
    )
    while True:
        try:
            mood = int(input(mood_prompt))

            if mood <1 or mood >6:
                print ("Invalid choice. Please enter a number between 1 and 6.")
            
            else:
                return(mood)
            
        except ValueError:
            print ("Please Enter a Number Between 1 and 6")

print ("------------------DAILY WELLNESS TRACKER----------------")

name= input("What is Your Name: ")

print (f"Hello {name}! \nWelcome to Your Wellness Tracker.\n")


weight = get_positive_number("What is Your Weight Today(kg)?: ")

sleep = get_positive_number ("How Many Hours Did You Sleep Last Night?: ")

steps = get_positive_number ("How Many Steps Did You Walk Today?: ")

mood = get_mood ()


mood_dict = { 
    1:'Angry', 
    2:'Sad', 
    3:'Anxious', 
    4:'Cheerful', 
    5:'Calm', 
    6:'Neutral'
}

today = date.today()

print(f"{name}'s Daily Wellness Summary")

print("------------------------------------------")

print(f"Date: {today}")

print(f"Weight: {weight} kg")

print(f"Sleep: {sleep} hours")

print(f"Steps: {steps}")

print(f"Mood: {mood_dict[mood]}")

file_exists = os.path.exists("daily_wellness.csv")

with open("daily_wellness.csv", "a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow([
            "Date",
            "Name",
            "Weight (kg)",
            "Sleep (hours)",
            "Steps",
            "Mood"
        ])

    writer.writerow([
        today,
        name,
        weight,
        sleep,
        steps,
        mood_dict[mood]
    ])
print("Daily wellness record saved successfully!")   