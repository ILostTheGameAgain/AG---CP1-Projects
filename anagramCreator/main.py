#Alec George Raid: Anagram Creator

#needs import random
import random
#make it a function to repeat it
def createAnagram(word):
    #variable for number of anagrams
    number_of_anagrams = input("How many anagrams do you want? ")
    #variables that reset when function starts
    times = 0
    anagram = ""
    anagrams = []
    #angagram creator that repeats a number of times, once for each anagram
    while times < int(number_of_anagrams):
        #put every letter in a list
        list_of_letters = []
        for x in word:
            list_of_letters.append(x)
        anagram = ""
        #rearange the letters in the list to form new anagrams
        for x in word:
            letter = random.randint(0, len(list_of_letters)-1)
            anagram += list_of_letters[letter]
            list_of_letters.pop(letter)
        anagrams.append(anagram)
        times += 1
    #print the results
    print("\noriginal word: "+word+"\nanagrams:")
    for x in anagrams:
        print(x)
    #allow the user to make more anagrams
    createAnagram(input("\nWhat word would you like to create anagrams of? "))
#call function for first time
createAnagram(input("What word would you like to create anagrams of? "))