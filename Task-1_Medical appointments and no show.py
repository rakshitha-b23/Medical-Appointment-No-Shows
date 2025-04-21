# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 16:29:19 2025

@author: Rakshitha K B
"""
#importing the libraries
import pandas as pd
import numpy as np

#importing dataset
df= pd.read_csv(r"C:\Users\Rakshitha K B\Documents\ELEVATE LABS INTERNSHIP\DATASETS\Medical Appointment No Show.csv")

#checking for dataframe
df.head
df.shape

# Strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()
print(df.columns)

#changing date format to dd-mm-yyyy
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.strftime('%d-%m-%Y')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.strftime('%d-%m-%Y')
print(df.columns)


#checking for null values
df.isnull().sum
df.isnull().values.any()

#checking for duplicates
df.duplicated()

"""Waiting Time Calculation"""

#Convert to datetime to calculate waiting days 
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

#Calculating the difference in days
df['WaitingDays'] = (df['AppointmentDay'] - df['ScheduledDay']).dt.days

#Check for any negative waiting days
negative_waits = df[df['WaitingDays'] < 0]

print(df[['ScheduledDay', 'AppointmentDay', 'WaitingDays']].head())


"""Age Group Binning"""

def categorize_age(age):
    if age < 0:
        return 'Invalid'
    elif age <= 12:
        return 'Child'
    elif age <= 18:
        return 'Teen'
    elif age <= 35:
        return 'Young Adult'
    elif age <= 60:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(categorize_age)

print(df[['Age', 'AgeGroup']].head())

print(df.columns)

#Reordering the columns
new_order = ['PatientId', 'AppointmentID', 'Gender', 'Age', 'AgeGroup',
             'ScheduledDay', 'AppointmentDay', 'WaitingDays',
             'Neighbourhood', 'Scholarship', 'Hipertension',
             'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received', 'No-show']

df = df[new_order]
print(df.columns)

file_path = r"C:\Users\Rakshitha K B\Documents\ELEVATE LABS INTERNSHIP\Task_1_medical_appointments_data.xlsx"
df.to_excel(file_path, index=False)
print(f"File saved successfully to: {file_path}")

