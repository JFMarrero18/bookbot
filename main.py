def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):
    number_of_words = len(book.split())
    return number_of_words

def main():
    path = "/home/fabio/workspace/github.com/jfmarrero18/bookbot/bookbot/books/frankenstein.txt"
    book = get_book_text(path)
    words =  get_word_count(book)
    print(f"{words} words found in the document")

main()