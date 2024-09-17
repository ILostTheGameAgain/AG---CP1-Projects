#Alec George SkillPractice: Palandrom (is this supposed to be misspelled?)

word = input("What word would you like to test? ").lower().strip()
if word[0] == word[::-1]:
    print(word+" is a palindrome.")
else:
    print(word+" isn't a palindrome.")