def encrypt(text):
    to_return=""
    for letter in text:
        if ord(letter)+shift<123:
            to_return+=chr(ord(letter)+shift)
        else:
            add=ord(letter)-122
            to_return+=chr(97+int(add))
            
    return to_return;


#start the main code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction=='encode':
    print(encrypt(text))
elif direction=="decode":
    print(decrypt(text));
else:
    print("wrong option")
    exit



