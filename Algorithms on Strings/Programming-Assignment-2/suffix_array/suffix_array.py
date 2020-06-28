# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  #result = []
  # Implement this function yourself
  suffixes = []
  length = len(text)
  for i in range(length):
    suffixes.append((text[i:], i))
  suffixes.sort()
  result = map(lambda x:x[1], suffixes)
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
