

def reverse_complement(seq, material='DNA'):

    """This is the reverse complement of a sequence."""
#init the reverse complement
    rev_seq = ''

    for base in seq[::-1]:
        rev_seq += complement_base(base, material=material)

    return rev_seq

def complement_base(base, material='DNA'):
    """returns the complement base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'
