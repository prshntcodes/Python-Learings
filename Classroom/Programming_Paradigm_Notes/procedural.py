def count_bases(seq):
    gc_count = 0
    at_count = 0

    for nucleotide in seq:
        if nucleotide in "GC":
            gc_count += 1
        elif nucleotide in "AT":
            at_count += 1

    return gc_count, at_count

#----Execution-------
DNA = "ACAAAGTACGTACGTACGTACGTACAAAGT"

# Call the procedure
gc , at = count_bases(DNA)

#Output results
print(f"The sequence is: {DNA}")
print(f"GC count:{gc} \nAT count: {at}")