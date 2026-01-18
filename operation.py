with open('revision.txt', 'w') as file:
    file.write("I went to India and enjoyed the wedding that I went to. It was very loud their and it hurt everyones ears. The celebration was fun becauase it was part of one my my family's wedding.")
file.close()

with open('revision.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are.....")
    for line in data:
        word = line.split()
        print (word)
file.close()