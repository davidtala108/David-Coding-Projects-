from hash_quad import *
import string

class Concordance:
    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            with open(filename,'r') as file:
               for word in file:
                   word = word.split('\n')
                   self.stop_table.insert(word[0],word[0])
        except:
            raise FileNotFoundError

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table,
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(10000)
        try:
            stop_words_set = set(self.stop_table.get_all_keys())
            with open(filename, 'r') as file:
                line_number = 1
                for line in file:
                    line = line.replace("'", '')
                    line = self.remove_punctuation(line)
                    line = line.strip()
                    line = line.lower()
                    words = line.split()
                    words = set(words)
                    for word in words:
                        if word not in stop_words_set and word.isalpha():
                            Value = self.concordance_table.get_value(word)
                            if Value == None:
                                self.concordance_table.insert(word, str(line_number))
                            else:
                                Value = Value + ' ' + str(line_number)
                                self.concordance_table.insert(word, Value)
                    line_number += 1
        except:
            raise FileNotFoundError

    def remove_punctuation(self,text):
        translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        return text.translate(translation_table)

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""

        try:
            with open (filename, 'w') as file:
                keys = self.concordance_table.get_all_keys()
                keys.sort()
                for key in keys:
                    value = self.concordance_table.get_value(key)
                    file.write(f"{key}: {value}\n")
        except:
            raise FileNotFoundError
