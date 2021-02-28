text = input("Enter any text with full stop: ")
y = text.split(". ")
z = ""
for line in y:
    z = "{} {}".format(z, line.capitalize())
print(z)