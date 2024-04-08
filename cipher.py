# Prompt user to enter a sentence
print("Please enter a sentence: ")
sentence = input()     

print("You entered: " + sentence)

# Create string for indexing
alphabet="abcdefghijklmnopqrstuvwxyz"
encrypted_sentence= ""

# Set up shifting
for i in range(0, len(sentence)):
  try:
    char=sentence[i]
    encrypted_char=str(alphabet[alphabet.index(char)+5])
    encrypted_sentence+=encrypted_char
  except:
    encrypted_char=str(alphabet[0])
    encrypted_sentence+=encrypted_char

# Print Caesar Cipher
print("The encrypted sentence is: "+ encrypted_sentence)
