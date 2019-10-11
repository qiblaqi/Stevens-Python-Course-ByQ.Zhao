"""
This is a program intend to get the words input of user with single form and
convert words into plural form.

@author: Qi Zhao
"""

def plural(s):
    """ convert a string, returns the plural form of the string using the grammar rules above """
    if s.endswith("y") and s.endswith(("ay", "ey", "iy", "oy", "uy")):
        new_string = s + "s"
    elif s.endswith("y"):
        new_string = s[:-1] + "ies"
    elif s.endswith(("o", "ch", "sh", "s", "x", "z")):
        new_string = s + "es"
    else:
        new_string = s + "s"

    return new_string

def main():
    """ get input of words from a line """
    usr_input = input("Please type the words you want to convert to plural form: (please type them divide by whitespace)")
    word_list = usr_input.split()
    new_world_list = []
    for word in word_list:
        new_world_list.append(plural(word))
    usr_output = " ".join(new_world_list)
    print(usr_output)

if __name__ == '__main__':
    main()