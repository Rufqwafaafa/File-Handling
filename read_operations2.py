#This file reads the file then overwrites the file and appends more text to the end

file_read = open('file4.txt', 'r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('file4.txt', 'w')
file_write.write("File in write mode....")
file_write.write("Hi my name is Rushil and I am a gamer")
file_write.close()

file_append = open('file4.txt', 'a')
file_append.write("File in write mode....")
file_append.write("Hi my name is Rushil and I am a gamer")
file_append.close()

