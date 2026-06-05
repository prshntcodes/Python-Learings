from readers import FASTAReader
from validators import DNAValidator
from analyzers import GCContentCalculator, ATContentCalculator, LengthCalculator, NucleotideCounter, Complementary_Seq_Generator
from analyzers import ATContentCalculator



def main():
    fasta_data = """>Example
    AAATGCAAATTATGCTTTCCATGCCCCGTATATAGGGGATGCCCAACA"""

    reader = FASTAReader()
    validator = DNAValidator()
    gc_calc = GCContentCalculator()
    at_calc = ATContentCalculator()
    len_calc = LengthCalculator()
    nuc_count = NucleotideCounter()
    comp_seq_gen = Complementary_Seq_Generator()

    seq = reader.read(fasta_data)
    validator.validate(seq)
    gc = gc_calc.compute(seq)
    at = at_calc.calculate(seq)
    seq_length = len_calc.length(seq)
    nucleotide_counts = nuc_count.count(seq)
    complementary_seq = comp_seq_gen.generate(seq)

    print("Sequence:", seq)
    print(f"GC Content: {gc * 100:.2f}")
    print(f"AT Content:{at:.2f}" )
    print("Sequence Length:", seq_length)
    print("Nucleotide Counts:", nucleotide_counts)
    print("Complementary Sequence:", complementary_seq)
   


if __name__ == "__main__":
    main()

"""
The output for the above code will be:
Sequence: AAATGCAAATTATGCTTTCCATGCCCCGTATATAGGGGATGCCCAACA
GC Content: 43.75
AT Content:56.25
Sequence Length: 48
Nucleotide Counts: {'A': 15, 'T': 12, 'G': 9, 'C': 12}
Complementary Sequence: TTTACGTTTAATACGAAAGGTACGGGGCATATATCCCCTACGGGTTGT
"""