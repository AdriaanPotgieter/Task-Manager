'''
Compulsory task.
This program will allow a user to login and register new members as well as let the admin to add more members.
It will allow them to create a password as well and to confirm their password. They will be able to view their
tasks as well when loging in to the menu.
'''

# This code will check whether the person can login or not by using a while loop. It will read the data from
# user.txt file and store the information in a dictionary.
# Creating an empty dictionary.
user_names = {}

# Open and close user.txt file to read from and giving it a variable name.
with open("user.txt", "r") as users:

# Use for loop to access each name and password in the user.txt file.
    for user in users:

# Giving the username and password new variables and creating a list.
        usr, pswd = user.split(", ")

# Adding the username and password into the dictionary and stripping the new line character.
        user_names[usr] = pswd.strip("\n")

validation = None

# Use while loop to ask and validate the username and password entered.
while True:
    validation = input("Enter username here:\n")

    pswd_validation = input("Enter password here:\n")

        # Checking whether the name and password entered are from the dictionary. Then break the while loop.
    if pswd_validation == user_names[validation] and validation in user_names.keys():
        break

# Use while loop to present the menu to the user. Input will be lower case.
while True:

        # Use if statement to seperate "admin" from normal users.
        if validation == "admin":

# This will show the menu to the admin.
                menu = input("""Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
vs - View statistics
e - Exit
: """).lower()

# This statement will execute if it is not "admin"
        else:

                # This will print the menu that the user will be able to see.
                menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

        # Use elif statements to help with decision making in the program.
        # This statement will be executed if the user chooses the option "r".
        if menu == 'r':

                # Ask admin to enter the new username and password as well as to confirm password.        
                username = input("Enter new username here:\n")

                password = input("Enter password here:\n")

                password_check = input("Enter password again to confirm:\n")

# Checking if the password is correct.
                if password == password_check:

# Open and close user.txt to append in.
                        with open("user.txt", "a") as users:

# Write the new username and password into the user.txt file.
                                users.write("\n" + username + ", " + password)

# Will display message if passwords do not match.
                else:
                        print("You have entered the wrong password.")


# This statement will be executed if the user or admin chooses the option "a".
        elif menu == 'a':

# Will ask the user to enter the username of the person whom they want to assign the task.
                username_person = input("Enter the username of the person whom the task will be assigned to:\n")

# Ask user to enter the title and description of the task.
                task_title = input("Enter the title of the task here:\n")

                task_description = input("Add a description of the task here:\n")

# Will ask user to enter the due date and the current date.
                due_date = input("Enter the due date here:\n")

                curr_date = input("Enter the current date here:\n")

# Open and close tasks.txt file to append extra info into the file.
                with open("tasks.txt", "a") as task_add:

# This info will be appended to the tasks.txt file.
                        task_add.write(f"\n" + username_person + ", " + task_title + ", " + task_description + ", " +
                        curr_date + ", " + due_date + ", " + "No")
            

# This statement will be executed if the user or admin chooses the option "va".
        elif menu == 'va':

# Open to read from tasks.txt and close the file.        
                with open("tasks.txt", "r") as task_add:

# Use for loop to access each line in the text file.
                        for lines in task_add:

# Making a string by splitting from the comma and space.
                                lines = lines.split(", ")

# Printing the outcome and use indexing to access different characters of the string.
                                print(f"""Task:\t {lines[1]}
Assigned to:\t{lines[0]}
Date assigned:\t{lines[3]}
Due date:\t{lines[4]}
Task complete?\t{lines[5]}
Task description:
{lines[2]}""")
                   
# This statement will be executed if the user or admin chooses the option "vm".
        elif menu == 'vm':

# Open and close the text file after reading from it and give it a variable.
                with open("tasks.txt", "r") as task_add:

# Use for loop to access each line in the text file.
                        for lines1 in task_add:

# Split the string where there is a comma and space to isolate characters.
                                lines1 = lines1.split(", ")

# Use if statement to check if the user that is logged in is the same as the lines that is being read.
                                if validation == lines1[0]:

# If the user is the same then the program will print out all the user's tasks.
                                        print(f"""Task:\t {lines1[1]}
Assigned to:\t{lines1[0]}
Date assigned:\t{lines1[3]}
Due date:\t{lines1[4]}
Task complete?\t{lines1[5]}
Task description:
{lines1[2]}""")

# This statement will execute when the admin chooses option "vs".
        elif menu == 'vs':

# Open and close the text file after reading from it. Store the total lines in a variable as it is equals to the
# amount of users. 
                with open("user.txt", "r") as users:
                        tot_users = len(users.readlines())

# Open and close the text file after reading from it. Store the total lines in a variable as it is equals to the
# amount of tasks.                
                with open("tasks.txt", "r") as task_add:
                        tot_tasks = len(task_add.readlines())

# Will print the results in a user friendly manner.
                        print(f"""Total users:\t{tot_users}
Total tasks:\t{tot_tasks}""")
        
# This statement will execute if the user wants to exit. Will display a message as well.
        elif menu == 'e':
                print('Goodbye!!!')
                exit()

# This statement will execute when the user enters an invalid choice.
        else:
                print("You have made a wrong choice, Please Try again")