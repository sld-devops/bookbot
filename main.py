def get_book_text(filepath):
    # open the file at given path
    with open(filepath) as file:
        # read it and give back the entire contents as one long string
        return file.read()
        
from stats import get_num_words, get_char_appearance, sort_on, get_sorted_count

def main():
    # store the location of our file in a variable
    path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    # call our function, use the path, and save the result in 'text'
    text = get_book_text(path)
    # call count_words on the content and store the returned word count
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    # call get_char_appearance on the content and store the returned char count
    char_counts = get_char_appearance(text)
    sorted_chars = get_sorted_count(char_counts)
    print("--------- Character Count -------")
    # print each char and its counts
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        # skip non-alphabetical characters
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print("============= END ===============")

main()