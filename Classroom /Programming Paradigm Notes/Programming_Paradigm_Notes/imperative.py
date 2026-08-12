
seq = "TATATAGCGCATTAGCGATAA"
gc_count = 0
at_count = 0
for nucleotide in seq:
    
    if nucleotide in "GC":
        gc_count += 1

    elif nucleotide in "AT":
        at_count += 1

print(f"GC count: {gc_count}")
print(f"AT count :{at_count}")

