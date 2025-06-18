def get_word_count(book):
    number_of_words = len(book.split())
    return number_of_words

def get_character_count(book):
    character_count_dict = {}
    i = 1
    for letter in book:
        letter = letter.lower()
        if letter not in character_count_dict:
            character_count_dict[letter] = i
        else:
            value = character_count_dict[letter] + 1
            character_count_dict[letter] = value
    return character_count_dict

def sort_dictionary(dictionary):
    sorted_list = []
    for key in dictionary:
        sorted_list.append({"name": key, "num": dictionary[key]})
    return sorted_list

def sort_on(dict):
    return dict["num"]

def print_sorted_list(a_list):
    for character in a_list:
        if((character["name"]).isalpha()):
            print(f"{character["name"]}: {character["num"]}")
        else:pass