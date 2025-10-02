#main.py

from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with a non-zero status to indicate an error

    book = sys.argv[1] # Get the book path from command line arguments
    #book = input("Enter the path to the book file: ")
    text = get_book_text(book)
    chars_dict = get_num_characters(text)
    sorted_list = sort_characters(chars_dict) 

    print("====== BOOKBOT ======")
    print(f"Analysing book found at {book}...")
    print(f"----- Word Count -----")
    print(f"Found {get_num_words(text)} total words")
    print(f"----- Character Count -----")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print(f"===== END =====")


main()