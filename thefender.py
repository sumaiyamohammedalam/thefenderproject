# Step 1: Import modules
import csv
import json

# Step 2: Create list to store compromised usernames
compromised_users = []

# Step 3: Reading in passwords.csv
# For demonstration, using sample data as a list of dicts
sample_passwords = [
    {"Username": "alice", "Password": "12345"},
    {"Username": "bob", "Password": "qwerty"},
    {"Username": "charlie", "Password": "password"}
]

# Normally you would open the file like this:
# with open("passwords.csv") as password_file:
#     password_csv = csv.DictReader(password_file)
#     for password_row in password_csv:
#         compromised_users.append(password_row['Username'])

# Using sample data instead
for password_row in sample_passwords:
    compromised_users.append(password_row['Username'])

# Step 4: Write compromised users to a text file
with open("compromised_users.txt", "w") as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + "\n")

# Step 5: Notify the boss via JSON
boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
}

with open("boss_message.json", "w") as boss_message:
    json.dump(boss_message_dict, boss_message)

# Step 6: Scramble the passwords by creating a new file with Slash Null's signature
slash_null_sig = """ 
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

with open("new_passwords.csv", "w") as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)

print("All tasks complete. Compromised users, boss message, and new scrambled passwords file created.")
