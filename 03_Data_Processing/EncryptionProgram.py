import random
import string

chars = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = chars.copy()

random.shuffle(key)

# print(f" chars: {chars}")
# print(f" key: {key}")

#ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original text: {plain_text}")
print(f"encrypted text: {cipher_text}")

plain_text = ""

#DECRYPT

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted text: {cipher_text}")
print(f"original text: {plain_text}")
