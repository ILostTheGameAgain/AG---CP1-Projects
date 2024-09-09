#Alec George Skill Practice: Setting, Resetting, and Resetting

staff = 32
students = 100
guests = students*2
people = students+guests
tables = str(people/12)
print ("\nyou will need "+tables+" tables.\n")


#changes
students = students-1
staff = staff-3
guests = guests-15
people = students+guests+1
tables = str(people/12)


print ("after the changes, you will need "+tables+" tables.\n")