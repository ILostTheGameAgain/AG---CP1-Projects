#Alec George SkillPractice: Palandrom

word = input("What word would you like to test? ").lower().strip()
reverse_word = word[::-1].lower().strip()
if word == reverse_word:
    print(word+" is a palindrome.")
else:
    print(word+" isn't a palindrome.")