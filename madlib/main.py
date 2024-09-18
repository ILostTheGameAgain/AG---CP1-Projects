#Alec George Proficiency Test: Madlib
name = input("name: ").strip().lower().title()
place1 = input("place: ").strip().lower()
verb1 = input("verb (present tense):").strip().lower()
noun1 = input("noun (plural): ").strip().lower()
adjective1 = input("adjective: ").strip().lower()
verb2 = input("verb (past tense): ").strip().lower()
adjective2 = input("adjective: ").strip().lower()
place2 = input("place: ").strip().lower()
verb3 = input("verb (past tense): ").strip().lower()

print("Today, "+name+" went to "+place1+" to "+verb1+" some "+noun1+". The "+noun1+" were "+adjective1+" by this, so they "+verb2+" "+name+". Feeling "+adjective2+", "+name+" started to head back to "+place2+". The "+noun1+" "+verb3+" him all the way there.")