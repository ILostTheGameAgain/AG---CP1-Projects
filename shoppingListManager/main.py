#Alec George Proficiency Test: Shopping list manager

shopping_list = []

while True:
    userInput = input("\nWhat would you like to do?\n type 1 to add an item\n type 2 to remove an item\n type 3 to clear the list\nyour input here: ")
    #if statement to use user input
    if userInput == "1":
        #if input is one, add an to the end of the list
        shopping_list.append(input("what would you like to add? "))
    elif userInput == "2":
        #if input is two, check if the item being removed is there or not, and remove it if it is
        removed_class = input("what would you like to remove? ")
        if removed_class in shopping_list:
            shopping_list.remove(removed_class)
        else:
            print("that is not on the list")
    elif userInput == "3":
        #if user input is four, clear the list
        shopping_list.clear()
    else:
        #if anything else is put, nothing happens
        print("that is not an option.")
    #after user input, sort and print the shopping list
    print("\nyour shopping list:")
    shopping_list.sort()
    for item in shopping_list:
        print(" "+item)