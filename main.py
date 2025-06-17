def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):
    number_of_words = 123

def main():
    path = "/home/fabio/workspace/github.com/jfmarrero18/bookbot/bookbot/books/frankenstein.txt"
    book = get_book_text(path)
    words =  book.split()
    #print(book)
    #book_chars = []
    print(f"{len(words)} words found in the document")
    text = "Hello there, world!"

main()