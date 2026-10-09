dna = input()
result = ""
for char in reversed(dna):
 if char == 'A':
  result += 'T'
 elif char == 'T':
  result += 'A'
 elif char == 'G':
  result += 'C'
 elif char == 'C':
  result += 'G'
print(result)
