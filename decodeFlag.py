# The flag was encoded 5 times in base64, base32 and base16 
import base64

#Functions
def base16decode(encoded):
    decoded = base64.b16decode(encoded)
    return decoded
def base32decode(encoded):
    decoded = base64.b32decode(encoded)
    return decoded
def base64decode(encoded):
    decoded = base64.b64decode(encoded)
    return decoded

file = open("encodedflag.txt", "r") #open the file
encodedflag = file.readline() #read the encoded flag

#decoding 5 times in base16
for i in range (5):
    encodedflag = base16decode(encodedflag)
#decoding 5 times in base32
for i in range (5):
    encodedflag = base32decode(encodedflag)
#decoding 5 times in base64
for i in range (5):
    encodedflag = base64decode(encodedflag)

print(encodedflag)
