import sys
seq  = sys.argv[1].upper()
print(f"Sequence: {seq}")
print(f"Length: {len(seq)}")
print(f"A: {seq.count('A')}")
print(f"T: {seq.count('T')}")
print(f"G: {seq.count('G')}")
print(f"C: {seq.count('C')}")

gc = seq.count('G') + seq.count('C')
print(f"GC: {gc / len(seq) * 100}")



