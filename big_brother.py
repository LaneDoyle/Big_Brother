#!/usr/bin/python3
# big_brother.py
# Lane Doyle
# 1/7/2020

import pickle

'''Runs prototype as specified in Contest_Instructions.txt'''

def print_all(sort_it = False):
    #print("Running print_all()")
    key_list = list(people.keys())
    if sort_it:
        key_list.sort()
    for key in key_list:
        print()
        print("SSN: ", key)
        print("Name: ", people[key][1]+", "+people[key][0])
        print("Birth Year: ", people[key][2])
        print("**********************")

def lookup():
    #print("Running lookup()")
    ssn = input("What is the SSN of the person you wish to lookup? ")
    if ssn in people:
        print()
        print("SSN: ", ssn)
        print("Name: ", people[ssn][1]+", "+people[ssn][0])
        print("Birth Year: ", people[ssn][2])
        print("**********************")
    else:
        print("\n*** THAT SSN DOES NOT EXIST ***\n")


def add_new():
    #print("Running add_new()")
    ssn = input("What is the SSN of the person you wish to add? ")
    if ssn in people:
        print("\n*** THAT NUMBER ALREADY EXISTS! ***\n")
    else:
        first = input("   What is their first name? ")
        last = input("   What is their last name? ")
        year = input("   What is their birth year? ")
        people[ssn] = [first, last, year]

def edit_existing():
    ssn = input("What is the SSN of the person you wish to edit? ")
    if ssn in people:
        first = input("   What is their first name? ")
        last = input("   What is their last name? ")
        year = input("   What is their birth year? ")
        people[ssn] = [first, last, year]
    else: 
        print("\n*** THAT NUMBER DOES NOT EXIST! ***\n")
        

def quit():
    #print("Running quit()")
    pickle_file = open("datafile.pickle", "wb")
    pickle.dump(people, pickle_file)
    pickle_file.close()
    

people = {}
pickle_file = open("datafile.pickle", "rb")
people = pickle.load(pickle_file)
pickle_file.close()


keep_going = True

while keep_going:
    print("""
    Welcome to Big Brother Inc.
    ---------------------------
    
    MAIN MENU
    1) Print All Records
    2) Look Up Person by SSN
    3) Add New Person
    
    4) Print All Records Sorted by SSN
    5) Edit Existing Person
    6) Delete Person from Database
    7) Look Up Person by Name
    
    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        print_all()
    elif choice == "2":
        lookup()
    elif choice == "3":
        add_new()
    elif choice == "4":
        print_all(sort_it = True)  
    elif choice == "5":
        edit_existing()         
    elif choice == "Q" or choice == "q":
        quit()
        keep_going = False
    else:
        print("*** PLEASE CHOOSE A VALID OPTION ***\n")
        
print("\nData saved! Goodbye!\n")
        
