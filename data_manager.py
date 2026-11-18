# CSV read, write, update, delete functions

import csv

FILE_NAME = "applications.csv"

def load_applications():

    #Loads all application records from the CSV file.

    file = open(FILE_NAME, "r", encoding="utf-8")
    data = list(csv.reader(file))
    file.close()
    return data

def save_all_applications(apps):

    #Overwrites the CSV file with the complete updated list of applications.

    file = open(FILE_NAME, "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerows(apps)
    file.close()
