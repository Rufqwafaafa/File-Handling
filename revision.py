file = open('revision.txt', 'r')
print(file.read())

file = open('revision.txt', 'w')
file.write('I traved to India for 10 days')

file = open('revision.txt', 'r')
print(file.read())

file = open('revision.txt', 'a')
file.write('I was missing America because of the food')

file = open('revision.txt', 'r')
print(file.read())