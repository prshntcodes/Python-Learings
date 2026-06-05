"""It calculates the: 
1. GC content
2. AT content
3. Length
4. Nucleotide counts for a given DNA sequence."""


class GCContentCalculator:
    def compute(self, seq):
        gc = seq.count("G") + seq.count("C")
        return gc / len(seq)
        
class ATContentCalculator:
    def calculate(self,seq):
        at = seq.count("A") + seq.count("T")
        return at / len(seq) * 100
    
class LengthCalculator:
    def length(self,seq):
        return len(seq)
    
class NucleotideCounter:
    def count(self,seq):
        return{
            "A" : seq.count("A"),
            "T" : seq.count("T"),
            "G" : seq.count("G"),
            "C" : seq.count("C"),
        }
    
class Complementary_Seq_Generator:
    def generate(self,seq):
        complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
        return "".join(complement[base] for base in seq)