file = open('sample.txt','r')
print(file.read())
file.close()

file = open('File.txt','w')
print(file.write('I am the best programmer and ethical hacker'))
file.close()

file = open('sample.txt','a')
print(file.write('\n My favourite subject is Biology'))
file.close()