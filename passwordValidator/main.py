#Alec George Skill Practice: Password Validator

#will have user input password that is strong, little like password game

#will have rules that must be followed, tell user which rules aren't followed, will display the next rule when all previous ones are followed

#variable for completed rules
followed_rules = 0

#rule 1: password must be 8 characters
def rule_1(password):
    if len(password) >= 8:
        print("\n✔ rule 1: password is 8 characters long")
        return True
    else:
        print("\nX rule 1: password is 8 characters long")
        return False


#rule 2: password must have a number
def rule_2(password):
    rule_2_correct = 0
    numbers = "0123456789"
    for i in password:
        if i in numbers:
            rule_2_correct = 1
    if rule_2_correct:
        print("✔ rule 2: password includes a number")
        return True
    else:
        print("X rule 2: password includes a number")
        return False


#rule 3: password must have a special character
def rule_3(password):
    rule_3_correct = 0
    special_characters = "`~!@#$%^&*()-_=+{[}]|\\:;\"\',./<>?"
    for i in password:
        if i in special_characters:
            rule_3_correct = 1
    if rule_3_correct:
        print("✔ rule 3: password includes a special character")
        return True
    else:
        print("X rule 3: password includes a special character")
        return False
    
    
#rule 4: password must have a capital letter
def rule_4(password):
    rule_4_correct = 0
    capitals = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for i in password:
        if i in capitals:
            rule_4_correct = 1
    if rule_4_correct:
        print("✔ rule 4: password includes a capital letter")
        return True
    else:
        print("X rule 4: password includes a capital letter")
        return False


#rule 5: digits in password must add to 25
def rule_5(password):
    rule_5_correct = 0
    numbers = "0123456789"
    total = 0
    for i in password:
        if i in numbers:
            total += int(i)

    if total == 25:
        rule_5_correct = 1
    if rule_5_correct:
        print("✔ rule 5: digits in password add to 25")
        return True
    else:
        print("X rule 5: digits in password add to 25")
        return False


#rule 6: password must include a specific word
def rule_6(password):
    rule_6_correct = 0
    list_of_words = ""
    possible_words = ["apple", "orange", "banana", "grape", "blueberry"]

    for i in possible_words:
        list_of_words += i +", "
        if i in password.lower():
            rule_6_correct = 1
    
    if rule_6_correct:
        print(f"✔ rule 4: password includes one of the following: {list_of_words}")
        return True
    else:
        print(f"X rule 4: password includes one of the following: {list_of_words}")
        return False


#rule 7: password must include the current time
import time
def rule_7(password):
    rule_7_correct = 0
    print(time.strptime())
    if rule_7_correct:
        print("✔ rule 4: password includes the current time")
        return True
    else:
        print("X rule 4: password includes the current time")
        return False



while True: #use break when password is valid
    followed_rules = 0
    
    password = input("what is your password?\n")

    #print rules not followed
    #test rule 1
    if rule_1(password):
        followed_rules += 1

    #test rule 2
    if rule_2(password):
        followed_rules += 1

    #test rule 3
    if rule_3(password):
        followed_rules += 1

    #test rule 4
    if rule_4(password):
        followed_rules += 1

    #show score
    print(f"score: {followed_rules} / 4")

    #test if all rules are followed
    if followed_rules == 4:
        break

print("\ngood job! you technically have a good password.")
time.sleep(1)

keep_going = input("however, would you like your password to be stronger?\n(y/n): ")
if keep_going == "y":
    print("\nyou don't know what you're getting yourself into.\n")

while keep_going == "y":
    followed_rules = 0
    
    password = input("what is your password?\n")

    #print rules not followed
    #test rule 1
    if rule_1(password):
        followed_rules += 1

    #test rule 2
    if rule_2(password):
        followed_rules += 1

    #test rule 3
    if rule_3(password):
        followed_rules += 1

    #test rule 4
    if rule_4(password):
        followed_rules += 1
    
    #test rule 5
    if rule_5(password):
        followed_rules += 1

    #test rule 6
    if rule_6(password):
        followed_rules += 1
    
    #test rule 7
    if rule_7(password):
        followed_rules += 1
    
    #show score
    print(f"score: {followed_rules} / 4")

    #test if all rules are followed
    if followed_rules == 4:
        break
else:
    print("\nthanks for verifying your password!")