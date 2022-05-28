# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count

#Read a text
def read_file_content(filename):

    f = open(filename, "r") 

    string = f.read()

    f.close
    
    return string

#count words in text and return a dictionary whose keys are unique word and their values.
def count_words():

    text = read_file_content("story.txt")
    split_text = text.split()
    print(split_text)
    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print (count_words())
    