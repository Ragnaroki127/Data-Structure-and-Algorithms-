# python3
import sys

def count_sort(bwt):
    count = {'A':0, 'T':0, 'C':0, 'G':0, '$':0}
    last_col = []
    first_col_dict = {'A':[], 'T':[], 'C':[], 'G':[], '$':[]}
    for char in bwt:
        last_col.append((char, count[char]))
        first_col_dict[char].append((char, count[char]))
        count[char] += 1
    first_col = first_col_dict['$'] + first_col_dict['A'] + first_col_dict['C'] + first_col_dict['G'] + first_col_dict['T']
    return first_col, last_col, count


def InverseBWT(bwt):
    # write your code here
    result = '$'
    length = len(bwt)
    first_col, last_col, count = count_sort(bwt)
    result += last_col[0][0]
    last_item = last_col[0]
    while len(result) < length:
        if last_item[0] == 'A':
            ind = 1 + last_item[1]
        elif last_item[0] == 'C':
            ind = 1 + count['A'] + last_item[1]
        elif last_item[0] == 'G':
            ind = 1 + count['A'] + count['C'] + last_item[1]
        elif last_item[0] == 'T':
            ind = 1 + count['A'] + count['C'] + count['G'] + last_item[1]
        result += last_col[ind][0]
        last_item = last_col[ind]
    return result[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
