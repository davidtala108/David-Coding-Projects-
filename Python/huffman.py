from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if isinstance(other,HuffmanNode):
            return self.char == other.char and self.freq == other.freq
        return False
    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if isinstance(other, HuffmanNode):
            if self.freq == other.freq:
                return self.char < other.char
            return self.freq < other.freq

def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file'''
    freqs = [0] * 256
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                freqs[ord(char)] += 1
    return freqs
def create_huff_tree(res):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns a list of all nodes in the Huffman tree'''
    if res == [0]*256:
        return None
    O = OrderedList()
    for i in range(len(res)):
        if res[i] != 0:
            N = HuffmanNode(i, res[i])
            O.add(N)
    while O.size() > 1:
        L_Node = O.pop(0)
        R_Node = O.pop(0)
        combine_freq = L_Node.freq + R_Node.freq
        if L_Node.char < R_Node.char:
            new_char = L_Node.char
        else:
            new_char = R_Node.char
        combine_node = HuffmanNode(new_char, combine_freq)
        combine_node.left = L_Node
        combine_node.right = R_Node
        O.add(combine_node)
    return O.pop(0)
def create_code(nodes):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    root = nodes
    codes =[''] * 256
    return helper_create_code(root,codes)
def helper_create_code(node, codes, P = ''):
        if node is not None:
            if node.left is not None:
                helper_create_code(node.left, codes, P + '0')
            if node.right is not None:
                helper_create_code(node.right,codes,P + '1')
            else:
                codes[node.char] = P
        return codes
def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    header = []
    for i in range(len(freqs)):
        if freqs[i] != 0:
            header.append(f'{i}')
            header.append(f'{freqs[i]}')
    K = ' '.join(header)
    return K
def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    try:
        with open(in_file, 'r'):
            pass
    except:
        raise FileNotFoundError

    X = cnt_freq(in_file)
    Z = create_huff_tree(X)
    if Z is None:
        with open(out_file, 'w') as f_out:
            f_out.write("")
        return
    W = create_code(Z)
    Y = create_header(X)

    File_encode=[]
    with open(in_file, 'r') as file:
        for line in file:
            for val in line:
                File_encode.append(W[ord(val)])

    A = ''.join(File_encode)
    with open(out_file, 'w') as f_out:
        f_out.write(Y + '\n')
        f_out.write(A)

    compressed = out_file.split('.')
    compressed.insert(1,'_compressed.')
    compressed_file = ''.join(compressed)

    hbw= HuffmanBitWriter(compressed_file)
    hbw.write_str(Y + '\n')
    hbw.write_code(A)
    hbw.close()

def  huffman_decode(encoded_file,decode_file):
    try:
        with open(encoded_file, 'r'):
            pass
    except:
        raise FileNotFoundError


    Reader_Header = HuffmanBitReader(encoded_file)
    Header = Reader_Header.read_str()
    Freq_list = parse_header(Header)
    Tree = create_huff_tree(Freq_list)
    if Tree == None:
        with open(decode_file, 'w') as f_out:
            f_out.write("")
        return
    Decoded_list=[]
    current_node = Tree
    for i in range(Tree.freq):
        while current_node.left is not None or current_node.right is not None:
            bit = Reader_Header.read_bit()
            if bit == 0:
                current_node = current_node.left
            else:
                current_node = current_node.right
        Decoded_list.append(chr(current_node.char))
        current_node = Tree

    Reader_Header.close()
    Decode_string = ''.join(Decoded_list)
    print(Decode_string)
    with open(decode_file,'w') as file:
        file.write(Decode_string)
def parse_header(header_string):
    Freq= [0]*256
    x= header_string.split()
    i=0
    while i < len(x):
        f = x[i]
        Freq[int(f)] = int(x[i+1])
        i = i + 2

    return Freq
res = parse_header("32 3 97 4 98 3  99 2 100 1")



