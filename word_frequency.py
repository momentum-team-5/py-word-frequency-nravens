#!/usr/local/bin/python3
from string import punctuation

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
wordscounts = {}

def format_word_freq(wf):
    """Returns a string of the word frequency deictionary formatted for printing."""
    format_width = max(len(w) for w in wf)
    output_string = ""

    for w in sorted(wf, key=wf.get, reverse=True):
        count = wf[w]
        output_string += f"{w:>{format_width}} : {count} {'*' * count}\n"

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    # Open the file and read its contents
    with open(file) as text_file:
        words = text_file.read()

    # Clean up the text
    words = words.lower() # set all lowercase
    for p in punctuation: # remove all punctuation
        words = words.replace(p, '')    


    # Split the text into a list
    wordsList = words.split()

    # Remove STOP_WORDS from the list
    for s_w in STOP_WORDS:
            while s_w in wordsList:
                wordsList.remove(s_w)

    #Iterate through wordsList and count occurrences of each word
    for w in wordsList:
        if w in wordscounts:
            wordscounts[w] += 1
        else:
            wordscounts[w] = 1

    # Print out the results
    format_word_freq(wordscounts)



        

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
