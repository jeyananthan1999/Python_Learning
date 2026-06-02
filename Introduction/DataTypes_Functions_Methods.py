text = "hi"
number = 10

print(type(text))
print(type(number))

print(len(text))
#print(len(number))         #error #TypeError: object of type 'int' has no len()

text.upper()                #no output - put it inside print statement to show output
print(text.upper()) 
#print(number.upper())      #error #AttributeError: 'int' object has no attribute 'upper'

print(number.bit_length())
#print(text.bit_length())   #AttributeError: 'str' object has no attribute 'bit_length'