def caesar_cipher(text, shift, mode):
  
  result = ""
  for char in text:
    if char.isalnum():
      if char.isupper():
        new_ord = ord(char) + shift - 65
      else:
        new_ord = ord(char) + shift - 97
      new_ord = (new_ord % 26) + (65 if char.isupper() else 97)
      result += chr(new_ord)
    elif char.isnumeric() or char.isprintable():
      new_ord = ord(char) + shift
      result += chr(new_ord)
    else:
      result += char
  return result

text = input("Enter your text: ")
while True:
  try:
    shift = int(input("Enter the shift value (positive for right, negative for left): "))
    break
  except ValueError:
    print("Invalid shift value. Please enter an integer.")

mode = input("Enter 'encrypt' or 'decrypt': ")

if mode.lower() == "encrypt":
  processed_text = caesar_cipher(text, shift, "encrypt")
  print("Encrypted text:", processed_text)
elif mode.lower() == "decrypt":
  processed_text = caesar_cipher(text, shift, "decrypt")
  print("Decrypted text:", processed_text)
else:
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
