

my_message = 'This is a String'

my_message1 = 'What\'s your name?'

my_message2 = """Another way of using single quots is to use triple quots outside"""

print(my_message)

print(my_message1)

print(my_message2)

#String length
print('The length of message is {}', len(my_message))

#String indexing
print(my_message[0])

#slicing
print(my_message2[0:7])

#String methods
print(my_message.lower())
print(my_message.upper())

print(my_message.count('This'))
print(my_message.count('s'))


print(my_message.find('universe'))
print(my_message.find('is'))

#string.replace will not mutate the original string, but it will return a new string
my_message3 = my_message1.replace('your', 'his')
print(my_message1)
print(my_message3)

#String concatenation
greeting = 'Hello'
name = 'Yuzhu'
new_message = greeting + ', ' + name + '. Welcome!'
print(new_message)

#formatted string(put placeholders in place of our variables)
greeting1 = """What's up"""
latest_message = '{}, {}. Welcome!'.format(greeting1, name)
print(latest_message)


#F Strings
latest_message_f = f'{greeting1}, {name.upper()}. You are being welcomed in a f string!'
print(latest_message_f)


#More tricks about string
#print(dir(name))
#print(help(str))
print(help(str.endswith))
