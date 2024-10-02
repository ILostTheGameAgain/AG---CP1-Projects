#Alec George Secret Cypher

#will ask for user input for number and a string, will shift the letters in the string by the number


#function to cypher or decypher a message
def cypher(string, shift):
    #variable for possible letters, easy to add or remove
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    #variable for new string
    cyphered_string = ""
    #if statement for testing if the shift is zero. If it is, do one for every possible shift.
    if shift == 0:
        #variable for number of shifts
        number_of_shifts = 0
        print("\n")
        #while loop to print every shift
        while number_of_shifts < len(letters):
            cyphered_string = ""
            for letter in string:
                #variable for the index of letters
                letter_number = 0
                #check every letter and shift it
                if letter in letters:
                    for x in letters:
                        if x == letter:
                            #add the shifted letter into the cyphered string
                            cyphered_string += letters[(letter_number+number_of_shifts)%len(letters)]
                        letter_number += 1
                else:
                    cyphered_string += letter
            number_of_shifts += 1
            print(cyphered_string)
        print("\n")
    else:
        for letter in string:
            #variable for the index of letters
            letter_number = 0
            #check every letter and shift it
            if letter in letters:
                for x in letters:
                    if x == letter:
                        #add the shifted letter into the cyphered string
                        cyphered_string += letters[(letter_number+shift)%len(letters)]
                    letter_number += 1
            else:
                cyphered_string += letter
        print("\n"+cyphered_string+"\n")

#while loop to take user input and cypher or decypher a message
while True:
    cypher_choice = input("Do you want to cypher or decypher a string?\n  input 1 to cypher\n  input 2 to decypher\n  your answer here: ")
    message = input("\n what would you like cyphered or decyphered? ")
    shift = input("\nWhat is the shift? Type 0 to get all possible shifts. (type an integer, positive or negative): ")
    if cypher_choice == "1":
        cypher(message, int(shift))
    else:
        cypher(message, 0-int(shift))

