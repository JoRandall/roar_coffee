# ROAR Coffee Sorting Program
# Author: Jonathan Kenney
# ***ROAR Exec 2018-2019***

import csv

ROAR_COFFEE_FIELDNAMES = [
    'Timestamp', 
    'Email Address', 
    'Name (first and last)',
    'What college are you in?',
    'Year',	
    'This is my ____ year as a ROAR Guide',
    'I would describe myself as an',
    'My favorite part of going to UC is',
    'I would love to',
    'One word to describe me is'
]

EXEC_NAMES = [
    'Chandler Meador',
    'Louis Acra',
    'Danielle Somershoe',
    'Nicole Smallwood',
    'Scott Venemeyer',
    'Dymond Robinson',
    'Kylie Boyd',
    'Jonathan Kenney'
]

class Person:
    
    def __init__(self, uid, timestamp, email, name, college, a_year, r_year, energy, favorite, motive, word):
        self.uid = uid
        self.timestamp = timestamp
        self.email = email
        self.name = name
        self.college = college
        self.a_year = a_year
        self.r_year = r_year
        self.energy = energy
        self.favorite = favorite
        self.motive = motive
        self.word = word
        
        self.checkExec()

    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year

    def checkExec(self)
        if self.name in EXEC_NAMES:
            self.inExec = 1
        else:
            self.inExec = 0
            

    
def main():
    guides = []

    with open('RoarCoffee.csv') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(row)
        # for row in reader:
        #     newPerson = Person()

        #     guides.append()


main()