#Alec George Skill Practice: Pig Latin Converter

#list of vowels so it can check when it reaches one
vowels = ["a","e","i","o","u"]

#function to convert words to pig latin, it takes all letters before the first vowel, moves them to the end, and ends it in ay, possibly works for multiple words
def piglatin(word):
    global vowels
    #make all words in the sentence separate
    word = word.lower().split()
    #variable for final sentence
    translated_string = ""
    #tells how many letters to move to the end
    word_letter = 0
    
    #converts every word
    for x in word:
        #resets variables
        word_letter = 0
        word_end = ""
        vowel = False
        
        #checks if letter is a vowel, and sticks everything before it to the end
        for specific_letter in x:
            #only do if vowel hasn't been found
            if not vowel:
                #cut off letters that aren't vowels
                if not specific_letter in vowels:
                    word_end += specific_letter
                    word_letter += 1
                else:
                    #check if letter is a vowel
                    vowel = True
        #if first letter is vowel, end word with "yay"
        if word_letter == 0:
            word_end = "y"
        
        #complete the sentence
        translated_string += x[word_letter::]+word_end+"ay "
    return translated_string


#make this repeat
while True:
    #takes user input and translates it to piglatin
    phrase = input("\ninput a word or sentence (only letters, no numbers or punctuation): ")
    print("\n"+piglatin(phrase))

