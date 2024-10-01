#Alec George Skill Practice: Pig Latin Converter

#list of vowels so it can check when it reaches one
vowels = ["a","e","i","o","u"]

#function to convert words to pig latin, it takes all letters before the first vowel, moves them to the end, and ends it in ay, possibly works for multiple words
def piglatin(word):
    global vowels
    word = word.lower().split()
    translated_string = ""
    word_letter = 0
    #does this for every word
    for x in word:
        print(word)
        word_letter = 0
        word_end = ""
        vowel = False
        #checks if letter is a vowel, and sticks everything before it to the endC
        for specific_letter in x:
            if not vowel:
                if not specific_letter in vowels:
                    word_end += specific_letter
                    word_letter += 1
                else:
                    vowel = True
        if word_letter == 0:
            word_end = "y"
        #complete the sentence
        translated_string += x[word_letter::]+word_end+"ay "
        print(translated_string)
    return translated_string
#make this repeat
while True:
    #takes user input and translates it to piglatin
    phrase = input("\ninput a word or sentence (only letters, no numbers or punctuation): ")
    print("\n"+piglatin(phrase))

