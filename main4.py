#Takes teh tect from file1 where line does not start with coding and writes it into file2

file1 = open('codingal1.txt', 
                        'r')
file2 = open('codingal_updated.txt', 
                                'w')

for line in file1.readlines():
    if not(line.startswith('Coding')):
        print(line)
        file2.write(line)

file2.close()
file1.close()