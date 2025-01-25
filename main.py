def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def countwords(book_string):
    words = book_string.split()
    print(len(words))

def countcharacters(book_string):
    lowered_string = book_string.lower()
    character_list = list(lowered_string)
    char_dict = {}
    for character in character_list:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def generate_report(char_dict):
    dictionary_list = []
    for char in char_dict:
        if char.isalpha():
            dictionary_list.append({"name": char, "num": char_dict[char]})
    dictionary_list.sort(reverse=True, key=sort_on)
    for dict in dictionary_list:
        print("The " f"'{dict["name"]}' character was found " f"{dict["num"]} times")
    

generate_report(countcharacters(main()))
