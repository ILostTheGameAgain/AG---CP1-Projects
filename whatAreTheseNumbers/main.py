#Alec George Proficiency test: What are these numbers?

#user inputs a number, formats it as an integer with commas separating thousands, a float with 4 decimals, a percentage, and a dollar amount


number = int(input("Type a number: "))

print("{:,}".format(number))
print("{:.4f}".format(number))
print("{:%}".format(number))
print("${:.2f}".format(number))