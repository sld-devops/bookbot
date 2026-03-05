def get_book_text(filepath):
    with open(filepath) as file:
    # open the file at that path; 's' represents the open file
        return file.read()
        # give back the entire contents of the file as one long string
    

def count_words(text):
    num_words = len(text.split())
    # split the string into a list of words on whitespace(no argument), then count them
    return num_words
    # send the count back to the caller

def main():
    path = "books/frankenstein.txt"
    # store the location of our file in a variable
    text = get_book_text(path)
    # call our function, use the path, and save the result in 'text'
    get_num_words = count_words(text)
    # call count_words with the book text and store the returned word count
    print(f"Found {get_num_words} total words")


main()