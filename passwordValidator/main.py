#Alec George Skill Practice: Password Validator

#will have user input password that is strong, little like password game

#will have rules that must be followed, tell user which rules aren't followed, will display the next rule when all previous ones are followed

import time

#variable for completed rules
followed_rules = 0

#rule 1: password must be 8 characters
def rule_1(password):
    if len(password) >= 8:
        print(f"\n✔ rule 1: password is 8 characters long (length: {len(password)})")
        return True
    else:
        print(f"\nX rule 1: password is 8 characters long (length: {len(password)})")
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
        print(f"✔ rule 5: digits in password add to 25 (sum: {total})")
        return True
    else:
        print(f"X rule 5: digits in password add to 25 (sum: {total})")
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
        print(f"✔ rule 6: password includes one of the following: {list_of_words}")
        return True
    else:
        print(f"X rule 6: password includes one of the following: {list_of_words}")
        return False


#rule 7: password must include the current time
def rule_7(password):
    rule_7_correct = 0
    current_time = str((time.localtime()[3])%12) + ":" + str(time.localtime()[4])
    if current_time in password:
        rule_7_correct = 1
    if rule_7_correct:
        print(f"✔ rule 7: password includes the current time ({current_time})")
        return True
    else:
        print(f"X rule 7: password includes the current time ({current_time})")
        return False


#rule 8: password must have more vowels than consonants
def rule_8(password):
    rule_8_correct = 0
    vowels = "aeiou"
    consonants = "qwrtypsdfghjklzxcvbnm"
    vowel_count = 0
    consonant_count = 0
    
    for i in password.lower():
        if i in vowels:
            vowel_count += 1
        elif i in consonants:
            consonant_count += 1
            
    if vowel_count > consonant_count:
        rule_8_correct = 1
    if rule_8_correct:
        print(f"✔ rule 8: password has more vowels than consonants (vowels: {vowel_count}, consonants: {consonant_count})")
        return True
    else:
        print(f"X rule 8: password has more vowels than consonants (vowels: {vowel_count}, consonants: {consonant_count})")
        return False

#rule 9: at leat 1/4 of all letters must be capitalized
def rule_9(password):
    rule_9_correct = 0
    lowercase = "qwertyuiopasdfghjklzxcvbnm"
    uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lower_count = 0
    upper_count = 0

    for i in password:
        if i in lowercase:
            lower_count += 1
        elif i in uppercase:
            upper_count += 1

    if lower_count <= upper_count * 4:
        rule_9_correct = 1
    if rule_9_correct:
        print(f"✔ rule 9: at least 1/4 of letters are capitalized (lowercase: {lower_count}, uppercase: {upper_count})")
        return True
    else:
        print(f"X rule 9: at least 1/4 of letters are capitalized (lowercase: {lower_count}, uppercase: {upper_count})")
        return False


#rule 10: password must include the word pudding at least three times
def rule_10(password):
    rule_10_correct = 0
    pudding_count = 0
    for i in range(0, len(password), 7):
        if "pudding" in password[i:len(password)].lower():
            pudding_count += 1
    if pudding_count >= 3:
        rule_10_correct = 1
    if rule_10_correct:
        print(f"✔ rule 10: password must include the word pudding at least three times (pudding count: {pudding_count})")
        return True
    else:
        print(f"X rule 10: password must include the word pudding at least three times (pudding count: {pudding_count})")
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

    #test rule 8
    if rule_8(password):
        followed_rules += 1

    #test rule 9
    if rule_9(password):
        followed_rules += 1

    #test rule 10
    if rule_10(password):
        followed_rules += 1
    
    #show score
    print(f"score: {followed_rules} / 10")

    #test if all rules are followed
    if followed_rules == 10:
        break
else:
    print("\nthanks for verifying your password!")