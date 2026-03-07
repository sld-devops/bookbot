def get_book_text(filepath):
    # open the file at given path
    with open(filepath) as file:
        # read it and give back the entire contents as one long string
        return file.read()
        
from stats import get_num_words, get_char_appearance

def main():
    # store the location of our file in a variable
    path = "books/frankenstein.txt"
    # call our function, use the path, and save the result in 'text'
    text = get_book_text(path)
    # call count_words on the content and store the returned word count
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    # call get_char_appearance on the content and store the returned char count
    char_counts = get_char_appearance(text)
    print(char_counts)

    # print(text) - output the contents to the console

main()