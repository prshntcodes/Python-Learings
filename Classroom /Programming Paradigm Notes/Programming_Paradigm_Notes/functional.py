"""
A simple bioinformatics pipeline demonstrating the functional paradigm.

The pipeline takes raw sequence and:
1. Removes unknown nucleotides (N)
2. Converts the sequence to uppercase
3. Calculates the sequence length
4. Calculates the GC content

Each function performs one transformation or calculation and
returns a value without modifying the original sequence.
"""

# lets consider a arbitary sequence obtained from a sequencing machine:
raw_seq = "ATatcgNNtataNNNcggcgcgcgcgcgcNNtatTTaGGCNNN"

# remove the unknown nucleotides from the raw sequence and return a cleaned sequence
def clean_seq(seq):
    return seq.replace("N","")

# make all nucleotides uppercase
def upper(seq):
    return seq.upper() 

# return sequence length
def length(seq):
    return len(seq)

# calculate and return the GC content as a percentage.
def gc_content(seq):
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    return gc


# Build the processing pipeline.
sequence = upper(clean_seq(raw_seq))
"""
It is a simple example of function composition: the output of clean_seq() becomes the input of upper(). 
clean_seq() → upper()
"""


# Display the results.
print(f"Cleaned Sequence : {sequence}")
print(f"Sequence Length: {length(sequence)}")
print(f"GC content: {gc_content(sequence):.2f}%")
