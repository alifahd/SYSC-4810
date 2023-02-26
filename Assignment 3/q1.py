import datetime
import os
from hashlib import blake2b
from hashlib import pbkdf2_hmac

users = {"Mischa Lowery": "Regular Client", "Willow Garza": "Premium Client", "Veronica Perez": "Regular Client", "Nala Preston": "Premium Client",
         "Winston Callahan": "Teller", "Stacy Kent": "Investment Analyst", "Kelan Gough": "Teller", "Keikilana Kapahu": "Investment Analyst", "Nelson Wilkins": "Financial Advisor",
         "Kodi Matthews": "Financial Planner", "Kelsie Chang": "Financial Advisor", "Malikah Wu": "Financial Planner", "Howard Linkler": "Compliance Officer", "Caroline Lopez":
         "Technical Support", "Stefania Smart": "Compliance Officer", "Pawel Barclay": "Technical Support"}

"""
for person in users:
    print(person + " is a " +
          users[person] + " and can view: " + ", ".join(roles[users[person]]["view"]))
    print(person + " is a " +
          users[person] + " and can modify: " + ", ".join(roles[users[person]]["modify"]))
    print(person + " is a " + users[person] + " and can validate modifications: " +
          ", ".join(roles[users[person]]["validate modifications"]))
    print(person + " is a " + users[person] + " and can view upon access: " +
          ", ".join(roles[users[person]]["view upon access"]))


while(True):
    role = input("Enter your role: ")

    print(role + " can view: " + ", ".join(roles[role]["view"]))
    print(role + " can modify: " + ", ".join(roles[role]["modify"]))
    print(role + " can validate modifications: " +
          ", ".join(roles[role]["validate modifications"]))
    print(role + " can view upon access: " +
          ", ".join(roles[role]["view upon access"]))
"""

import datetime
import os
from hashlib import blake2b
from hashlib import pbkdf2_hmac

roles = {
    "Regular Client":
        {
            "view": ["Client Account Balance", "Client Investment Portfolio", "Contact Details of Financial Advisor"],
            "modify": [],
            "validate modifications": [],
            "view upon access": []
        },
    "Premium Client":
        {
            "view": ["Client Account Balance", "Client Investment Portfolio", "Contact Details of Financial Advisor", "Contact Details of Financial Planner", "Contact Details of Investment Analyst"],
            "modify": ["Client Investment Portfolio"],
            "validate modifications": [],
            "view upon access": []
        },
    "Teller":
    {
            "view": ["Client Account Balance (Between the hours of 9-5)", "Client Investment Portfolio (Between the hours of 9-5)"],
            "modify": [],
            "validate modifications": [],
            "view upon access": []
        },
    "Financial Advisor":
    {
            "view": ["Client Account Balance", "Client Investment Portfolio", "Private Consumer Instruments"],
            "modify": ["Client Investment Portfolio"],
            "validate modifications": [],
            "view upon access": []
        },
    "Compliance Officer":
    {
            "view": ["Client Account Balance", "Client Investment Portfolio"],
            "modify": [],
            "validate modifications": ["Client Investment Portfolio"],
            "view upon access": []
        },
    "Investment Analyst":
    {
            "view": ["Client Account Balance", "Client Investment Portfolio", "Money Market Instruments", "Private Consumer Instruments", "Derivatives Trading", "Interest Instruments"],
            "modify": ["Client Investment Portfolio"],
            "validate modifications": [],
            "view upon access": []
        },
    "Financial Planner":
    {
            "view": ["Client Account Balance", "Client Investment Portfolio", "Money Market Instruments", "Private Consumer Instruments"],
            "modify": ["Client Investment Portfolio"],
            "validate modifications": [],
            "view upon access": []
        },
    "Technical Support":
    {
            "view": [],
            "modify": [],
            "validate modifications": [],
            "view upon access": ["Client Account Balance", "Client Investment Portfolio"]
        },
}
special = ["!", "@", "#", "$", "%", "?", "∗"]
common = []
with open('common_passwords.txt') as f:
    for line in f.readlines():
        common.append(line)
        f.close()


option = input("Sign Up or Sign In? (U/I)")

if option == "U" or option == "u":
    userid = input("Enter your user ID: ")
    username = input("Enter your name: ")
    while True:
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Password is too short")
        elif len(password) > 12:
            print("Password is too long")
        elif not any(x.isupper() for x in password):
            print("Password needs an uppercase")
        elif not any(x.islower() for x in password):
            print("Password needs an uppercase")
        elif not any(x.isdigit() for x in password):
            print("Password needs a number")
        elif not any(x in password for x in special):
            print("Password needs a special character from the set {!, @, #, $, %, ?, ∗}")
        elif any(x in password for x in common):
            print("Password is too common")
        elif password == userid or password == username:
            print("Password can't be same as User ID or Name")
        else:
            break
    while True:
        role = input("Enter your role (select 1 - 8):\n1. Regular Client\n2. Premium Client\n3. Teller\n4. Financial Advisor\n5. Compliance Officer\n6. Investment Analyst\n7. Financial Planner\n8. Technical Support\n")
        if not role.isdigit():
            print("Please enter a number")
        elif int(role) > 8 or int(role) < 1:
            print("Please enter a valid number")
        else:
            role = list(roles.keys())[int(role) - 1]
            break
    
    print("Account Created.")

    with open('passwd.txt', 'a') as f:
        salt = os.urandom(blake2b.SALT_SIZE)
        dk = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 500_000)
        f.write(userid+':'+username+':'+dk.hex()+':'+salt.hex() +':'+role+'\n')
else:
    userid = input("Enter your user ID: ")
    password = input("Enter your password: ")

    with open('passwd.txt') as f:
        lines = f.readlines()
        for line in lines:
            if userid in line:
                line = line.strip()
                arr = line.split(':')
                plaintext_salt = bytes.fromhex(arr[3])
                check = pbkdf2_hmac('sha256', password.encode('utf-8'), plaintext_salt, 500_000)
                if check.hex() == arr[2]:
                    print("\n\nACCESS GRANTED\nWelcome "+arr[1]+".\n")
                    print("You are a " + arr[4] + " and can view: " + ", ".join(roles[arr[4]]["view"]))
                    print("\nand can modify: " + ", ".join(roles[arr[4]]["modify"]))
                    print("\nand can validate modifications: " + ", ".join(roles[arr[4]]["validate modifications"]))
                    print("\nand can view upon access: " + ", ".join(roles[arr[4]]["view upon access"]))
                    f.close()