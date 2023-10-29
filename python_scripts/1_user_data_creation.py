# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:38:54 2023

@author: darsh
"""

import random
import string
import csv

# Define education levels and languages if not already defined
education_levels = [
    "High School Diploma",
    "Associate's Degree",
    "Bachelor's Degree",
    "Master's Degree",
    "Doctorate",
    "Other"
]

languages = [
    "Hindi",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Urdu",
    "Gujarati",
    "Kannada",
    "Odia",
    "Punjabi",
    "Malayalam",
    "Assamese",
    "Maithili",
    "Santali",
    "Kashmiri",
    "Nepali",
    "Konkani",
    "Manipuri",
    "Bodo",
    "Sanskrit",
]

cities = ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Pimpri-Chinchwad', 'Nashik',
          'Kalyan-Dombivli', 'Vasai-Virar', 'Aurangabad', 'Navi Mumbai', 'Solapur',
          'Mira-Bhayandar', 'Bhiwandi-Nizampur', 'Jalgaon', 'Amravati', 'Nanded-Waghala',
          'Kolhapur', 'Ulhasnagar', 'Sangli-Miraj & Kupwad', 'Malegaon', 'Akola', 'Latur',
          'Dhule', 'Ahmednagar', 'Ichalkaranji', 'Chandrapur', 'Parbhani', 'Jalna', 'Bhusawal',
          'Navi Mumbai Panvel Raigad', 'Panvel', 'Satara', 'Beed', 'Yavatmal', 'Kamptee', 'Gondia',
          'Barshi', 'Achalpur', 'Osmanabad', 'Nandurbar', 'Wardha', 'Udgir', 'Hinganghat']

occupations = [
    "Engineer",
    "Teacher",
    "Doctor",
    "Software Developer",
    "Nurse",
    "Accountant",
    "Chef",
    "Electrician",
    "Graphic Designer",
    "Lawyer",
    "Mechanic",
    "Pharmacist",
    "Police Officer",
    "Real Estate Agent",
    "Sales Manager",
    "Writer",
    "Artist",
    "Dentist",
    "Firefighter",
    "Marketing Specialist"
]

interests = ["Sports", "Travel", "Cooking", "Gardening", "Reading", "Music", "Hiking", "Art", "Photography", "Gaming", "Fashion", "Technology", "Fitness", "Food", "Movies", "Pets", "Dancing", "Yoga", "Cycling", "Writing"]


# Create a list to store the data
data = []

# Generate 1000 rows of data
for user_id in range(1, 1001):
    row = {
        'user_id': "USI_"+ str(user_id),
        'age': random.randint(28, 65),
        'gender': random.choice(['Male', 'Female']),
        'education': random.choice(education_levels),
        'marital_status': random.choice(['Single', 'Married', 'Divorced']),
        'occupation': random.choice(occupations),
        'interests': random.choice(interests),
        'email': f'user{user_id}@example.com',
        'phone_number': ''.join(random.choice(string.digits) for _ in range(10)),
        'city': random.choice(cities),
        'language': random.choice(languages)
    }
    data.append(row)

# Define the CSV file name
csv_file = 'D:\Project\E-commerce-ETL-Pipeline-Project\static_data\data_user.csv'

# Write the data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"CSV file '{csv_file}' has been created with 1000 rows of data.")
