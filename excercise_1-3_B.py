

def reverse_complement(seq, material='DNA'):

    """This is the reverse complement of a sequence without loops"""
#init the reverse complement

    rev_seq = seq[::-1]
    rep_seq=rev_seq.replace('Aa','x').replace('Tt', 'y').replace('Cc','w').replace('Gg','z').replace('Uu','y')
    if material == 'DNA':
        comp_seq=rep_seq.replace('x','T').replace('w','G').replace('z','C').replace('y','A')
    elif material == 'RNA':
        comp_seq=rep_seq.replace('x','U').replace('w','G').replace('z','C').replace('y','A')

    return comp_seq
