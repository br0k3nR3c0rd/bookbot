import sys
from stats import *

def main():
    input = len(sys.argv)
    if input < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Please specify path to the book!")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
# Take direct path to book. (Can be used as user input too with book = input())
    book = sys.argv[1]

    book_contents = get_book_text(book)

    get_word_count(book_contents)

    characters = get_character_total(book_contents)

    get_report(characters)
    print("============= END ===============")
main()
