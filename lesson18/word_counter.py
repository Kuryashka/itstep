file = open("C:\\Users\\kirusha\\PycharmProjects\\itstep1\\lesson18\\file_with_words.txt", "rt")
data = file.read()
words = data.split()

print(len(words))
