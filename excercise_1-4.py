def comm_substr(seq1, seq2):
    """Looking for longest common substring of a sequence"""
    #define the length of each sequence

    if len(seq1) < len(seq2):
        longseq = seq2
        shortseq = seq1
    else:
        longseq = seq1
        shortseq = seq2

    if shortseq in longseq:
        return shortseq
    #len_index is length of shortseq - 1 kind of...
    for len_index in reversed(range(len(shortseq)+1)):
        for i in range(len(shortseq) - len_index):
            subshort=shortseq[i:i+len_index]
            if subshort in longseq:
                return subshort
