f = open("C:\\Users\\kirusha\\PycharmProjects\\itstep1\\lesson18\\lines.txt", 'wb')
file = open("C:\\Users\\kirusha\\PycharmProjects\\itstep1\\lesson18\\lines.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

print(line_count)
