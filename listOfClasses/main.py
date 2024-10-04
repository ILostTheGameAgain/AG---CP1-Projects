#Alec George   Skill Practice: List of Classes


#needs a list that will contain classes, classses will be added with user input
classes = []


#while true statement to let this repeat
while True:
    #give options to add or remove a class, remove all classes, and sort them alphabetically
    #afterwards, show all classes
    userInput = input("\nWhat would you like to do?\n type 1 to add a class\n type 2 to remove a class\n type 3 to sort classes alphabetically\n type 4 to clear the list\nyour input here: ")
    #if statement to use user input
    if userInput == "1":
        #if input is one, add a class to the end of the list
        classes.append(input("what class would you like to add? "))
    elif userInput == "2":
        #if input is two, check if the removed class is in classes, then remove it
        removed_class = input("what class would you like to remove? ")
        if removed_class in classes:
            classes.remove(removed_class)
        else:
            print("that is already not a class")
    elif userInput == "3":
        #if user input is three, sort the list
        classes.sort()
    elif userInput == "4":
        #if user input is four, clear the list
        classes.clear()
    else:
        #if anything else is put, nothing happens
        print("that is not an option.")
    #after user input, print the classes
    print("\nyour classes are:")
    for x in classes:
        print(" "+x)