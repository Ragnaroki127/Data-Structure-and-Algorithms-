# python3
import sys

class Node():
    def __init__(self, start_ind, length, node_id):
        self.start_ind = start_ind
        self.length = length
        self.node_id = node_id
        self.children = []

def merge_nodes(node, text, result):
    if node.node_id != 0 and len(node.children) == 1:
        while len(node.children) == 1:
            node.length += node.children[0].length
            node.children = node.children[0].children

    if node.node_id != 0:
        result.append(text[node.start_ind:node.start_ind + node.length])
    
    for sub_node in node.children:
        merge_nodes(sub_node, text, result)

def build_trie(trie_root, text):
    str_len = len(text)
    n = 1
    for i in range(str_len):
        current_node = trie_root
        for j in range(i, str_len):
            current_symbol = text[j]
            for node in current_node.children:
                if text[node.start_ind] == current_symbol:
                    current_node = node
                    break
            else:
                new_node = Node(j, 1, n)
                current_node.children.append(new_node)
                current_node = new_node
                n += 1
        

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    trie_root = Node(-1, -1, 0)
    build_trie(trie_root, text)
    merge_nodes(trie_root, text, result)
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
