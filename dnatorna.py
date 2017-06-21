
def rna(seq):
"""
Convert dna to RNA. returned strings have the same case as the input seq
"""
    #determine if input seq is uppercase
    seq_upper = seq.isupper()
    #convert to lovercase
    seq = seq.lower()
    #swap t for u
    seq = seq.replace('t', 'u')
    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_comp(seq):

"""convert a DNA seq to RNA reverse complement
returned sequences have the same lettercase as the input
"""

    #upper or lowercase
    seq_upper = seq.isupper()

    #reverse sequence
    seq = seq[::-1]
    #convert to uppercase
    seq = seq.upper()
    #compute complement
    seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')

    #return to appropriate lettercase
    if seq_upper:
        return seq.upper()
    else:
        return seq
