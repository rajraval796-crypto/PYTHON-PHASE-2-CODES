text = input("Enter the input text: ")
shift = int(input("Enter the shift value: "))

cipher = ""

for char in text:
  if char.isupper():
    cipher += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
  elif char.islower():
    cipher += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
  else:
    cipher += char

print(f"Cipher: {cipher}")

# text = input("Enter the input text: ")
# shift = int(input("Enter the shift value: "))

# cipher = ""
decrypt=""
for char in cipher:
  if char.isupper():
    decrypt += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
  elif char.islower():
    decrypt += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
  else:
    decrypt += char

print(f"Cipher: {decrypt}")

