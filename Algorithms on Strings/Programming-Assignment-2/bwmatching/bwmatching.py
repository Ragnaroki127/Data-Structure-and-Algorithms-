# python3
import sys


def PreprocessBWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt    from position 0 to position P inclusive.
    """
    # Implement this function yourself
    length = len(bwt)
    starts = {'A':0, 'T':0, 'C':0, 'G':0, '$':0}
    alphabet = ['A', 'T', 'C', 'G', '$']
    occ_counts_before = {'A':[0]*(length+1), 'T':[0]*(length+1), 'C':[0]*(length+1), 'G':[0]*(length+1), '$':[0]*(length+1)}

    for i in range(1, length + 1):
        symbol = bwt[i - 1]
        for ch in alphabet:
            occ_counts_before[ch][i] = occ_counts_before[ch][i - 1] + 1 if ch == symbol else occ_counts_before[ch][i - 1]
        #occ_counts_before[symbol][i:] = [occ_counts_before[symbol][i - 1] + 1] * (length - i + 1)
        starts[symbol] += 1
    starts['T'] = starts['G'] + starts['C'] + starts['A'] + starts['$']
    starts['G'] = starts['C'] + starts['A'] + starts['$']
    starts['C'] = starts['A'] + starts['$']
    starts['A'] = 1
    starts['$'] = 0
    return starts, occ_counts_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and occ_counts_before.
    """
    # Implement this function yourself
    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if occ_counts_before[symbol][bottom + 1] - occ_counts_before[symbol][top] > 0:
                top = starts[symbol] + occ_counts_before[symbol][top]
                bottom = starts[symbol] + occ_counts_before[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1
     


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).  
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
