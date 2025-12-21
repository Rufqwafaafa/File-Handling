file = open("codingal.txt", "r")
Counter = 0

Content = file.read()
CoList = Content.split(".")
print(CoList)

for i in CoList:
    print(i)
    if 1:
        Counter += 1 

print("This is the number of lines in the file")
print(Counter)