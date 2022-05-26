# File Objects

print("---------Reading from a file----------")
f = open('text.txt', 'r')

print(f.name)
print(f.mode)

f.close() #make sure to close the file you opened

print("-------------------------------------")

#context manager
print("---------Context Manager----------")
with open('text.txt', 'r') as f1:
    #pass 
    f_contents = f1.read(100) 
    print(f_contents)
    print(type(f_contents))

print(f1.closed)

print("-------------------------------------")

with open('text.txt', 'r') as f2:
    f2_contents = f2.readlines() #readline() reads line one at a time
    print(f2_contents)
    print(type(f2_contents))

print("-------------------------------------")
with open('text.txt', 'r') as f3:
    for line in f3:
        print(line, end = '')


print("-----------------------------------------")
