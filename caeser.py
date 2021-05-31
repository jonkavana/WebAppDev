def encrypt2(plain_text, offset):
    cipher_text = ""
    
    for i in plain_text:
        numerical_value = ord(i)
        if (i.isupper()):
            adapt = (((numerical_value + offset - 65)%26) + 65)
            cipher_text += chr(adapt)
        elif numerical_value == 32:
            cipher_text += i
        else:
            adapt = (((numerical_value + offset - 97)%26) + 97)
            cipher_text += chr(adapt)
    return cipher_text
print(encrypt2("hello lads", 2))