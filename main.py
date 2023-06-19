#importing art.py file
import art
print(art.logo)

#start encode function
def cipher(text):
    to_return=""
    for letter in text:
        if ord(letter)+shift<123:
            to_return+=chr(ord(letter)+shift)
        else:
            add=ord(letter)+shift-123
            to_return+=chr(97+int(add))
            
    return to_return;


#start the main code

restart='y'

while restart=='y':

    direction = input("Type 'encode' to cipher, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift%=26

    if direction=='encode':
        print(cipher(text))
    elif direction=="decode":
        shift=26-shift
        print(cipher(text))
    else:
        print("wrong option")
        exit

    restart=input("Do you want to restart the program (y/n) ")

