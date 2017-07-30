#String functions

myStr = 'Hello world!'

#Capitalize
print(myStr.capitalize())

#Swap case
print(myStr.swapcase())

#Get length
print(len(myStr))

#Replace
print(myStr.replace('world', 'everyone'))

#Count
sub = 'l'
print(myStr.count(sub))

#Startswith
print(myStr.startswith('Hello'))

#Endswith
print(myStr.endswith('Hello'))

#Split to list
print(myStr.split())

#Find
print(myStr.find('world'))

#Index
print(myStr.index('world'))

#Is all alphanumeric?
print(myStr.isalnum())

#Is all alphabetic?
print(myStr.isalpha())

#Is all numeric?
print(myStr.isnumeric())