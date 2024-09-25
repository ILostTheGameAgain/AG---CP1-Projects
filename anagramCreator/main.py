#Alec George Raid: Anagram Creator

#needs import random
import random
#make it a function to repeat it
def createAnagram(word):
    times = 0
    anagram = ""
    anagrams = []
    while times < 5:
        list_of_letters = []
        for x in word:
            list_of_letters.append(x)
        anagram = ""
        for x in word:
            letter = random.randint(0, len(list_of_letters)-1)
            anagram += list_of_letters[letter]
            list_of_letters.pop(letter)
        anagrams.append(anagram)
        times += 1
    print("\noriginal word: "+word+"\nanagrams:")
    for x in anagrams:
        print(x)
    createAnagram(input("\nWhat word would you like to create anagrams of? "))
createAnagram(input("What word would you like to create anagrams of? "))