"""
this is a program contains reverse(sequence) function that return a new sequence with a reversed orger

Written by Qi Zhao 
"""

def reverse(s):
    """ reverse a string and return a new string """
    new_s = []
    for i in range(len(s)):
        new_s.append(i)
    for offset,  val in enumerate(s):
        new_s[len(s)-offset-1] = val
    new_s = str(new_s)
    new_s = new_s.replace(", ", "")
    new_s = new_s.strip("[]")
    new_s = new_s.replace("'", "")
    return new_s

def rev_enumerate(seq):
    """ use generator to create my reverse enumerate function """
    cnt = 0
    seq = reverse(seq)
    for i in seq:
        yield len(seq)-cnt-1, i
        cnt += 1

def find_second(target, string):
    """ find the second substr and return the first offset"""
    if string == "":
        return -1
    first_off = string.find(target)
    return string.find(target,first_off+1)

def get_lines(path):
    """ read a file in txt"""
    try:
        fp = open(path, "r")
    except:
        raise FileNotFoundError
    with fp:
            lines = fp.readlines()
            new_lines = []
            buff = ""
            for i in range(len(lines)):
                if lines[i].find("\\") != -1:
                    offset = lines[i].find("\\")
                    buff += lines[i][:offset]
                    continue
                else:
                    buff += lines[i]
                    new_lines.append(buff)
                    buff = ""
            for i in range(len(new_lines)):
                if new_lines[i].find("#") == 0:
                    new_lines[i] = ""
                    continue
                elif new_lines[i].find("#") > 0:
                    offset = new_lines[i].find("#")
                    new_lines[i] = new_lines[i][:offset].strip("\n")
                else:
                    new_lines[i] = new_lines[i].strip("\n")
            for i in range(len(new_lines)):
                if new_lines[i] != "":
                    yield new_lines[i]

                    
                    




