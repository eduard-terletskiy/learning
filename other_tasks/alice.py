# Alice knows that NSA agents use the following algorithm to cipher their messages.

# 1) They delete all spaces and punctuation marks.
# 2) They replace all successive identical letters with only one such letter.
# 3) They insert two identical letters at an arbitrary place many times.

# Alice has intercepted some messages which are "meaningless" sequences of letters that NSA agent 
# Bob has sent to another NSA agent Caroline about possible Alice’s location. She wants to be able 
# to restore the message as it was after step 2). Help Alice write a program in Python that removes 
# all pairs of identical letters from the message inserted in the third step. 

# The program should be executed by calling “python alice.py path/to/file.txt” from the Unix shell 
# where "path/to/file.txt" is the path to the file with a ciphered message sent by Bob. The message 
# consists of lowercase English letters and its length is at most 100 000. Output the message after 
# step 2). The program should produce an answer in less than a few seconds.

# Example
# Execute: python alice.py somefile.txt
# somefile.txt: wwaldaadicffenn
# Output: alice


import os
import sys
import itertools



class PathToFile(Exception):
    pass


def read_path():
    try:
        fn = sys.argv[1]
        if not os.path.exists(fn):
            raise PathToFile('File not found')
        return fn
    except IndexError:
        raise IndexError('Input path to file')


def open_file():
    try:
        with open(read_path()) as file_obj:
            file = file_obj.read()
        return file
    except Exception as e:
        return f"{e}"


def del_duplicate(value):
    try:
        result = ''.join(letter for letter, group in itertools.groupby(
            value) if len(tuple(group)) % 2 == 1)
        return del_duplicate(result) if len(result) != len(value) else result
    except Exception as e:
        return f'{e}'


print(del_duplicate(open_file()))