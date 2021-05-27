Message = input("Please enter your msg \n").lower()

print(Message)

no_of_shifts = input("Please enter the number of shifts to encrypt your msg\n")

'''if isinstance(no_of_shifts,int):
    pass
else:
    no_of_shifts= input("Please enter again a number\n")'''

def cipher(msg,no_of_shifts):
    cipher_text=[]
    for i in msg:
        if i == " ":
            cipher_text.append(i)
        else:    
            b = ord(i) + int(no_of_shifts)
            if b > 122:
                b = 97 + ((b-122)-1)
                cipher_text.append(chr(b))
            else:
                cipher_text.append(chr(b))
    return ''.join(cipher_text)

c_code=cipher(Message,no_of_shifts)
print(f'cipered text {c_code}')


def decipher(c_code , no_of_shifts):
    decpher_text = []
    for i in c_code:
        if i==" ":
            decpher_text.append(i)
        else:
            b = ord(i) - int(no_of_shifts)
            if b < 97:
                b = 122 - ((97-b)-1)
                decpher_text.append(chr(b))
            else:
                decpher_text.append(chr(b))
    return ''.join(decpher_text)

d_code= decipher(c_code,no_of_shifts)
print(d_code)





