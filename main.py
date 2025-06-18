from stats import get_word_count, get_character_count, sort_dictionary, sort_on, print_sorted_list
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        path = f"/home/fabio/workspace/github.com/jfmarrero18/bookbot/bookbot/{book_path}"
        book = get_book_text(path)
        words =  get_word_count(book)
        print(f"{words} words found in the document")
        characters_counted = get_character_count(book)
        #print(characters_counted)
        new_list = sort_dictionary(characters_counted)
        new_list.sort(reverse = True, key = sort_on)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        print_sorted_list(new_list)
        print("============= END ===============")
    
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()