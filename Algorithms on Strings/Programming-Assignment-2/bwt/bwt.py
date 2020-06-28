# python3
import sys

def BWT(text):
    bwt_mat = []
    result = ''
    length = len(text)
    for i in range(length - 1, -1, -1):
        sub_1 = text[i:length]
        sub_2 = text[0:i]
        bwt_mat.append(sub_1 + sub_2)
    bwt_mat.sort()
    for sub in bwt_mat:
        result += sub[-1]
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
