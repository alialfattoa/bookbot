import sys
from stats import get_book_text, num_words,count_charachters, print_report,list_sort

#note: add book files in .txt format in the /books directory before running. sample books have been removed.
def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath= sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = num_words(book_text)

    print_report("/home/alial/bookbot/books/frankenstein.txt",book_text, word_count, count_charachters(book_text))
main()