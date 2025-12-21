file = open('file3.txt', 'r')
print(file.read())
file.close()

file = open('file3.txt', 'r')
print("\n Read in Parts \n")
print(file.read(50))
file.close()

file = open('file3.txt', 'a')
file.write("Hi! I am Rushil and I'm 14 years old.")
file.close()
