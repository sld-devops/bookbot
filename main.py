import sys

def get_book_text(filepath):
    # open the file at given path
    with open(filepath) as file:
        # read it and give back the entire contents as one long string
        return file.read()
        
from stats import get_num_words, get_char_appearance, sort_on, get_sorted_count

def main():
    # check if argv has length of 2 items (script name and book path)
    # if not, explain to use the command to run the book bot
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        # do not crash, instead exit program with error code (not 0)
        sys.exit(1)
    # gets second arguments from len sys (which is path)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    # call our function, use the path, and save the result in 'text'
    text = get_book_text(book_path)
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