# Alec George  Proficiency Test: Authorized

#will have a list of users, it will tell if the user is a user or an admin. If neither, they are not authorized. Can add new authorized users

#list of admins:
admins = ["banana"]
#list of users:
users = ["apple", "orange", "pear", "plum", "grape", "lemon", "lime", "eggplant"]

while True: #while loop, program continues running
    try:
        user_input = int(input("\nwhat would you like to do?\nType\n 1 to create new user\n 2 to remove user\n 3 to check if user is authorized\nYour input here: "))
        if user_input == 1:
            user_input = input("\nwhat is the name of the account you're adding? ").strip().lower()
            if user_input not in users:
                users.append(user_input)
                print(f"{user_input} has been added")
            else:
                print("that is already a user")
        if user_input == 2:
            user_input = input("\nwhat account are you removing? (type its name) ").strip().lower()
            if user_input in users:
                users.remove(user_input)
                print(f"{user_input} has been removed")
            else:
                print("that is not a user")
        if user_input == 3:
            user_input = input("\nwhat account are you checking? ").strip().lower()
            if user_input in users:
                print(f"{user_input} is a user")
            elif user_input in admins:
                print(f"{user_input} is an admin")
            else:
                print(f"{user_input} is not authorized")
    except ValueError:print("\ninput a number")