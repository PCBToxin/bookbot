import sys
from stats import get_num_words
from stats import character_count
from stats import sorted_dictionary_list

def get_book_text(in_filepath):
    file_contents = ""
    
    with open(in_filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    contents = ""
    path_to_book = ""
    word_count = 0
    char_count = {}
    sorted_count = {}

    if len(sys.argv) == 1:
        print('Usage: python3 main.py <path_to_book>')
        print(f'Exiting: {sys.argv[0]}')
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]

    # contents = get_book_text("/home/pcbtoxin/workspace/github.com/PCBToxin/bookbot/books/frankenstein.txt")
    contents = get_book_text(path_to_book)
    word_count = get_num_words(contents)
    char_count = character_count(contents)
    sorted_count = sorted_dictionary_list(char_count)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')

    #for char, count in char_count.items():
        #print(f'{repr(char)}: {count}')
        #print("{0}: {1}".format(repr(char), count))
        #pass
  
    for char, count in sorted_count.items():
        if char.isalpha() == True:
            print("{0}: {1}".format(char, count))

    print('============= END ===============')
    pass

main ()