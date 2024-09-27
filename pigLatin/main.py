#Alec George Skill Practice: Pig Latin Converter

#list of vowels so it can check when it reaches one
vowels = ["a","e","i","o","u"]
#function to convert words to pig latin, it takes all letters before the first vowel, moves them to the end, and ends it in ay, possibly works for multiple words
def piglatin(word):
    global vowels
    word = word.lower().split()
    word_number = 0
    word_letter = 0
    while word[word_number[word_letter]] not in vowels:
        word[word_number]
        word_letter += 1
    print()



