#	Find ASCII value of a character
try:
    inputCharacter = input("Enter a character or number :")
    ordValue = ord(inputCharacter)
    print("ASCII Value is :", ordValue)
except TypeError as e:
    print(e)