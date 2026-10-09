alphabet = input().strip()
n = int(input().strip())
def generate_strings(current_string, remaining_length):
 if remaining_length == 0:
   print(current_string)
   return
 for char in alphabet:
   generate_strings(current_string + char, remaining_length - 1)
generate_strings("", n)

