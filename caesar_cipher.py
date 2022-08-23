import string


def get_letter_value(char_letter):
  lower_case_list = string.ascii_lowercase 

  upper_case_list = string.ascii_uppercase   

  if char_letter.islower():
    letter_position = lower_case_list.index(char_letter)
  elif char_letter.isupper():
      letter_position = upper_case_list.index(char_letter)

  return letter_position

def get_value_char(int_value):    
  lower_case_list = string.ascii_lowercase 

  upper_case_list =  string.ascii_uppercase  
  return upper_case_list[int_value]


def encrypt_vigenere(key_i, plaintext_i):
  cipherText = (get_letter_value(plaintext_i) + get_letter_value(key_i)) % 26
  return get_value_char(cipherText).upper()


def decrypt_vigenere(key_i, ciphertext_i):
  plaintext_i = (get_letter_value(ciphertext_i) - get_letter_value(key_i)) % 26
  return get_value_char(plaintext_i).lower()
  
o = ""

flag = input('choose the Mode (0 == encryption / 1 == decryption) ')

if flag == '0':

  plaintext_i = str(input('Enter the plaintext : '))

  key_i = str(input('Enter the Key : '))

  for i in range(0, len(plaintext_i)):
    o = o + encrypt_vigenere(key_i[i%len(key_i)],plaintext_i[i])


if flag == '1':
  ciphertext_i = str(input('Enter the cipher text : '))
  key_i = str(input('Enter the Key : '))
  for i in range(0, len(ciphertext_i)):
    o = o + decrypt_vigenere(key_i[i % len(key_i)],ciphertext_i[i])

print(o)