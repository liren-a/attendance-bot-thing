# Google Form Automation
# Developed by John Seong and Liren Abeyratne
# Last updated date: May 11, 2021

# Please include remarks for any changes that you have made!

import requests
import datetime
import time
import sys

url = 'https://docs.google.com/forms/d/e/1FAIpQLSdrxP9zkT4JCNCbmwrr70nMe80j4XbZUaHivLQNQ5oCjuYLiA/viewform'

print ("Welcome to Google Form Automation! This is a bot designed specifically for Google Form Attendance, which a lot of schools are using amid COVID-19 pandemic.", end = '')
print("Developed by John Seong and Liren Abeyratne", end = '')

timeMonday = input("Enter the time (hour) of your class on Monday: "
minMonday = input("Enter the time (minutes) of your class on Monday: ")

timeTuesday = input("Enter the time (hour) of your class on Tuesday "
minTuesday = input("Enter the time (minutes) of your class on Tuesday: ")

timeWednesday = input("Enter the time (hour) of your class on Wednesday: "
minWednesday = input("Enter the time (minutes) of your class on Wednesday: ")

timeThursday = input("Enter the time (hour) of your class on Thursday: "
minThursday = input("Enter the time (minutes) of your class on Thursday: ")

timeFriday = input("Enter the time (hour) of your class on Friday: "
minFriday = input("Enter the time (minutes) of your class on Friday: ")

def get_values():
    """It returns a list of different form data to be submitted by send_attendance method.
    subjects_time is a dictionary with Day as keys and time and subjects in a list as values.
    value_list is a list of lectures' subject and time of current_day."""

    values_list = []
    now = datetime.datetime.now()
    day_name = now.strftime("%A")

    # We're going to have to edit this part of the code, for now, the values in the array are simply placeholders to demonstrate the feature:
    subjects_time = {
        "Monday": [["10", "30", "AJ(HC)"], ["11", "30", "DCDR(PC)"], ["1", "00", "WT(AM)"], ["2", "00", "SE(KD)"]],
        "Tuesday": [["11", "30", "SE(KD)"], ["1", "00", "AJ(HC)"]],
        "Wednesday": [["11", "30", ".NET(PC)"], ["1", "00", "SE(KD)"], ["2", "00", ".NET(PC)"]],
        "Thursday": [["10", "30", "WT(AM)"], ["11", "30", "DCDR(PC)"], ["1", "00", "AJ(HC)"]],
        "Friday": [["10", "30", "AJ(HC)"], ["11", "30", ".NET(PC)"], ["1", "00", "SE(KD)"], ["2", "00", ".NET(PC)"]],
    }

    date = str(now).split('-')

    for i in subjects_time[day_name]:
        '''keys are the value of 'name' element of the '''
        values = {
            # TDSB student #
            "emailAddress": str(sys.argv[1]),
            # First name
            "entry.33987362": str(sys.argv[2]),
            # Last name
            "entry.363926033": "BE",
            # Grade
            "entry.733518766": "IT",
          
            """
            "entry.114626584": "Sem-6",
    
            "entry.609979780": i[2],
         
            "entry.1916623197_year": date[0],
            "entry.1916623197_month": date[1],
            "entry.1916623197_day": date[2][0:2],
      
            "entry.125609755_hour": i[0],
            "entry.125609755_minute": i[1],
            """
        }

        values_list.append(values)

    return values_list


def send_attendance(url, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    for d in data:
        try:
            requests.post(url, data=d)
            print("Form Submitted.")
            time.sleep(10)
        except:
            print("Error Occured!")


final_data = get_values()

send_attendance(url, final_data)